import os
import random
from statistics import mean

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
        for image in os.listdir(self.controller.file_manager.telechargement_dir):
            self.images[image] = 100

    def compare(self, images=None):
        if images is None:
            images = random.sample(list(self.images), 2)
        if len(images) > 2:
            # todo: test
            raise NotImplementedError
        if len(self.images) < 2:
            # todo: test
            raise ValueError("Il doit y avoir au moins deux images enregistrées. Penser à lancer self.build_app()")
        # todo: show_images(...)
        self.show_image(images[0])
        self.show_image(images[1])
        fav_num = self.controller.input_controller.get_fav_image()
        other_num = 1 if fav_num == 0 else 0
        if self.images[images[0]] == self.images[images[1]]:
            self.images[images[fav_num]] += 10
        # todo: test
        elif self.images[images[fav_num]] < self.images[images[fav_num]]:
            new_val = round(mean((self.images[images[fav_num]], self.images[images[other_num]])))
            self.images[images[fav_num]], self.images[images[other_num]] = new_val, new_val
