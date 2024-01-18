import shutil
import os

def copy_image(src, dest):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copy(src, dest)
    print(f"Copied {src} to {dest}")

def auto_copy_images(source_dir, target_dir, image_names):
    for image_name in image_names:
        src_path = os.path.join(source_dir, image_name)
        dest_path = os.path.join(target_dir, image_name)
        copy_image(src_path, dest_path)

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))
    source_dir = os.path.join(current_dir, 'files_to_coppy')
    target_dir = os.path.join(current_dir, 'files_details')
    image_names = ['img11.png', 'img2.png']
    
    auto_copy_images(source_dir, target_dir, image_names)
# Make sure you have both images in files_to_coppy directory
