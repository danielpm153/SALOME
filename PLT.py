#!/usr/bin/env python

import sys
import salome
import os
import tempfile

salome.salome_init()

import salome_notebook

notebook = salome_notebook.NoteBook()

import salome_version#Prendre la version du SALOME
#Salome version
if salome_version.getVersions() >= [9,4,0]:
  #Si le dossier "WORK" n'existe pas, créez-le, sinon il passe.
  #pour la version 9.4.0
  try:
    os.makedirs("WORK")
  except OSError:
    pass
  adresseAUX = os.getcwd()+'/WORK'
else:
  #Salome 9.3.0
  adresseAUX = os.getcwd()

#Adresse du dossier
adresse = adresseAUX#C'est possible de mettre autre dossier(Si le dossier WORK est protege), par exemple: adresse = "C:/Users/Daniel ~/Desktop"

sys.path.insert(0, r'%s'%(adresse))

adresse_temp = tempfile.gettempdir()

A = 14#largeur
B = 1.5#hauteur
C = 5#Profondeur

R = 0.8#Rayon de courbure du congé

NOM = "PLT%.1f_%.1f_%.1f"%(A,C,B)#Nom de fichier .STL

###
### SHAPER component
###

from SketchAPI import *

from salome.shaper import model

#Sketch construction
model.begin()
partSet = model.moduleDocument()
Sketch_1 = model.addSketch(partSet, model.defaultPlane("XOZ"))
SketchLine_1 = Sketch_1.addLine(A, B, 0, B)
SketchLine_2 = Sketch_1.addLine(0, B, 0, 0)
SketchLine_3 = Sketch_1.addLine(0, 0, A, 0)
SketchLine_4 = Sketch_1.addLine(A, 0, A, B)
SketchConstraintCoincidence_1 = Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_1.startPoint())
SketchConstraintCoincidence_2 = Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_2.startPoint())
SketchConstraintCoincidence_3 = Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_3.startPoint())
SketchConstraintCoincidence_4 = Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_4.startPoint())
SketchConstraintHorizontal_1 = Sketch_1.setHorizontal(SketchLine_1.result())
SketchConstraintVertical_1 = Sketch_1.setVertical(SketchLine_2.result())
SketchConstraintHorizontal_2 = Sketch_1.setHorizontal(SketchLine_3.result())
SketchConstraintVertical_2 = Sketch_1.setVertical(SketchLine_4.result())
SketchConstraintDistanceHorizontal_1 = Sketch_1.setHorizontalDistance(SketchLine_2.startPoint(), SketchLine_1.startPoint(), A)
SketchConstraintDistanceVertical_1 = Sketch_1.setVerticalDistance(SketchLine_4.endPoint(), SketchLine_3.endPoint(), B)
SketchProjection_1 = Sketch_1.addProjection(model.selection("VERTEX", "Origin"), False)
SketchPoint_1 = SketchProjection_1.createdFeature()
SketchConstraintCoincidence_5 = Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchAPI_Point(SketchPoint_1).coordinates())


model.do()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Face_1 = model.addFace(Part_1_doc, [model.selection("FACE", "PartSet/Sketch_1/Face-SketchLine_1r-SketchLine_2f-SketchLine_3f-SketchLine_4f")])
Extrusion_1 = model.addExtrusion(Part_1_doc, [model.selection("FACE", "PartSet/Sketch_1/Face-SketchLine_1r-SketchLine_2f-SketchLine_3f-SketchLine_4f")], model.selection(), C, 0)
Fillet_1 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_4][Extrusion_1_1/To_Face]")], R)
Fillet_2 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_1_1/MF:Fillet&PartSet/Sketch_1/SketchLine_4][Extrusion_1_1/From_Face]")], R)
Fillet_3 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_1_1/MF:Fillet&Extrusion_1_1/To_Face][Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_2]")], R)
Fillet_4 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_3_1/MF:Fillet&PartSet/Sketch_1/SketchLine_2][Fillet_2_1/MF:Fillet&Extrusion_1_1/From_Face]")], R)

#Exportez le fichier ".XAO" dans le dossier ./temp
Export_1 = model.exportToXAO(Part_1_doc, adresse_temp+'\\shaper_mve3cacu.xao', model.selection("SOLID", "Fillet_4_1"), 'XAO')

model.end()

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
#importer le fichier ".XAO" du dossier ./temp
(imported, Fillet_4_1, [], [], []) = geompy.ImportXAO(adresse_temp+"/shaper_mve3cacu.xao")
#Exporter le fichier ".STL" vers le dossier ./WORK
geompy.ExportSTL(Fillet_4_1, adresse+"/%s.stl"%(NOM), True, 0.001, True)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
#Ajouter à "Geometry"
geompy.addToStudy( Fillet_4_1, NOM )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
