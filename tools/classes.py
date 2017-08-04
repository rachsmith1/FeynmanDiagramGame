import pygame
import math
from collections import OrderedDict

class Button:
   def __init__(self, color, clickColor, textColor, caption, xBegin, yBegin, width, height, display):
      self.click = False
      self.image = pygame.Surface([width, height])
      self.image.fill(color)
      self.rect = self.image.get_rect()
      self.rect.x = xBegin
      self.rect.y = yBegin
      self.color = color
      self.textColor = textColor
      self.clickColor = clickColor
      self.caption = caption
      self.display = display

   def update(self):
      if self.click:
         self.image.fill(self.clickColor)
      else:
         self.image.fill(self.color)

   def draw(self):
      self.display.blit(self.image, (self.rect.x, self.rect.y))
      
      myfont = pygame.font.SysFont("Bold", 30)
      text = myfont.render(self.caption, 1, self.textColor)
      textRect = text.get_rect()
      textRect.center = (self.rect.centerx, self.rect.centery)
      self.display.blit(text, (textRect.x, textRect.y))

class Grid:
   def __init__(self, color, xBegin, yBegin, stepSize, numSteps, radius, display):
      self.image = pygame.Surface([stepSize*numSteps, stepSize*numSteps], pygame.SRCALPHA)
      self.rect = self.image.get_rect()
      self.rect.x = xBegin
      self.rect.y = yBegin
      self.numSteps = numSteps
      self.stepSize = stepSize
      self.color = color
      self.radius = radius
      self.display = display

      self.corners = []
      for x in range(numSteps):
         for y in range(numSteps):
            self.corners.append((xBegin + x*stepSize, yBegin + y*stepSize))

   def update(self):
         none = None

   def draw(self):
      for x,y in self.corners:
         circ = pygame.Rect(0,0,self.radius*2,self.radius*2)
         circ.center = (x,y)
         pygame.draw.circle(self.display, self.color, (circ.centerx, circ.centery), self.radius, 0)    

class Vertex:
   def __init__(self, color, name, vNum, xBegin, yBegin, width, height, grid, display):
      self.click = False
      self.xStart = xBegin
      self.yStart = yBegin
      self.image = pygame.Surface([width,height], pygame.SRCALPHA)
      self.image.fill(color)
      self.rect = self.image.get_rect()
      self.rect.x = xBegin
      self.rect.y = yBegin
      self.grid = grid
      self.display = display
      self.name = name
      self.vNum = vNum

   def update(self):
      if self.click:
         self.rect.center = pygame.mouse.get_pos()
      else:
         distToSnap = math.hypot(self.grid.stepSize/2, self.grid.stepSize/2)
         for cx, cy in self.grid.corners:
            if math.hypot(cx - self.rect.centerx, cy - self.rect.centery) < distToSnap:
               self.rect.center = (cx,cy)

   def draw(self):
      self.display.blit(self.image, (self.rect.x, self.rect.y))
      myfont = pygame.font.SysFont("Bold", 20)
      if self.vNum==None:
         #if ("QCD" in self.name) or ("QED" in self.name) or ("Input" in self.name) or ("Output" in self.name):
         label = myfont.render(self.name, 1, (255,0,0))
         self.display.blit(label, (self.rect.x + 10, self.rect.centery + 48))
      if self.vNum==1:
         label = myfont.render(self.name, 1, (0,0,255))
         self.display.blit(label, (self.rect.x, self.rect.centery + 28))

class Point:
    # constructed using a normal tupple
    def __init__(self, point_t = (0,0)):
        self.x = float(point_t[0])
        self.y = float(point_t[1])
    # define all useful operators
    def __add__(self, other):
        return Point((self.x + other.x, self.y + other.y))
    def __sub__(self, other):
        return Point((self.x - other.x, self.y - other.y))
    def __mul__(self, scalar):
        return Point((self.x*scalar, self.y*scalar))
    def __div__(self, scalar):
        return Point((self.x/scalar, self.y/scalar))
    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2))
    # get back values in original tuple format
    def get(self):
        return (self.x, self.y)

