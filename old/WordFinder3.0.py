import glob, os, os.path, sys

for dirpath, dirnames, filenames in os.walk("/"):
    for filename in [f for f in filenames if f.endswith(".py")]:
        print(os.path.join(dirpath, filename))

