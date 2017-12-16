#############################
# Author: Naren Mudivarthy
#
#############################

# This script creates a directory for each kind of file extension
# Moves the files to the corresponding extension folders

import os
import re
import shutil
import subprocess

image_extensions = []

image_extensions.append(".jpg")
image_extensions.append(".png")
image_extensions.append(".gif")
image_extensions.append(".JPG")
image_extensions.append(".PNG")
image_extensions.append(".GIF")

compressed_extensions = []

compressed_extensions.append(".zip")
compressed_extensions.append(".rar")
compressed_extensions.append(".gz")
compressed_extensions.append(".bz2")

app_extensions = []

app_extensions.append(".pkg")
app_extensions.append(".dmg")

doc_extensions = []
doc_extensions.append(".doc")
doc_extensions.append(".docx")

ppt_extensions = []
ppt_extensions.append(".pptx")

excel_extensions = []
excel_extensions.append(".xlsx")
excel_extensions.append(".xls")
excel_extensions.append(".csv")

movie_extensions = []
movie_extensions.append(".mkv")

c_program_extensions = []
c_program_extensions.append(".c")
c_program_extensions.append(".h")
c_program_extensions.append(".cpp")


def move_files_to_corresponding_dirs(dirToScreens):
    print("Moving files to corresponding folders in ", dirToScreens)

    # delete .DS_Store files
    print("started cleaning .DS_Store files")
    find_and_delete_ds_store = "find . -type f -name '.DS_Store'  -delete"
    subprocess.call(find_and_delete_ds_store, shell=True)
    print("completed cleaning .DS_Store files")

    files = [f for f in os.listdir(dirToScreens) if os.path.isfile(
        os.path.join(dirToScreens, f))]

    for filename in files:
        f, file_extension = os.path.splitext(filename)

        target_filename = filename
        if file_extension == "":
            file_extension = ".no_extension"

        if file_extension in image_extensions:
            file_extension = ".images"

        if file_extension in doc_extensions:
            file_extension = ".docs"

        if file_extension in ppt_extensions:
            file_extension = ".ppts"

        if file_extension in excel_extensions:
            file_extension = ".excel_sheets"

        if file_extension in compressed_extensions:
            file_extension = ".compressed"

        if file_extension in app_extensions:
            file_extension = ".installer_files"

        if file_extension in movie_extensions:
            file_extension = ".movies"

        if file_extension in c_program_extensions:
            file_extension = ".c_programs"

        if file_extension.find("@") > 0:
            file_extension = file_extension[:file_extension.index("@")]
            dot_index = filename.index(".")
            target_filename = filename[: filename.index("@", dot_index)]

        moveTo = os.path.join(dirToScreens, file_extension[1:])
        if not os.path.exists(moveTo):
            os.makedirs(moveTo)

        src = os.path.join(dirToScreens, filename)
        dst = os.path.join(moveTo, target_filename)
        try:
            shutil.move(src, dst)
        except Exception as e:
            print("Unable to arrange ", f)
            print("Reason:", str(e))

####################################
# Drity way to remove empty folders
# Change it when you have time
####################################


def delete_empty_folders(dirToScreens):
    files = [f for f in os.listdir(dirToScreens) if not f.startswith(".")]

    for walk_dir, dirs, fs in os.walk(dirToScreens):
        if (len(fs) == 0 and len(dirs) == 0):
            shutil.rmtree(walk_dir)
            print("Deleted -", walk_dir)


if __name__ == '__main__':
    move_files_to_corresponding_dirs(dirToScreens=os.getcwd())
    delete_empty_folders(dirToScreens=os.getcwd())
