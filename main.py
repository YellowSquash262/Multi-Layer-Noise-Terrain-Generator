import random

rows = 300
screensize = 1000
intensity = 2000

changeV = 1
smoothingV = 4

changeV2 = 1
smoothingV2 = 50

b = 0
noise1 = []
noise2 = []
noiseEnd = []

for a in range(rows):
    nested = []
    for b in range(rows): 
      nested.append(0)
    noiseEnd.append(nested[:])

def noise(change, smoothing):
  list = []
  for a in range(rows):
    nested = []
    for b in range(rows): 
      nested.append(0)
    list.append(nested[:])
  
  for x in range(rows):
      for y in range(rows):
        list[x][y]=random.randint(-intensity, intensity)
  
  def smooth(it):
    for x in range(it):
      for x in range(rows):
          for y in range(rows):
              if x == 0:
                  if y == 0:
                      b = round((list[x][y+1]+list[x+1][y]+list[x+1][y+1])/3)
                  elif y == rows-1:
                      b = round((list[x][y-1]+list[x+1][y]+list[x+1][y-1])/3)
                  else:
                      b = round((list[x][y-1]+list[x+1][y-1]+list[x+1][y]+list[x+1][y+1]+list[x][y+1])/5)
              elif y == 0:
                  if x == rows-1:
                      b = round((list[x-1][y]+list[x-1][y+1]+list[x][y+1])/3)
                  else:
                      b = round((list[x-1][y]+list[x-1][y+1]+list[x][y+1]+list[x+1][y+1]+list[x+1][y])/5)
              elif x == rows-1:
                  if y == rows-1:
                      b = round((list[x-1][y]+list[x-1][y-1]+list[x][y-11])/3)
                  else: 
                      b = round((list[x][y-1]+list[x-1][y-1]+list[x-1][y]+list[x-1][y+1]+list[x][y+1])/5)
              elif y == rows-1:
                  b = round((list[x-1][y]+list[x-1][y-1]+list[x][y-1]+list[x+1][y-1]+list[x+1][y])/5)
              else:
                  b = round((list[x-1][y]+list[x-1][y-1]+list[x][y-1]+list[x+1][y-1]+list[x+1][y]+list[x-1][y+1]+list[x][y+1]+list[x+1][y+1])/8)
              list[x][y] = random.randint(b-change,b+change)

  smooth(smoothing)
  return(list)

import pygame

noise1 = noise(changeV, smoothingV)
noise2 = noise(changeV2, smoothingV2)

for x in range(rows):
    for y in range(rows):
        noiseEnd[x][y]=noise1[x][y]*1+noise2[x][y]*10

maximum = 0
minimum = 0
total =0
ave = 0


red = 0
green = 0
blue = 0

# make pygame work
pygame.init()

# create screen
screen = pygame.display.set_mode((screensize, screensize))

#icon
icon1 = pygame.image.load('icon.png')
pygame.display.set_icon(icon1)

# title
pygame.display.set_caption("sound")

for x3 in range(rows):
      for y3 in range(rows):
        if noiseEnd[x3][y3] < minimum:
          minimum = noiseEnd[x3][y3]
        if noiseEnd[x3][y3] > maximum:
          maximum = noiseEnd[x3][y3]
total = maximum + minimum*-1
print("min: "+str(minimum)+", max: "+str(maximum))
print(total)

running = True
while running:
    for x2 in range(rows):
      for y2 in range(rows):
            Cintensity = 255 - maximum*(255/total) + (noiseEnd[x2][y2]*(255/total))
            Cintensity = int(Cintensity)
            red = 0
            green = 0
            blue = 0
            if Cintensity < 40:
              blue = 150
            elif Cintensity < 70:
              blue = 215
              green = 75
            elif Cintensity < 90:
              blue = 215
              red = 50
              green = 150
            elif Cintensity < 110:
              red = 217
              green = 202
              blue = 128
            elif Cintensity < 120:
              green = 180
            elif Cintensity < 160:
              green = 150
            elif Cintensity < 200:
              green = 100
            elif Cintensity < 230:
              red = 50
              green = 50
              blue = 50
            elif Cintensity < 256:
              red = 200
              green = 200
              blue = 200
            pygame.draw.rect(screen,(red,green,blue),(x2*(screensize/rows),y2*(screensize/rows),screensize/rows+rows/10,screensize/rows+rows/10))
            

    # update screen
    while True:
      pygame.display.update()
