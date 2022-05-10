import sys
import os

def parse_html_and_move_image(path, output_dir):
    try: os.makedirs(output_dir)
    except FileExistsError: pass

    try: html = open(path).read()
    except IsADirectoryError: exit()
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


try:
    if sys.argv[2] == '-d':
        path = sys.argv[1]
        output_dir = sys.argv[3]
        parse_html_and_move_image(path, output_dir)
    else:
        raise IndexError
except IndexError:
    try:
        for arg in sys.argv[1:]:
            if not arg[-5:] == '.html':
                continue
            episode, comic_name = arg[:-5].split(" | ")
            output_dir = f"{comic_name}/{episode}"
            print(output_dir)
            parse_html_and_move_image(arg, output_dir)
    except (IndexError, ValueError):
        output_dir = "output"
