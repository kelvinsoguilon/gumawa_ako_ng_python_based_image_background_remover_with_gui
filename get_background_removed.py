from image_processor import ImageProcessor
from rembg import remove

class BackgroundRemover(ImageProcessor):
    def process_image(self):
        if self._image:
            try:
                return remove(self.image)
            except Exception as error:
                print("Error processing image: ", error)
                return None
            return None