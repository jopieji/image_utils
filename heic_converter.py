import sys, os
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

if len(sys.argv) < 2: # need to edit for save dir
    print("Usage: python heic_converter.py source_directory\n")
    exit(0)

source_dir = sys.argv[1]
# can implement later save_dir = sys.argv[2]

directory = os.fsencode(source_dir)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".HEIC") or filename.endswith(".heic"):
        print("converting " + filename)
        dir_plus_filename = sys.argv[1] + filename
        print(dir_plus_filename)
        image = Image.open(dir_plus_filename)
        desired_filename = filename.strip(".heic").strip(".HEIC")
        conv_filename_string = "./converted/" + desired_filename + ".jpg"
        image.save(conv_filename_string)
        print("Saved as jpg")
    else:
        print("junk file: " + filename)

print("Converted all viable files in " + source_dir)

print("check if saved...")