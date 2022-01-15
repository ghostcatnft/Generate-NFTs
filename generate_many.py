import os, random, itertools, json
from PIL import Image

def listdir_nohidden(path):
  for file in os.listdir(path):
    if not file.startswith('.'):
      yield file

def listdir(path):
  return list(listdir_nohidden(path))

def listlen(path):
  return len(listdir(path))

number_of_nfts= 20

lengths = []
for i in range (0,6):
  lengths.append(listlen(f'./{i}'))

random_array = list(itertools.product(*(range(0, k) for k in lengths)))

for n in range(number_of_nfts):
  selected = random.choice(random_array)
  metadata = {
    "tokenId" : n + 1,
    "name" : f'ghost-cat-{n + 1}',
    "description" : 'Cute and Cuddly Ghost Cat.',
    "attributes" : [
      {
        "trait_type": "Background",
        "value": str(listdir('./0')[selected[0]]).split('.')[0].upper()
      },
      {
        "trait_type": "Skin",
        "value": str(listdir('./1')[selected[1]]).split('.')[0].upper()
      },
      {
        "trait_type": "Mouth",
        "value": str(listdir('./2')[selected[2]]).split('.')[0].upper()
      },
      {
        "trait_type": "Eyes",
        "value": str(listdir('./3')[selected[3]]).split('.')[0].upper()
      },
      {
        "trait_type": "Hat",
        "value": str(listdir('./4')[selected[4]]).split('.')[0].upper()
      },
      {
        "trait_type": "Accessory",
        "value": str(listdir('./5')[selected[5]]).split('.')[0].upper()
      }
    ]
  }
  # (4, 15, 15, 4, 2, 0)

  background= Image.open('./0/' + str(listdir('./0')[selected[0]]))
  skin= Image.open('./1/' + str(listdir('./1')[selected[1]]))
  mouth= Image.open('./2/' + str(listdir('./2')[selected[2]]))
  eyes= Image.open('./3/' + str(listdir('./3')[selected[3]]))
  hats= Image.open('./4/' + str(listdir('./4')[selected[4]]))
  accessory= Image.open('./5/' + str(listdir('./5')[selected[5]]))

  background.paste(skin, (0,0), skin)
  background.paste(mouth, (0,0), mouth)
  background.paste(eyes, (0,0), eyes)
  background.paste(hats, (0,0), hats)
  background.paste(accessory, (0,0), accessory)
  background.save(f'./output/ghostcat-{n+1}.png')

  with open(f'./output/metadata/ghostcat-{n+1}.json', "w") as file:
    file.write(json.dumps(metadata, indent = 2))

  random_array.remove(selected)

print("NFTs saved!")
