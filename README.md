I created a background remover program using python with GUI.
Source code From Hover Cube in YouTube

from rembg import remove import easygui
from PIL import Image
inputPath = easygui. fileopenbox (title='Select image file') easygui.filesavebox (title='Save file to..')
outputPath
input
=
Image.open(inputPath)
output = remove(input)
output.save(outputPath)
