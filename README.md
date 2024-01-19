# Python Value Replacer

This is a demonstration repository created to test the capability of python script to replace values in a file deep in the project

## Requirements
Python setup on the machine

## How to run 
### Example for a color change
```
python3 modify_color.py tvWhite 0x555555ff accent 0x333333ff
```
OR
```
python modify_color.py tvWhite 0x555555ff accent 0x333333ff
```
### Example to replace/populate images
Add the wanted images in files_to_coppy folder and check that the names are right in the `coppy_image.py` file.
```
python3 coppy_image.py
```
OR
```
python coppy_image.py
```
### Example to execute both image replace and color change
Add the details to the `switch_setup.py` file.
```
python3 switch_setup.py
```
OR
```
python switch_setup.py
```