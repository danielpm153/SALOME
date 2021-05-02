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

A = 28.55#Largeur de la pièce(Largura da peça)
B = 14#Hauteur de la pièce(Altura da peça)
C = 11.14#profondeur de la pièce(profundidade da peça)
D = 9.75#Hauteur de la partie interne(Altura da parte interna)

D1 = 9.9#Diamètre intérieur(Diametro interno)
D2 = 21.75#Diamètre externe(Diametro externo)

R1 = 0.3#Rayon du filet intérieur(Raio do filete interno)

NOM = "ER%.1f_%.1f_%.1f"%(A,B,C)#Nom de fichier .STL

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
SketchConstraintLength_1 = Sketch_1.setLength(SketchLine_1.result(), A)
SketchConstraintLength_2 = Sketch_1.setLength(SketchLine_2.result(), B)
SketchProjection_1 = Sketch_1.addProjection(model.selection("VERTEX", "Origin"), False)
SketchPoint_1 = SketchProjection_1.createdFeature()
SketchConstraintCoincidence_5 = Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchAPI_Point(SketchPoint_1).coordinates())

model.do()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Face_1 = model.addFace(Part_1_doc, [model.selection("FACE", "PartSet/Sketch_1/Face-SketchLine_1r-SketchLine_2f-SketchLine_3f-SketchLine_4f")])
Extrusion_1 = model.addExtrusion(Part_1_doc, [model.selection("FACE", "PartSet/Sketch_1/Face-SketchLine_1r-SketchLine_2f-SketchLine_3f-SketchLine_4f")], model.selection(), C, 0)
Sketch_2 = model.addSketch(Part_1_doc, model.selection("FACE", "Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_1"))
SketchCircle_1 = Sketch_2.addCircle(A/2, -C/2, D1/2)
SketchCircle_2 = Sketch_2.addCircle(A/2, -C/2, D1/2)
SketchConstraintCoincidence_6 = Sketch_2.setCoincident(SketchCircle_1.center(), SketchCircle_2.center())
SketchConstraintRadius_1 = Sketch_2.setRadius(SketchCircle_1.results()[1], D1/2)
SketchConstraintRadius_2 = Sketch_2.setRadius(SketchCircle_2.results()[1], D2/2)
SketchProjection_2 = Sketch_2.addProjection(model.selection("VERTEX", "[Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_1][Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_2][Extrusion_1_1/To_Face]"), False)
SketchPoint_2 = SketchProjection_2.createdFeature()
SketchConstraintDistanceVertical_1 = Sketch_2.setVerticalDistance(SketchCircle_2.center(), SketchAPI_Point(SketchPoint_2).coordinates(), C/2)
SketchConstraintDistanceHorizontal_1 = Sketch_2.setHorizontalDistance(SketchAPI_Point(SketchPoint_2).coordinates(), SketchCircle_2.center(), A/2)

model.do()
Face_2 = model.addFace(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchCircle_2_2f-SketchCircle_1_2r")])
ExtrusionCut_1 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchCircle_2_2f-SketchCircle_1_2r")], model.selection(), 0, D, [model.selection("SOLID", "Extrusion_1_1")])
Fillet_1 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[ExtrusionCut_1_1/Modified_Face&Extrusion_1_1/To_Face][(ExtrusionCut_1_1/Modified_Face&Extrusion_1_1/From_Face)(ExtrusionCut_1_1/Modified_Face&Extrusion_1_1/To_Face)(ExtrusionCut_1_1/Modified_Face&ExtrusionCut_1_1/From_Face)]")], R1)
Fillet_2 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_1_1/MF:Fillet&Sketch_1/SketchCircle_2_2][ExtrusionCut_1_1/Modified_Face&Extrusion_1_1/From_Face]")], R1)
Fillet_3 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_2_1/MF:Fillet&Extrusion_1_1/From_Face][(Fillet_2_1/MF:Fillet&Extrusion_1_1/From_Face)(Fillet_2_1/MF:Fillet&ExtrusionCut_1_1/From_Face)(Fillet_2_1/MF:Fillet&PartSet/Sketch_1/SketchLine_1)2(Fillet_2_1/MF:Fillet&Sketch_1/SketchCircle_2_2)2(Fillet_2_1/GF:Fillet&Fillet_2_1/FilletSelected)2(Fillet_1_1/GF:Fillet&Fillet_1_1/FilletSelected)2(Fillet_1_1/MF:Fillet&Extrusion_1_1/To_Face)2(Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_2)2(Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_3)2(Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_4)2(ExtrusionCut_1_1/Generated_Face&Sketch_1/SketchCircle_1_2)2]")], R1)
Fillet_4 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_1_1/MF:Fillet&Extrusion_1_1/To_Face][(Fillet_3_1/MF:Fillet&PartSet/Sketch_1/SketchLine_1)(Fillet_3_1/MF:Fillet&ExtrusionCut_1_1/From_Face)(Fillet_3_1/MF:Fillet&Sketch_1/SketchCircle_2_2)(Fillet_1_1/MF:Fillet&Extrusion_1_1/To_Face)]")], R1)

#Exportez le fichier ".XAO" dans le dossier ./temp
Export_1 = model.exportToXAO(Part_1_doc, adresse_temp+'\\shaper_rmj10kp6.xao', model.selection("SOLID", "Fillet_4_1"), 'XAO')

model.end()

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

#importer le fichier ".XAO" du dossier ./temp
(imported, Fillet_4_1, [], [], []) = geompy.ImportXAO(adresse_temp+"/shaper_rmj10kp6.xao")
#Exporter le fichier ".STL" vers le dossier ./WORK
geompy.ExportSTL(Fillet_4_1, adresse+"/%s.stl"%(NOM), True, 0.001, True)
#Ajouter à "Geometry"
geompy.addToStudy( Fillet_4_1, NOM )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
