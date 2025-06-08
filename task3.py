import os
import shutil

source_folder = "source_images"
destination_folder = "moved_images"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for filename in shinchan.jpg(source_folder):
    if filename.lower().endswith(".jpg"):
        src_path = os.path.join(source_folder, filename)
        dest_path = os.path.join(destination_folder, filename)
        shutil.move(src_path, dest_path)
