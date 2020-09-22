import os
import json

path = "./images/"
repoimgpath="https://raw.githubusercontent.com/teabreaktime/pictocards/master/images/"

categories=os.listdir(path)
pictograms={}
for c in categories:
    pictograms[c]=list(map(lambda v: repoimgpath+c+"/"+v,sorted(os.listdir(os.path.join(path,c)))))

with open('pictogramas.json', 'w') as outfile:
    json.dump(pictograms, outfile)
    
