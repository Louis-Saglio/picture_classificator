import os
from PIL import Image


class ImageComparator:

    def __init__(self, controller):
        """
        :type controller: src.controller.Controller
        """
        self.controller = controller

    def show_image(self, name):
        with Image.open(os.path.join(self.controller.file_manager.telechargement_dir, name)) as img:
            img.show()
