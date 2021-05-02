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

A = 12.8#Largeur de la pièce(Largura da peça)
B = 2.85#Hauteur de la pièce(Altura da peça)
C = 8.7#profondeur de la pièce(profundidade da peça)

D = 9.05#la distance par rapport aux parties intérieures(distancia das partes internas)
E = 1.75#Hauteur intérieure des pièces(Altura interna das partes)

D1 = 5#Diamètre intérieur plus petit(Diametro interno menor)
D2 = 11.2#Diamètre intérieur plus grand(Diametro interno maior)

R1 = 0.4#à l'intérieur du rayon extérieur du filet(raio filete externo interior)
R2 = 0.5#rayon extérieur du filet(raio filete externo exterior)
R3 = 0.7#rayon du filet intérieur(raio filete interno interior)

NOM = "EQ%.1f_%.1f_%.1f"%(A,B,C)#Nom de fichier .STL

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
SketchCircle_1 = Sketch_2.addCircle(A/2, -B/2, D1/2)
SketchCircle_2 = Sketch_2.addCircle(A/2, -B/2, D2/2)
SketchConstraintCoincidence_6 = Sketch_2.setCoincident(SketchCircle_1.center(), SketchCircle_2.center())
SketchProjection_2 = Sketch_2.addProjection(model.selection("VERTEX", "[Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_1][Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_2][Extrusion_1_1/To_Face]"), False)
SketchPoint_2 = SketchProjection_2.createdFeature()
SketchConstraintDistanceVertical_1 = Sketch_2.setVerticalDistance(SketchCircle_1.center(), SketchAPI_Point(SketchPoint_2).coordinates(), C/2)
SketchConstraintDistanceHorizontal_1 = Sketch_2.setHorizontalDistance(SketchCircle_2.center(), SketchAPI_Point(SketchPoint_2).coordinates(), A/2)
SketchConstraintRadius_1 = Sketch_2.setRadius(SketchCircle_1.results()[1], D1/2)
SketchConstraintRadius_2 = Sketch_2.setRadius(SketchCircle_2.results()[1], D2/2)

