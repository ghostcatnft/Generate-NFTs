import os, random
from PIL import Image

def listdir_nohidden(path):
  for file in os.listdir(path):
    if not file.startswith('.'):
      yield file

def listdir(path):
  return list(listdir_nohidden(path))

background= Image.open('./0/' + random.choice(listdir('./0')))
skin= Image.open('./1/' + random.choice(listdir('./1')))
mouth= Image.open('./2/' + random.choice(listdir('./2')))
eyes= Image.open('./3/' + random.choice(listdir('./3')))
hats= Image.open('./4/' + random.choice(listdir('./4')))

background.paste(skin, (0,0), skin)
background.paste(mouth, (0,0), mouth)
background.paste(eyes, (0,0), eyes)
background.paste(hats, (0,0), hats)

background.save('sample.png')



