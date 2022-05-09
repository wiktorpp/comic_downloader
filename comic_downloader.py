import sys
import os

path = sys.argv[1]
try:
    output_dir = sys.argv[2]
except IndexError:
    try:
        episode, comic_name = sys.argv[1][:-5].split(" | ")
        output_dir = f"{comic_name}/{episode}"
    except IndexError:
        output_dir = "output"

try: os.makedirs(output_dir)
except FileExistsError: pass

html = open(path).read()
files_dir = f"{path[:-5]}_files"



#get a list of all files
files = os.listdir(files_dir)
comic_imgs = []
for filename in files:
    #check if filename is numbers not including file extension
    if filename.split(".")[0].isdigit():
        comic_imgs.append(filename)

#sort the images in the order in which they appear in the html
indexes = []
for img in comic_imgs:
    #find index of img in html
    index = html.find(img)
    indexes.append(index)

index_and_img = list(zip(indexes, comic_imgs))

#order the images in the order in which they appear in the html
index_and_img = sorted(index_and_img, key=lambda x: x[0])

#copy file to order in which it appears in html
for i, img in enumerate(index_and_img):
    _, img = img
    with open(f"{files_dir}/{img}", "rb") as input, open(f"{output_dir}/{i}.jpg", "wb") as output:
        output.write(input.read())

#158958397734613812155.jpg
