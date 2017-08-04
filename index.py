import pygame
import math
import sys
import importlib
from collections import OrderedDict
from tools.definitions import *
from tools.classes import *

pygame.init()

displayWidth = 1000
displayHeight = 600
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))

clock = pygame.time.Clock()

buttonDict      = OrderedDict()
vertexDict      = OrderedDict()
allObjectsDict  = OrderedDict()

levelFileName = "levels.level2"
levelFile = importlib.import_module(levelFileName)

grid = Grid(Color("black", 255), 450, 100, 40, 10, 3, gameDisplay)
allObjectsDict["grid"] = {"name":"grid", "species":None, "subspecies":None, "vertexNum":None, "object":grid}

checkButton = Button(Color("green", 255), Color("red", 255), Color("black", 255), "Check!", 900, 100, 90, 80, gameDisplay)
buttonDict["checkButton"] = {"name":"checkButton","object":checkButton}
allObjectsDict["checkButton"] = {"name":"checkButton", "species":None, "subspecies":None, "vertexNum":None, "object":checkButton}

clearButton = Button(Color("yellow", 255), Color("red", 255), Color("black", 255), "Clear!", 900, 200, 90, 80, gameDisplay)
buttonDict["clearButton"] = {"name":"clearButton","object":clearButton}
allObjectsDict["clearButton"] = {"name":"clearButton", "species":None, "subspecies":None, "vertexNum":None, "object":clearButton}

MakeAndDrawInputsAndOutputs(levelFile.inputsDict, levelFile.outputsDict, allObjectsDict, grid, gameDisplay)
MakeAndDrawObjects(levelFile.levelInteractionsDict, levelFile.levelParticlesDict, vertexDict, allObjectsDict, 10, 10, grid, gameDisplay)

winOrLose = levelFile.winOrLose

done = False

while not done:

   gameDisplay.fill(Color("white",255))
   for object in allObjectsDict:
      allObjectsDict[object]["object"].update()
      allObjectsDict[object]["object"].draw()

   diagramsLeft = 0
   for i in range(len(winOrLose)):
      if winOrLose[i] == False: diagramsLeft+=1

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         done = True
      if event.type == pygame.MOUSEBUTTONDOWN:
         clicked = []
         for v in vertexDict:
            if vertexDict[v]["object"].rect.collidepoint(event.pos) :
               vertexDict[v]["object"].click = True
               clicked.append(vertexDict[v]["object"])
         for b in buttonDict:
            if buttonDict[b]["object"].rect.collidepoint(event.pos) :
               buttonDict[b]["object"].click = True
               clicked.append(buttonDict[b]["object"])
         for check in clicked[1:]:
            check.click = False

         if buttonDict["checkButton"]["object"].click:
            winCondition = Check(allObjectsDict, grid, levelFileName)           
            if winCondition != None:
               winOrLose[winCondition] = True

         if buttonDict["clearButton"]["object"].click:
            for v in vertexDict:
               if not vertexDict[v]["object"].click:
                  vertexDict[v]["object"].rect.x = vertexDict[v]["object"].xStart
                  vertexDict[v]["object"].rect.y = vertexDict[v]["object"].yStart

      if event.type == pygame.MOUSEBUTTONUP:
         for v in vertexDict:
            vertexDict[v]["object"].click = False
         for b in buttonDict:
            buttonDict[b]["object"].click = False

   myfont = pygame.font.SysFont("Bold", 50)
   text = myfont.render("{} Feynman diagrams left!".format(diagramsLeft), 1, Color("black",255))
   gameDisplay.blit(text, (430, 25))

   pygame.display.update()
   #clock.tick(20)
   