class Line:
   def __init__(self, color, thickness, dashNum, vertex1, vertex2, display, lineType):
      self.vertex1 = vertex1
      self.vertex2 = vertex2
      self.x1 = vertex1.rect.centerx
      self.y1 = vertex1.rect.centery
      self.x2 = vertex2.rect.centerx
      self.y2 = vertex2.rect.centery
      self.display = display
      self.color = color
      self.thickness = thickness
      self.dashNum = dashNum
      self.lineType = lineType

      self.image = pygame.Surface([abs(self.x1-self.x2),abs(self.y1-self.y2)], pygame.SRCALPHA)
      self.rect = self.image.get_rect()
      
   def update(self):
      self.x1 = self.vertex1.rect.centerx
      self.y1 = self.vertex1.rect.centery
      self.x2 = self.vertex2.rect.centerx
      self.y2 = self.vertex2.rect.centery

   def draw(self):
      origin = Point((self.x1, self.y1))
      target = Point((self.x2, self.y2))
      displacement = target - origin
      length = len(displacement)
      slope = Point((0,0)); dash_length = 0; dashVar = 0
      if length!=0:
         slope = displacement/length
         dash_length = length/self.dashNum
         if dash_length!=0:
            dashVar = length/dash_length

      if self.lineType=="loops":
         radius = 10
         for index in range(0, length/(radius*2)):
            cent = origin + slope * index * radius*2
            circ = pygame.Rect(0,0,radius*2,radius*2)
            circ.center = (cent.get())
            pygame.draw.circle(self.display, self.color, (circ.centerx, circ.centery), radius, self.thickness)  


      if self.lineType=="squiggle":
         antislope = Point((-slope.get()[1], slope.get()[0]))
         for index in range(0, dashVar):
            p1 = origin + slope * (index + 0) * dash_length 
            p2 = origin + slope * (index + 1/4.0) * dash_length 
            peak1 = p2 - antislope * 10
            p3 = origin + slope * (index + 2/4.0) * dash_length 
            p4 = origin + slope * (index + 3/4.0) * dash_length 
            peak2 = p4 + antislope * 10
            p5 = origin + slope * (index + 4/4.0) * dash_length

            pygame.draw.line(self.display, self.color, p1.get(), peak1.get(), self.thickness)
            pygame.draw.line(self.display, self.color, peak1.get(), p3.get(), self.thickness)
            pygame.draw.line(self.display, self.color, p3.get(), peak2.get(), self.thickness)
            pygame.draw.line(self.display, self.color, peak2.get(), p5.get(), self.thickness)
       

      if self.lineType=="arrow":
         midway = origin + slope*length*3/5
         arrowBase = midway - slope * 20
         antislope = Point((-slope.get()[1], slope.get()[0]))
         arrowV1 = arrowBase - antislope * 10
         arrowV2 = arrowBase + antislope * 10
         pygame.draw.line(self.display, self.color, midway.get(), arrowV1.get(), self.thickness)
         pygame.draw.line(self.display, self.color, midway.get(), arrowV2.get(), self.thickness)
         pygame.draw.line(self.display, self.color, origin.get(), target.get(), self.thickness)
         

      if self.lineType=="dashed":
         for index in range(0, dashVar, 2):
            start = origin + (slope *    index    * dash_length)
            end   = origin + (slope * (index + 1) * dash_length)
            pygame.draw.line(self.display, self.color, start.get(), end.get(), self.thickness)

class Interaction:
   def __init__(self, name, vertex, particleDict):
      self.name = name
      self.vertex = vertex
      self.particleList = OrderedDict()
      
      vertexPosition = vertex["object"].rect.center
      for particle in particleDict:
         particlePosition = particleDict[particle]["object"].rect.center
         if vertexPosition==particlePosition:
            name = particleDict[particle]["name"] + "_v" + str(particleDict[particle]["vertexNum"])
            self.particleList[name] = particleDict[particle]

      self.isInputOrOutput = False
      self.isQCD = False
      self.isQED = False
      self.typeQCD = None
      self.typeQED = None

      self.isConnected = False
      self.connectionV1 = None
      self.connectionV2 = None
      self.connection   = None

      if ("input" in vertex["name"]) or ("output" in vertex["name"]):
         if len(self.particleList)==1:
            self.isInputOrOutput = True

      if ("QCD" in vertex["name"]):
         gluons = OrderedDict()
         quarks = OrderedDict()
         for particle in self.particleList:
            name = self.particleList[particle]["name"] + "_v" + str(self.particleList[particle]["vertexNum"])
            if "Gluon" in self.particleList[particle]["subspecies"]: gluons[name] = self.particleList[particle]
            if "Quark" in self.particleList[particle]["subspecies"]: quarks[name] = self.particleList[particle]
            
         #QCD Type #1
         if len(gluons)==1 and len(quarks)==2:
            if (
                  quarks[quarks.keys()[0]]["name"]!=quarks[quarks.keys()[1]]["name"] and 
                  quarks[quarks.keys()[0]]["vertexNum"]!=quarks[quarks.keys()[1]]["vertexNum"] and
                  quarks[quarks.keys()[0]]["subspecies"]==quarks[quarks.keys()[1]]["subspecies"]
               ):
                  self.isQCD = True
                  self.typeQCD = 1
         
         #QCD Type #2
         if len(gluons)==3:
            gluonNames = []
            for gluon in gluons:
               gluonNames.append(gluons[gluon]["name"])
            if len(set(gluonNames)) == len(gluonNames):
               self.isQCD = True
               self.typeQCD = 2

         #QCD Type #3
         if len(gluons)==4:
            gluonNames = []
            for gluon in gluons:
               gluonNames.append(gluons[gluon]["name"])
            if len(set(gluonNames)) == len(gluonNames):
               self.isQCD = True
               self.typeQCD = 3

      if ("QED" in vertex["name"]):
         fermions = OrderedDict()
         bosons = OrderedDict()
         for particle in self.particleList:
            name = self.particleList[particle]["name"] + "_v" + str(self.particleList[particle]["vertexNum"])
            if "fermion" in self.particleList[particle]["species"]: fermions[name] = self.particleList[particle]
            if "boson"   in self.particleList[particle]["species"]: bosons[name] = self.particleList[particle]

         #QED Type #1
         if len(fermions)==2 and len(bosons)==1: 
            if (
                  fermions[fermions.keys()[0]]["name"]!=fermions[fermions.keys()[1]]["name"] and 
                  fermions[fermions.keys()[0]]["vertexNum"]!=fermions[fermions.keys()[1]]["vertexNum"] and
                  fermions[fermions.keys()[0]]["subspecies"]==fermions[fermions.keys()[1]]["subspecies"]
               ):
                  self.isQED = True
                  self.typeQED = 1



   def getConnections(self, interactionList):
      for potentialMate in interactionList:
         if self.name!=potentialMate.name:
            for ourParticle in self.particleList:
               for theirParticle in potentialMate.particleList:
                  if (
                        self.particleList[ourParticle]["name"]==potentialMate.particleList[theirParticle]["name"] and
                        self.particleList[ourParticle]["vertexNum"]!=potentialMate.particleList[theirParticle]["vertexNum"]
                     ):
                        self.isConnected = True
                        if len(self.particleList)==1:
                           self.connectionV1 = self.particleList[ourParticle]
                           self.connectionV2 = potentialMate.particleList[theirParticle]
                           self.connection = potentialMate

