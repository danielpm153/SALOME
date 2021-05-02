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

Xi = 0 #position iniciale X et Z
Zi = 0

A = 14 #Largeur de piece(Largura peça)
B = 3.5 #Hauteur de la piece(Altura peça)
L1 = 11 #largeur entre les parties extrêmes internes
L2 = 3 #largeur de la partie intérieure
D = 2 #Hauteur interne(Altura da parte)

F = 5 #profondeur de la piece(Profundidade peça)

R1 = 0.8#Rayon de conge

NOM = "PlanarE%.1f_%.1f_%.1f"%(A,B,F)#Nom de fichier .STL

C = (A-L1)/2 #Largeur de la partie haut(Largura da parte)
E = (L1-L2)/2 #Largeur de la partie inférieure(Largura da parte fundo)

###
### SHAPER component
###

from SketchAPI import *

from salome.shaper import model

#Sketch construction
model.begin()
partSet = model.moduleDocument()
Sketch_1 = model.addSketch(partSet, model.defaultPlane("XOZ"))
SketchLine_1 = Sketch_1.addLine(Xi, Zi, Xi, Zi+B)
SketchConstraintVertical_1 = Sketch_1.setVertical(SketchLine_1.result())
SketchLine_2 = Sketch_1.addLine(Xi, Zi+B, Xi+C, Zi+B)
SketchConstraintCoincidence_1 = Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_2.startPoint())
SketchConstraintHorizontal_1 = Sketch_1.setHorizontal(SketchLine_2.result())
SketchLine_3 = Sketch_1.addLine(Xi+C, Zi+B, Xi+C, Zi+B-D)
SketchConstraintCoincidence_2 = Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_3.startPoint())
SketchConstraintVertical_2 = Sketch_1.setVertical(SketchLine_3.result())
SketchLine_4 = Sketch_1.addLine(Xi+C, Zi+B-D, Xi+C+E, Zi+B-D)
SketchConstraintCoincidence_3 = Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_4.startPoint())
SketchLine_5 = Sketch_1.addLine(Xi+C+E, Zi+B-D, Xi+C+E, Zi+B)
SketchConstraintCoincidence_4 = Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_5.startPoint())
SketchLine_6 = Sketch_1.addLine(Xi+C+E, Zi+B, Xi+C+E+(A-2*C-2*E), Zi+B)
SketchConstraintCoincidence_5 = Sketch_1.setCoincident(SketchLine_5.endPoint(), SketchLine_6.startPoint())
SketchConstraintHorizontal_2 = Sketch_1.setHorizontal(SketchLine_6.result())
SketchLine_7 = Sketch_1.addLine(Xi+C+E+(A-2*C-2*E), Zi+B, Xi+C+E+(A-2*C-2*E), Zi+B-D)
SketchConstraintCoincidence_6 = Sketch_1.setCoincident(SketchLine_6.endPoint(), SketchLine_7.startPoint())
SketchLine_8 = Sketch_1.addLine(Xi+C+E+(A-2*C-2*E), Zi+B-D, Xi+C+E+(A-2*C-2*E)+E, Zi+B-D)
SketchConstraintCoincidence_7 = Sketch_1.setCoincident(SketchLine_7.endPoint(), SketchLine_8.startPoint())
SketchLine_9 = Sketch_1.addLine(Xi+C+E+(A-2*C-2*E)+E, Zi+B-D, Xi+C+E+(A-2*C-2*E)+E, Zi+B)
SketchConstraintCoincidence_8 = Sketch_1.setCoincident(SketchLine_8.endPoint(), SketchLine_9.startPoint())
SketchConstraintVertical_3 = Sketch_1.setVertical(SketchLine_9.result())
SketchLine_10 = Sketch_1.addLine(Xi+C+E+(A-2*C-2*E)+E, Zi+B, Xi+A, Zi+B)
SketchConstraintCoincidence_9 = Sketch_1.setCoincident(SketchLine_9.endPoint(), SketchLine_10.startPoint())
SketchLine_11 = Sketch_1.addLine(Xi+A, Zi+B, Xi+A, Zi)
SketchConstraintCoincidence_10 = Sketch_1.setCoincident(SketchLine_10.endPoint(), SketchLine_11.startPoint())
SketchConstraintVertical_4 = Sketch_1.setVertical(SketchLine_11.result())
SketchLine_12 = Sketch_1.addLine(Xi+A, Zi, Xi, Zi)
SketchConstraintCoincidence_11 = Sketch_1.setCoincident(SketchLine_11.endPoint(), SketchLine_12.startPoint())
SketchConstraintCoincidence_12 = Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchLine_12.endPoint())
SketchConstraintHorizontal_3 = Sketch_1.setHorizontal(SketchLine_12.result())
SketchConstraintHorizontal_4 = Sketch_1.setHorizontal(SketchLine_8.result())
SketchConstraintHorizontal_5 = Sketch_1.setHorizontal(SketchLine_10.result())
SketchConstraintVertical_5 = Sketch_1.setVertical(SketchLine_5.result())
SketchConstraintVertical_6 = Sketch_1.setVertical(SketchLine_7.result())
SketchConstraintHorizontal_6 = Sketch_1.setHorizontal(SketchLine_4.result())
SketchConstraintEqual_1 = Sketch_1.setEqual(SketchLine_1.result(), SketchLine_11.result())
SketchConstraintEqual_2 = Sketch_1.setEqual(SketchLine_2.result(), SketchLine_10.result())
SketchConstraintEqual_3 = Sketch_1.setEqual(SketchLine_3.result(), SketchLine_5.result())
SketchConstraintEqual_4 = Sketch_1.setEqual(SketchLine_5.result(), SketchLine_7.result())
SketchConstraintEqual_5 = Sketch_1.setEqual(SketchLine_4.result(), SketchLine_8.result())
SketchConstraintDistanceVertical_1 = Sketch_1.setVerticalDistance(SketchLine_2.endPoint(), SketchLine_3.endPoint(), D)
SketchConstraintDistanceVertical_2 = Sketch_1.setVerticalDistance(SketchLine_10.endPoint(), SketchLine_12.startPoint(), B)
SketchConstraintDistanceHorizontal_1 = Sketch_1.setHorizontalDistance(SketchLine_1.endPoint(), SketchLine_2.endPoint(), C)
SketchConstraintDistanceHorizontal_2 = Sketch_1.setHorizontalDistance(SketchLine_3.endPoint(), SketchLine_4.endPoint(), E)
SketchConstraintLength_1 = Sketch_1.setLength(SketchLine_12.result(), A)

