from PIL import Image

class ImageProcessor:
    def __init__(self):
        self._image = None
        self.original_image_pil = None

    def load_image(self, path):
        try:
            with open(path, "rb") as file:
                self._image = file.read()
            self.original_image_pil = Image.open(path).convert("RGBA")
            return True
        except Exception as error:
            print(f"Error Loading image: {error}")
            return False

    def get_image_data(self):
        return self._image
    
    def get_original_image(self):
        return self.original_image_pil
    
    def process_image(self):
        raise NotImplementedError("Subclasses should implement image processing.")