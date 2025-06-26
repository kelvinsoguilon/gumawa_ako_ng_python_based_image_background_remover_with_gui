#import necessary libraries rembg, pillow, io, tkinter
#get image from os or files from desktop
#remove the background of image
#save image to desktop or any path you want

import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import io
from get_background_removed import BackgroundRemover

class InterfaceBackgroundRemover:
    def __init__(self, root):
        self.processor = BackgroundRemover()
        self.root = root
        self.root.title = "Background Remover"