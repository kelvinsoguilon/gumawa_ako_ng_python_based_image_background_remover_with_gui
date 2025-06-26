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

        #title box in window panel
        self.title_label = tk.Label(root, text = "Image Background Remover", font = ("Arial", 20))
        self.title_label.pack(pady=10)

        #image type
        self.label_frame = tk.Frame(root)
        self.label_frame.pack()

        self.original_label = None
        self.processed_label = None

        #image display comparison in UI
        self.image_frame = tk.Frame(root)
        self.image_frame.pack()

        self.original_image_box = tk.Label(self.image_frame)
        self.original_image_box.grid(row=0, column=0, padx=30)

        self.result_image_box = tk.Label(self.image_frame)
        self.result_image_box.grid(row=0, column=1, padx=30)
        
        #Choose image and save button
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=20)

        self.choose_button = tk.Button(root, text = "Choose Image", font = ("Arial", 12), command= self.choose_image)
        self.choose_button.grid(row=0, column=0, padx= 30)

        self.save_button = tk.Button(root, text = "Save Image", font = ("Arial", 12), command=self.save_image, state=tk.DISABLED)
        self.save_button.grid(row = 0, column = 1, padx = 30)

        self.result_image = None

        