#############################
# Author: Naren Mudivarthy
#
#############################

# Script to rename image files with timestamp of image creation

import os, time, datetime
import subprocess, re, sys
from PIL import Image

image_extensions = list()

image_extensions.append(".jpg")
image_extensions.append(".png")
image_extensions.append(".gif")
image_extensions.append(".JPG")
image_extensions.append(".PNG")
image_extensions.append(".GIF")
image_extensions.append(".CR2")
image_extensions.append(".cr2")


def get_jpeg_exif_time(file_path):
    if not os.path.isfile(file_path):
        return None
    try:
        image = Image.open(file_path)
        if hasattr(image, '_getexif'):
            exifdata = image._getexif()
            create_time = exifdata[0x9003]
            # print "ctime - ", create_time, " exifdata - ",  exifdata[36868]
            return create_time
    except:
        _type, value, traceback = sys.exc_info()
        print "Error:\n", value

    return None

def get_file_name(file_path):
    new_file_name = get_jpeg_exif_time(file_path)
    if not new_file_name:
        print "Couldn't find file creation time for - ", file_path
        return new_file_name

    new_file_name = new_file_name.replace("-", "_")
    new_file_name = new_file_name.replace(":", "_")
    new_file_name = re.sub('[^\d]+', '_', new_file_name)
    return new_file_name

def rename_images_to_creation_time_stamp(image_folder_path):
    file_name_dict = dict()

    # for mac, cleaning up the .DS_Store files
    print "started cleaning .DS_Store files"
    find_and_delete_ds_store = "find . -type f -name '.DS_Store'  -delete"
    subprocess.call(find_and_delete_ds_store, shell=True)
    print "completed cleaning .DS_Store files"

    # walk through the directories
    for walk_dir, dirs, files in os.walk(image_folder_path):
        for file in files :

            f, file_extension = os.path.splitext(file)

            # skip if file in not an image
            if not file_extension in image_extensions:
                continue

            file_path = os.path.join(walk_dir, file)
            new_file_name = get_file_name(file_path)

            if not new_file_name:
                continue

            # Handling the case for image with same time stamp
            if new_file_name in file_name_dict.keys():
                file_name_dict[new_file_name] +=1
                new_file_name = new_file_name + "_" + str(file_name_dict[new_file_name])

            file_name_dict[new_file_name] = 0

            dest_dir = walk_dir

            if file_extension == ".CR2":
                if "CR2" in walk_dir:
                    # print "skippinv", dest_dir
                    continue

                dest_dir = os.path.join(walk_dir, file_extension[1:])

                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)

            new_file_path = os.path.join(dest_dir, new_file_name + file_extension)

            print file_path + " -> " +new_file_name
            try:
                os.rename(file_path, new_file_path)
            except Exception as e:
                print "Couldn't perform " +file_path + " -> " +new_file_name
                print e
                return

# atom git test

"""
    Usage : python image_rename.py
            or
            python image_rename.py /path/to/image/dir
"""
if __name__ == '__main__':
    try:
        path = sys.argv[1]
        if(not os.path.isdir(path)):
            print "Invalid directory - ", path
            sys.exit(1)
    except IndexError:
        path = os.getcwd()

    rename_images_to_creation_time_stamp(path)