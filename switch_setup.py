from modify_color import modify_colors
from coppy_image import auto_copy_images
import os

if __name__ == "__main__":
    file_path = 'files_details/ColorFile.bs'
    colors_to_change = {
        'tvWhite': '0x555555ff',
        'accent': '0x123456'
    }
    modify_colors(file_path, colors_to_change)

    current_dir = os.path.dirname(os.path.realpath(__file__))
    source_dir = os.path.join(current_dir, 'files_to_coppy')
    target_dir = os.path.join(current_dir, 'files_details')
    image_names = ['img1.png', 'img2.png']
    
    auto_copy_images(source_dir, target_dir, image_names)
