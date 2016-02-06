#############################
# Author: Naren Mudivarthy
#
#############################

# Script to rename image files with timestamp of image creation

import os, time, datetime

image_extensions = []

image_extensions.append(".jpg")
image_extensions.append(".png")
image_extensions.append(".gif")
image_extensions.append(".JPG")
image_extensions.append(".PNG")
image_extensions.append(".GIF")

def rename_images_to_creation_time_stamp(image_folder_path):
    file_name_dict = dict()

    # walk through the directories
    for walk_dir, dirs, files in os.walk(image_folder_path):
        counter = 0
        for file in files :

            f, file_extension = os.path.splitext(file)

            # skip if file in not an image
            if not file_extension in image_extensions:
                continue

            file_path = os.path.join(walk_dir, file)
            new_file_name = str(datetime.datetime.strptime(time.ctime(
                                    os.path.getmtime(file_path)),
                                    "%a %b %d %H:%M:%S %Y"))
            new_file_name = new_file_name.replace("-", "_")
            new_file_name = new_file_name.replace(":", "_")
            new_file_name = new_file_name.replace(" ", "_")

            # Handling the case for image with same time stamp
            if new_file_name in file_name_dict.keys():
                file_name_dict[new_file_name] +=1
                new_file_name = new_file_name + "_" + str(counter)

            file_name_dict[new_file_name] = 0
            new_file_path = os.path.join(walk_dir, new_file_name+ file_extension)

            print file_path + "->" +new_file_name

            os.rename(file_path, new_file_path)


if __name__ == '__main__':
    rename_images_to_creation_time_stamp(os.getcwd())