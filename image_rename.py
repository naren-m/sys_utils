import os, time, datetime

# parent_dir = "/Users/nmudivar/Desktop/Naren_photos"

parent_dir = os.getcwd()


image_extensions = []

image_extensions.append(".jpg")
image_extensions.append(".png")
image_extensions.append(".gif")
image_extensions.append(".JPG")
image_extensions.append(".PNG")
image_extensions.append(".GIF")

new_file_name_list = []

for walk_dir, dirs, files in os.walk(parent_dir):
    counter = 0
    for file in files :
        
        f, file_extension = os.path.splitext(file)
        
        if not file_extension in image_extensions:
            continue
        file_path = os.path.join(walk_dir, file)
        new_file_name = str(datetime.datetime.strptime(time.ctime(os.path.getmtime(file_path)), "%a %b %d %H:%M:%S %Y"))
        new_file_name = new_file_name.replace("-", "_")
        new_file_name = new_file_name.replace(":", "_")
        new_file_name = new_file_name.replace(" ", "_")
        
        if new_file_name in new_file_name_list:
            counter +=1
            new_file_name = new_file_name + "_" + str(counter)
              
        
        new_file_name_list.append(new_file_name)        
        new_file_path = os.path.join(walk_dir, new_file_name+ file_extension)
        print file_path + "->" +new_file_name
        os.rename(file_path, new_file_path)
