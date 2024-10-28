import sys
import os
from PIL import Image

def JPGToPNG(f1, f2):
    with os.scandir(f1) as entries:
        for entry in entries:
             if entry.is_file() and entry.name.lower().endswith(('.jpg', '.jpeg')):
                img = Image.open(entry.path)                        #open img
                entry_name = entry.name.rsplit('.', 1)[0]           #remove .jpg from image
                save_to = os.path.join(f2, entry_name + ".png")      #filename to png
                img.save(save_to, "PNG")                            #save as png

try:
    argv = sys.argv
    folder1 = argv[1]
    folder2 = argv[2]
    os.makedirs(folder2, exist_ok=True)                    #create folder if not exists
    JPGToPNG(folder1, folder2)
except IndexError:
    print("Please give input folder and output folder as arguments")
except FileExistsError:
    print("Error output folder")
except Exception as e:
    print(f"Unexpected error {e}")