#Cette partie fixe l'objet à l'origine
#SketchProjection_1 = Sketch_1.addProjection(model.selection("VERTEX", "Origin"), False)
#SketchPoint_1 = SketchProjection_1.createdFeature()
#SketchConstraintCoincidence_13 = Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchAPI_Point(SketchPoint_1).coordinates())

model.do()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Face_1 = model.addFace(Part_1_doc, [model.selection("FACE", "PartSet/Sketch_1/Face-SketchLine_12r-SketchLine_11r-SketchLine_10r-SketchLine_9r-SketchLine_8r-SketchLine_7r-SketchLine_6r-SketchLine_5r-SketchLine_4r-SketchLine_3r-SketchLine_2r-SketchLine_1r")])
Extrusion_1 = model.addExtrusion(Part_1_doc, [model.selection("FACE", "PartSet/Sketch_1/Face-SketchLine_12r-SketchLine_11r-SketchLine_10r-SketchLine_9r-SketchLine_8r-SketchLine_7r-SketchLine_6r-SketchLine_5r-SketchLine_4r-SketchLine_3r-SketchLine_2r-SketchLine_1r")], model.selection(), F, 0)
Fillet_1 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_7][Extrusion_1_1/To_Face]")], R1)
Fillet_2 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_1_1/MF:Fillet&Extrusion_1_1/To_Face][Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_5]")], R1)
Fillet_3 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_1_1/MF:Fillet&PartSet/Sketch_1/SketchLine_7][Extrusion_1_1/From_Face]")], R1)
Fillet_4 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_3_1/MF:Fillet&Extrusion_1_1/From_Face][Fillet_2_1/MF:Fillet&PartSet/Sketch_1/SketchLine_5]")], R1)
Fillet_5 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_4_1/MF:Fillet&Extrusion_1_1/From_Face][Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_9]")], R1)
Fillet_6 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_5_1/MF:Fillet&PartSet/Sketch_1/SketchLine_9][Fillet_2_1/MF:Fillet&Extrusion_1_1/To_Face]")], R1)
Fillet_7 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_5_1/MF:Fillet&Extrusion_1_1/From_Face][Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_3]")], R1)
Fillet_8 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_7_1/MF:Fillet&PartSet/Sketch_1/SketchLine_3][Fillet_6_1/MF:Fillet&Extrusion_1_1/To_Face]")], R1)
Fillet_9 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_7_1/MF:Fillet&Extrusion_1_1/From_Face][Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_1]")], R1)
Fillet_10 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_9_1/MF:Fillet&PartSet/Sketch_1/SketchLine_1][Fillet_8_1/MF:Fillet&Extrusion_1_1/To_Face]")], R1)
Fillet_11 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_9_1/MF:Fillet&Extrusion_1_1/From_Face][Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_11]")], R1)
Fillet_12 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_11_1/MF:Fillet&PartSet/Sketch_1/SketchLine_11][Fillet_10_1/MF:Fillet&Extrusion_1_1/To_Face]")], R1)

#Exportez le fichier ".XAO" dans le dossier ./temp
Export_1 = model.exportToXAO(Part_1_doc, adresse_temp+'\\shaper_rikgiz79.xao', model.selection("SOLID", "Fillet_12_1"), 'XAO')

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
(imported, Fillet_12_1, [], [], []) = geompy.ImportXAO(adresse_temp+"/shaper_rikgiz79.xao")
#Exporter le fichier ".STL" vers le dossier ./WORK
geompy.ExportSTL(Fillet_12_1, adresse+"/%s.stl"%(NOM), True, 0.001, True)
#Ajouter à "Geometry"
geompy.addToStudy( Fillet_12_1, NOM )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
