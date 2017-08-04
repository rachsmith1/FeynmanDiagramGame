import pygame
import math
import importlib
from collections import OrderedDict
from tools.classes import *

def Color(name, transparency):
   a = 0; b = 0; c = 0; d = transparency
   if name=="black":  a = 0; b = 0; c = 0
   if name=="white":  a = 255; b = 255; c = 255
   if name=="green":  a = 0; b = 255; c = 0
   if name=="blue" :  a = 0; b = 0; c = 255
   if name=="red"  :  a = 255; b = 0; c = 0
   if name=="yellow": a = 255; b = 255; c = 0
   if name=="purple": a = 102; b = 51; c = 153
   return (a, b, c, d)

def MakeParticle(name, x, y, species, subspecies, vertexDict, allObjectsDict, grid, display):

   if species=="gluon":

      thickness = 3
      dashNum = 20
      lineType = "loops"
      
      colorVertex1 = Color("black",100)
      colorVertex2 = Color("black",100)
      colorLine = Color("black",100)
      
   if species=="fermion":
      
      thickness = 5
      dashNum = 1
      lineType = "arrow"
      
      if "Quark" in subspecies:
         colorVertex1 = Color("red",100)
         colorVertex2 = Color("red",100)
         colorLine = Color("red",100)
      if ("Electron" in subspecies) or ("Muon" in subspecies) or ("Tau" in subspecies):
         colorVertex1 = Color("blue",100)
         colorVertex2 = Color("blue",100)
         colorLine = Color("blue",100)

   if species=="boson":

      thickness = 5
           
      if "Higgs" in subspecies:
         dashNum = 20
         lineType = "dashed"
         colorVertex1 = Color("green",100)
         colorVertex2 = Color("green",100)
         colorLine = Color("green",100)

      if "Photon" in subspecies:
         dashNum = 4
         lineType = "squiggle"
         colorVertex1 = Color("yellow",100)
         colorVertex2 = Color("yellow",100)
         colorLine = Color("yellow",100)

      if "Z" in subspecies:
         dashNum = 4
         lineType = "squiggle"
         colorVertex1 = Color("purple",100)
         colorVertex2 = Color("purple",100)
         colorLine = Color("purple",100)

   particleVertex1 = Vertex(colorVertex1, subspecies, 1, x, y, 30, 30, grid, display)
   vertexDict[name+"_v1"]     = {"name":name, "species":species, "subspecies":subspecies, "vertexNum":1, "object":particleVertex1}
   allObjectsDict[name+"_v1"] = {"name":name, "species":species, "subspecies":subspecies, "vertexNum":1, "object":particleVertex1}

   particleVertex2 = Vertex(colorVertex2, subspecies, 2, x+100, y, 30, 30, grid, display)
   vertexDict[name+"_v2"]     = {"name":name, "species":species, "subspecies":subspecies, "vertexNum":2, "object":particleVertex2}
   allObjectsDict[name+"_v2"] = {"name":name, "species":species, "subspecies":subspecies, "vertexNum":2, "object":particleVertex2}

   line = Line(colorLine, thickness, dashNum, particleVertex1, particleVertex2, display, lineType)
   allObjectsDict[name+"_line"] = {"name":name, "species":None, "subspecies":None, "vertexNum":None, "object":line}

def MakeInteraction(name, x, y, species, subspecies, vertexDict, allObjectsDict, grid, display):
   if subspecies=="QCD":
      colorVertex = Color("yellow",100)
   if subspecies=="QED":
      colorVertex = Color("green",100)

   interactionVertex = Vertex(colorVertex, subspecies, None, x, y, 50, 50, grid, display)
   vertexDict[name]     = {"name":name, "species":species, "subspecies":subspecies, "vertexNum":None, "object":interactionVertex}
   allObjectsDict[name] = {"name":name, "species":species, "subspecies":subspecies, "vertexNum":None, "object":interactionVertex}

def MakeAndDrawInputsAndOutputs(inputsDict, outputsDict, allObjectsDict, grid, display):
   step = math.floor(grid.numSteps/len(inputsDict))
   index = 0
   for i in inputsDict:
      x = grid.rect.x - grid.stepSize
      y = grid.rect.y + index*step*grid.stepSize

      inputVertex = Vertex(Color("black",100), inputsDict[i]["subspecies"], None, x, y, 50, 50, grid, display)
      allObjectsDict[inputsDict[i]["name"]] = {"name":inputsDict[i]["name"], 
                                               "species":inputsDict[i]["species"],
                                               "subspecies":inputsDict[i]["subspecies"],
                                               "vertexNum":None,
                                               "object":inputVertex}
      index+=1

   step = math.floor(grid.numSteps/len(outputsDict))
   index = 0
   for j in outputsDict:
      x = grid.rect.x - 2*grid.stepSize + grid.numSteps*grid.stepSize
      y = grid.rect.y + index*step*grid.stepSize

      outputVertex = Vertex(Color("black",100), outputsDict[j]["subspecies"], None, x, y, 50, 50, grid, display)
      allObjectsDict[outputsDict[j]["name"]] = {"name":outputsDict[j]["name"],
                                                "species":outputsDict[j]["species"],
                                                "subspecies":outputsDict[j]["subspecies"],
                                                "vertexNum":None,
                                                "object":outputVertex}
      index+=1
      

def MakeAndDrawObjects(interactionsDict, particlesDict, vertexDict, allObjectsDict, xStart, yStart, grid, display):
   x=xStart; y=yStart
   for interaction in interactionsDict:
      if abs(y - pygame.display.get_surface().get_height()) < 100:
         x+=150
         y=yStart 
      MakeInteraction(interactionsDict[interaction]["name"], x, y,
                      interactionsDict[interaction]["species"],
                      interactionsDict[interaction]["subspecies"],
                      vertexDict, allObjectsDict, grid, display)
      y+=80

   y+=10
   for particle in particlesDict:
      if abs(y - pygame.display.get_surface().get_height()) < 100:
         x+=150
         y=yStart 
      MakeParticle(particlesDict[particle]["name"], x, y,
                   particlesDict[particle]["species"], 
                   particlesDict[particle]["subspecies"], 
                   vertexDict, allObjectsDict, grid, display)
      y+=70

def Check(allObjectsDict, grid, level):
   particleDict = OrderedDict()
   interactionDict = OrderedDict()

   for object in allObjectsDict:
      if allObjectsDict[object]["species"]=="interaction": 
         interactionDict[allObjectsDict[object]["name"]] = allObjectsDict[object]
      if (
            "grid" not in allObjectsDict[object]["name"] and
            "Button" not in allObjectsDict[object]["name"] and
            allObjectsDict[object]["vertexNum"]!=None
         ):
            particleDict[allObjectsDict[object]["name"] + "_v" + str(allObjectsDict[object]["vertexNum"])] = allObjectsDict[object]

   checkedInteractionDict = OrderedDict()
   interactionList = []

   for corner in grid.corners:
      for interaction in interactionDict:
         interactionPosition = interactionDict[interaction]["object"].rect.center
         if interactionPosition == corner:
            newInteraction = Interaction(interactionDict[interaction]["name"], interactionDict[interaction], particleDict)
            interactionList.append(newInteraction)
            checkedInteractionDict[newInteraction.name] = {"name":newInteraction.name, "object":newInteraction}

   for checkedInteraction in checkedInteractionDict: 
      checkedInteractionDict[checkedInteraction]["object"].getConnections(interactionList)

   levelFile = importlib.import_module(level)
   winCondition = levelFile.CheckIfWinningCondition(checkedInteractionDict)

   return winCondition
      