model.do()
Face_2 = model.addFace(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchCircle_2_2f-SketchCircle_1_2r")])
ExtrusionCut_1 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Face_2_1")], model.selection(), 0, E, [model.selection("SOLID", "Extrusion_1_1")])
Sketch_3 = model.addSketch(Part_1_doc, model.selection("FACE", "ExtrusionCut_1_1/Modified_Face&Extrusion_1_1/To_Face"))
SketchLine_5 = Sketch_3.addLine((A-D)/2+(D-D1)/2, B, (A-D)/2, B)
SketchProjection_3 = Sketch_3.addProjection(model.selection("EDGE", "[ExtrusionCut_1_1/Modified_Face&Extrusion_1_1/To_Face][(ExtrusionCut_1_1/Modified_Face&Extrusion_1_1/From_Face)(ExtrusionCut_1_1/Modified_Face&Extrusion_1_1/To_Face)(Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_2)(Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_4)2(Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_3)2(ExtrusionCut_1_1/Modified_Face&ExtrusionCut_1_1/From_Face)2]"), False)
SketchLine_6 = SketchProjection_3.createdFeature()
SketchConstraintCoincidence_7 = Sketch_3.setCoincident(SketchLine_5.endPoint(), SketchLine_6.result())
SketchLine_7 = Sketch_3.addLine((A-D)/2, B, (A-D)/2, B-E)
SketchLine_8 = Sketch_3.addLine((A-D)/2, B-E, (A-D)/2+(D-D1)/2, B-E)
SketchLine_9 = Sketch_3.addLine((A-D)/2+(D-D1)/2, B-E, (A-D)/2+(D-D1)/2, B)
SketchConstraintCoincidence_8 = Sketch_3.setCoincident(SketchLine_9.endPoint(), SketchLine_5.startPoint())
SketchConstraintCoincidence_9 = Sketch_3.setCoincident(SketchLine_5.endPoint(), SketchLine_7.startPoint())
SketchConstraintCoincidence_10 = Sketch_3.setCoincident(SketchLine_7.endPoint(), SketchLine_8.startPoint())
SketchConstraintCoincidence_11 = Sketch_3.setCoincident(SketchLine_8.endPoint(), SketchLine_9.startPoint())
SketchConstraintHorizontal_3 = Sketch_3.setHorizontal(SketchLine_5.result())
SketchConstraintVertical_3 = Sketch_3.setVertical(SketchLine_7.result())
SketchConstraintHorizontal_4 = Sketch_3.setHorizontal(SketchLine_8.result())
SketchConstraintVertical_4 = Sketch_3.setVertical(SketchLine_9.result())
SketchProjection_4 = Sketch_3.addProjection(model.selection("EDGE", "([ExtrusionCut_1_1/Modified_Face&Extrusion_1_1/To_Face][Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_4])3([ExtrusionCut_1_1/Modified_Face&Extrusion_1_1/To_Face][Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_2])3"), False)
SketchLine_10 = SketchProjection_4.createdFeature()
SketchConstraintCoincidence_12 = Sketch_3.setCoincident(SketchLine_8.endPoint(), SketchLine_10.result())
Aux = D1 + (D-D1)/2 
SketchLine_11 = Sketch_3.addLine(Aux+(A-D)/2, B, Aux+(A-D)/2+(D-D1)/2, B)
SketchProjection_5 = Sketch_3.addProjection(model.selection("EDGE", "[(ExtrusionCut_1_1/Modified_Face&Extrusion_1_1/From_Face)(ExtrusionCut_1_1/Modified_Face&Extrusion_1_1/To_Face)(Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_4)(Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_3)2(Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_2)2(ExtrusionCut_1_1/Modified_Face&ExtrusionCut_1_1/From_Face)2][ExtrusionCut_1_1/Modified_Face&Extrusion_1_1/To_Face]"), False)
SketchLine_12 = SketchProjection_5.createdFeature()
SketchConstraintCoincidence_13 = Sketch_3.setCoincident(SketchLine_11.endPoint(), SketchLine_12.result())
SketchLine_13 = Sketch_3.addLine(Aux+(A-D)/2+(D-D1)/2, B, Aux+(A-D)/2+(D-D1)/2, B-E)
SketchLine_14 = Sketch_3.addLine(Aux+(A-D)/2+(D-D1)/2, B-E, Aux+(A-D)/2, B-E)
SketchLine_15 = Sketch_3.addLine(Aux+(A-D)/2, B-E, Aux+(A-D)/2, B)
SketchConstraintCoincidence_14 = Sketch_3.setCoincident(SketchLine_15.endPoint(), SketchLine_11.startPoint())
SketchConstraintCoincidence_15 = Sketch_3.setCoincident(SketchLine_11.endPoint(), SketchLine_13.startPoint())
SketchConstraintCoincidence_16 = Sketch_3.setCoincident(SketchLine_13.endPoint(), SketchLine_14.startPoint())
SketchConstraintCoincidence_17 = Sketch_3.setCoincident(SketchLine_14.endPoint(), SketchLine_15.startPoint())
SketchConstraintHorizontal_5 = Sketch_3.setHorizontal(SketchLine_11.result())
SketchConstraintVertical_5 = Sketch_3.setVertical(SketchLine_13.result())
SketchConstraintHorizontal_6 = Sketch_3.setHorizontal(SketchLine_14.result())
SketchConstraintVertical_6 = Sketch_3.setVertical(SketchLine_15.result())
SketchConstraintCoincidence_18 = Sketch_3.setCoincident(SketchLine_14.endPoint(), SketchLine_10.result())
SketchConstraintEqual_1 = Sketch_3.setEqual(SketchLine_5.result(), SketchLine_11.result())
SketchConstraintLength_3 = Sketch_3.setLength(SketchLine_5.result(), (D-D1)/2)
SketchProjection_6 = Sketch_3.addProjection(model.selection("VERTEX", "[ExtrusionCut_1_1/Modified_Face&Extrusion_1_1/To_Face][Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_3][Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_2]"), False)
SketchPoint_3 = SketchProjection_6.createdFeature()
SketchConstraintDistanceHorizontal_2 = Sketch_3.setHorizontalDistance(SketchAPI_Point(SketchPoint_3).coordinates(), SketchLine_7.endPoint(), (A-D)/2)
SketchProjection_7 = Sketch_3.addProjection(model.selection("VERTEX", "[ExtrusionCut_1_1/Modified_Face&Extrusion_1_1/To_Face][Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_4][Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_3]"), False)
SketchPoint_4 = SketchProjection_7.createdFeature()
SketchConstraintDistanceHorizontal_3 = Sketch_3.setHorizontalDistance(SketchLine_14.startPoint(), SketchAPI_Point(SketchPoint_4).coordinates(), (A-D)/2)

model.do()
Face_3 = model.addFace(Part_1_doc, [model.selection("FACE", "Sketch_2/Face-SketchLine_1r-SketchLine_3f-SketchLine_4f-SketchLine_5f")])
Face_4 = model.addFace(Part_1_doc, [model.selection("FACE", "Sketch_2/Face-SketchLine_11r-SketchLine_10r-SketchLine_9r-SketchLine_7r")])
ExtrusionCut_2 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Face_3_1")], model.selection(), 0, C, [model.selection("SOLID", "ExtrusionCut_1_1")])
ExtrusionCut_3 = model.addExtrusionCut(Part_1_doc, [model.selection("FACE", "Sketch_2/Face-SketchLine_11r-SketchLine_10r-SketchLine_9r-SketchLine_7r")], model.selection(), 0, C, [model.selection("SOLID", "ExtrusionCut_2_1")])
Fillet_1 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[(ExtrusionCut_3_1/Modified_Face&PartSet/Sketch_1/SketchLine_1)(ExtrusionCut_3_1/Modified_Face&Extrusion_1_1/To_Face)(ExtrusionCut_3_1/Modified_Face&Extrusion_1_1/From_Face)2(Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_4)2(Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_2)2(Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_3)2][ExtrusionCut_3_1/Modified_Face&Extrusion_1_1/To_Face]")], R1)
Fillet_2 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_1_1/MF:Fillet&Sketch_2/SketchLine_9][(Fillet_1_1/MF:Fillet&PartSet/Sketch_1/SketchLine_1)(Fillet_1_1/MF:Fillet&Sketch_2/SketchLine_9)(Fillet_1_1/GF:Fillet&Fillet_1_1/FilletSelected)2(Fillet_1_1/MF:Fillet&Extrusion_1_1/To_Face)2(Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_4)2(ExtrusionCut_3_1/Modified_Face&Extrusion_1_1/From_Face)2(Fillet_1_1/MF:Fillet&Sketch_2/SketchLine_10)2]")], R3)
Fillet_3 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[(Fillet_2_1/MF:Fillet&PartSet/Sketch_1/SketchLine_1)(Fillet_2_1/MF:Fillet&Sketch_1/SketchCircle_2_2)(Fillet_2_1/MF:Fillet&ExtrusionCut_1_1/From_Face)(Fillet_2_1/MF:Fillet&Sketch_2/SketchLine_9)2(Fillet_2_1/GF:Fillet&Fillet_2_1/FilletSelected)2(Fillet_1_1/GF:Fillet&Fillet_1_1/FilletSelected)2(Fillet_1_1/MF:Fillet&Extrusion_1_1/To_Face)2(Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_4)2(ExtrusionCut_3_1/Modified_Face&Extrusion_1_1/From_Face)2(Fillet_2_1/MF:Fillet&Sketch_2/SketchLine_10)2][(Fillet_2_1/MF:Fillet&PartSet/Sketch_1/SketchLine_1)(ExtrusionCut_3_1/Modified_Face&Extrusion_1_1/From_Face)(Fillet_2_1/MF:Fillet&Sketch_2/SketchLine_9)2(Fillet_2_1/GF:Fillet&Fillet_2_1/FilletSelected)2(Fillet_1_1/GF:Fillet&Fillet_1_1/FilletSelected)2(Fillet_2_1/MF:Fillet&Sketch_1/SketchCircle_2_2)2(Fillet_1_1/MF:Fillet&Extrusion_1_1/To_Face)2(Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_4)2(Fillet_2_1/MF:Fillet&ExtrusionCut_1_1/From_Face)2(Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_3)2(Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_2)2]")], R3)
Fillet_4 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[(ExtrusionCut_3_1/Modified_Face&Extrusion_1_1/From_Face)(ExtrusionCut_2_1/Modified_Face&Sketch_1/SketchCircle_2_2)(Fillet_3_1/MF:Fillet&PartSet/Sketch_1/SketchLine_1)2(Fillet_3_1/MF:Fillet&Sketch_2/SketchLine_9)2(Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_4)2(Fillet_1_1/MF:Fillet&Extrusion_1_1/To_Face)2(Fillet_3_1/MF:Fillet&Sketch_2/SketchLine_10)2(Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_2)2(Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_3)2][ExtrusionCut_2_1/Modified_Face&Sketch_1/SketchCircle_2_2]")], R3)
Fillet_5 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_4_1/MF:Fillet&Sketch_1/SketchCircle_2_2][(Fillet_4_1/MF:Fillet&PartSet/Sketch_1/SketchLine_1)(Fillet_4_1/MF:Fillet&Sketch_1/SketchCircle_2_2)(Fillet_1_1/MF:Fillet&Extrusion_1_1/To_Face)]")], R3)
Fillet_6 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_5_1/MF:Fillet&Sketch_2/SketchLine_3][Fillet_1_1/MF:Fillet&Extrusion_1_1/To_Face]")], R1)
Fillet_7 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[ExtrusionCut_3_1/Modified_Face&Extrusion_1_1/From_Face][Fillet_4_1/MF:Fillet&Sketch_2/SketchLine_3]")], R1)
Fillet_8 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_7_1/MF:Fillet&Extrusion_1_1/From_Face][Fillet_3_1/MF:Fillet&Sketch_2/SketchLine_9]")], R1)
Fillet_9 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_4][Fillet_6_1/MF:Fillet&Extrusion_1_1/To_Face]")], R2)
Fillet_10 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_9_1/MF:Fillet&PartSet/Sketch_1/SketchLine_4][Fillet_8_1/MF:Fillet&Extrusion_1_1/From_Face]")], R2)
Fillet_11 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_9_1/MF:Fillet&Extrusion_1_1/To_Face][Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_2]")], R2)
Fillet_12 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_11_1/MF:Fillet&PartSet/Sketch_1/SketchLine_2][Fillet_10_1/MF:Fillet&Extrusion_1_1/From_Face]")], R2)

#Exportez le fichier ".XAO" dans le dossier ./temp
Export_1 = model.exportToXAO(Part_1_doc, adresse_temp+'\\shaper_pbc8yjek.xao', model.selection("SOLID", "Fillet_12_1"), 'XAO')

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
(imported, Fillet_12_1, [], [], []) = geompy.ImportXAO(adresse_temp+"/shaper_pbc8yjek.xao")
#Exporter le fichier ".STL" vers le dossier ./WORK
geompy.ExportSTL(Fillet_12_1, adresse+"/%s.stl"%(NOM), True, 0.001, True)
#Ajouter à "Geometry"
geompy.addToStudy( Fillet_12_1, NOM )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
