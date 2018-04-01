import os
import shutil

directory = os.path.join(os.getcwd(), "test")
directory = "/Users/nmudivar/Desktop/RamayanaSlokas/5-SundaraKanda"
print(directory)

print(os.listdir(directory))

files = [f for f in os.listdir(directory) if os.path.isfile(
    os.path.join(directory, f))]

print(files)

for f in files:
    fn, ext = os.path.splitext(f)

    if ext == "":
        print(fn)

        src = os.path.join(directory, fn)
        dst = os.path.join(directory, fn + ".txt")

        try:
            shutil.move(src, dst)
        except Exception as e:
            print("Unable to arrange ", f)
            print("Reason:", str(e))
