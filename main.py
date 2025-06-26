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

        #Make the ui centered when run
        window_width = 800
        window_height = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
