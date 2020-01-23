#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.4.0 with dump python functionality
###

import sys
import salome
import os
import tempfile

salome.salome_init()

import salome_notebook

try:
    os.makedirs("WORK")
except OSError:
    pass

notebook = salome_notebook.NoteBook()
adresse = os.getcwd()+'/WORK'
sys.path.insert(0, r'%s'%(adresse))

adresse_temp = tempfile.gettempdir()

###
### SHAPER component
###

from SketchAPI import *

from salome.shaper import model
Xi = 0 #position iniciale X et Z
Zi = 0
A = 43 #Largeur de piece(Largura peça)
B = 21 #Hauteur de la piece(Altura peça)
C = 6.75 #Largeur de la partie haut(Largura da parte)
D = 14.8 #Hauteur interne(Altura da parte)
E = 8.65 #Largeur de la partie inférieure(Largura da parte fundo)
F = 15.2 #profondeur de la piece(Profundidade peça)

R1 = 0.6#Rayon de conge interieur(Raio filete interno)
R2 = 2#Rayon de conge exterieur(Raio filete externo)

NOM = "E%.1f_%.1f_%.1f"%(A,B,F)

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
SketchConstraintHorizontal_2 = Sketch_1.setHorizontal(SketchLine_4.result())
SketchLine_5 = Sketch_1.addLine(Xi+C+E, Zi+B-D, Xi+C+E, Zi+B)
SketchConstraintCoincidence_4 = Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_5.startPoint())
SketchConstraintVertical_3 = Sketch_1.setVertical(SketchLine_5.result())
SketchLine_6 = Sketch_1.addLine(Xi+C+E, Zi+B, Xi+C+E+(A-2*C-2*E), Zi+B)
SketchConstraintCoincidence_5 = Sketch_1.setCoincident(SketchLine_5.endPoint(), SketchLine_6.startPoint())
SketchConstraintHorizontal_3 = Sketch_1.setHorizontal(SketchLine_6.result())
SketchLine_7 = Sketch_1.addLine(Xi+C+E+(A-2*C-2*E), Zi+B, Xi+C+E+(A-2*C-2*E), Zi+B-D)
SketchConstraintCoincidence_6 = Sketch_1.setCoincident(SketchLine_6.endPoint(), SketchLine_7.startPoint())
SketchLine_8 = Sketch_1.addLine(Xi+C+E+(A-2*C-2*E), Zi+B-D, Xi+C+E+(A-2*C-2*E)+E, Zi+B-D)
SketchConstraintCoincidence_7 = Sketch_1.setCoincident(SketchLine_7.endPoint(), SketchLine_8.startPoint())
SketchConstraintHorizontal_4 = Sketch_1.setHorizontal(SketchLine_8.result())
SketchLine_9 = Sketch_1.addLine(Xi+C+E+(A-2*C-2*E)+E, Zi+B-D, Xi+C+E+(A-2*C-2*E)+E, Zi+B)
SketchConstraintCoincidence_8 = Sketch_1.setCoincident(SketchLine_8.endPoint(), SketchLine_9.startPoint())
SketchConstraintVertical_4 = Sketch_1.setVertical(SketchLine_9.result())
SketchLine_10 = Sketch_1.addLine(Xi+C+E+(A-2*C-2*E)+E, Zi+B, Xi+A, Zi+B)
SketchConstraintCoincidence_9 = Sketch_1.setCoincident(SketchLine_9.endPoint(), SketchLine_10.startPoint())
SketchConstraintHorizontal_5 = Sketch_1.setHorizontal(SketchLine_10.result())
SketchLine_11 = Sketch_1.addLine(Xi+A, Zi+B, Xi+A, Zi)
SketchConstraintCoincidence_10 = Sketch_1.setCoincident(SketchLine_10.endPoint(), SketchLine_11.startPoint())
SketchLine_12 = Sketch_1.addLine(Xi+A, Zi, Xi, Zi)
SketchConstraintCoincidence_11 = Sketch_1.setCoincident(SketchLine_11.endPoint(), SketchLine_12.startPoint())
SketchConstraintCoincidence_12 = Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchLine_12.endPoint())
SketchConstraintHorizontal_6 = Sketch_1.setHorizontal(SketchLine_12.result())
SketchConstraintVertical_5 = Sketch_1.setVertical(SketchLine_7.result())
SketchConstraintVertical_6 = Sketch_1.setVertical(SketchLine_11.result())
SketchConstraintDistanceHorizontal_1 = Sketch_1.setHorizontalDistance(SketchLine_1.startPoint(), SketchLine_12.startPoint(), A)
SketchConstraintDistanceVertical_1 = Sketch_1.setVerticalDistance(SketchLine_1.endPoint(), SketchLine_1.startPoint(), B)
SketchConstraintEqual_1 = Sketch_1.setEqual(SketchLine_1.result(), SketchLine_11.result())
SketchConstraintEqual_2 = Sketch_1.setEqual(SketchLine_3.result(), SketchLine_5.result())
SketchConstraintEqual_3 = Sketch_1.setEqual(SketchLine_5.result(), SketchLine_7.result())
SketchConstraintDistanceHorizontal_2 = Sketch_1.setHorizontalDistance(SketchLine_1.endPoint(), SketchLine_3.startPoint(), C)
SketchConstraintEqual_4 = Sketch_1.setEqual(SketchLine_2.result(), SketchLine_10.result())
SketchConstraintEqual_5 = Sketch_1.setEqual(SketchLine_4.result(), SketchLine_8.result())
SketchConstraintDistanceVertical_2 = Sketch_1.setVerticalDistance(SketchLine_3.startPoint(), SketchLine_3.endPoint(), D)
SketchConstraintDistanceHorizontal_3 = Sketch_1.setHorizontalDistance(SketchLine_5.endPoint(), SketchLine_6.endPoint(), A-2*C-2*E)
SketchProjection_1 = Sketch_1.addProjection(model.selection("VERTEX", "Origin"), False)
SketchPoint_1 = SketchProjection_1.createdFeature()
SketchConstraintCoincidence_13 = Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchAPI_Point(SketchPoint_1).coordinates())
model.do()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Face_1 = model.addFace(Part_1_doc, [model.selection("FACE", "PartSet/Sketch_1/Face-SketchLine_12r-SketchLine_11r-SketchLine_10r-SketchLine_9r-SketchLine_8r-SketchLine_7r-SketchLine_6r-SketchLine_5r-SketchLine_4r-SketchLine_3r-SketchLine_2r-SketchLine_1r")])
Extrusion_1 = model.addExtrusion(Part_1_doc, [model.selection("FACE", "PartSet/Sketch_1/Face-SketchLine_12r-SketchLine_11r-SketchLine_10r-SketchLine_9r-SketchLine_8r-SketchLine_7r-SketchLine_6r-SketchLine_5r-SketchLine_4r-SketchLine_3r-SketchLine_2r-SketchLine_1r")], model.selection(), F, 0)
Fillet_1 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_12][Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_1]")], R2)
Fillet_2 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_1_1/MF:Fillet&PartSet/Sketch_1/SketchLine_12][Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_11]")], R2)
Fillet_3 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_9][Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_8]")], R1)
Fillet_4 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_3_1/MF:Fillet&PartSet/Sketch_1/SketchLine_8][Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_7]")], R1)
Fillet_5 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_5][Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_4]")], R1)
Fillet_6 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Fillet_5_1/MF:Fillet&PartSet/Sketch_1/SketchLine_4][Extrusion_1_1/Generated_Face&PartSet/Sketch_1/SketchLine_3]")], R1)


Export_1 = model.exportToXAO(Part_1_doc, adresse_temp+'/shaper_atmag7zk.xao', model.selection("SOLID", "Fillet_6_1"), 'XAO')

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
(imported, Fillet_6_1, [], [], []) = geompy.ImportXAO(adresse_temp+'/shaper_atmag7zk.xao')
geompy.ExportSTL(Fillet_6_1, adresse+"/%s.stl"%(NOM), True, 0.001, True)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Fillet_6_1, NOM )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
