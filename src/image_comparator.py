import os
import random

from PIL import Image


class ImageComparator:

    def __init__(self, controller):
        """
        :type controller: src.controller.Controller
        """
        self.controller = controller
        self.images = {}

    def show_image(self, file_name, directory=None):
        if directory is None:
            directory = self.controller.file_manager.telechargement_dir
        with Image.open(os.path.join(directory, file_name)) as img:
            img.show()

    def build_app(self):
        images = os.listdir(self.controller.file_manager.telechargement_dir)
        for image in images:
            self.images[image] = 100

    def compare(self):
        if len(self.images) < 2:
            raise ValueError("Il doit y avoir au moins deux images enregistrées. Penser à lancer self.build_app()")
        image1, image2 = random.sample(list(self.images), 2)
        self.show_image(image1)
        self.show_image(image2)
