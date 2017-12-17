import shutil
from unittest import TestCase

import os

from src.controller import Controller


class TestImageComparator(TestCase):

    def setUp(self):
        self.controller = Controller()
        self.controller.image_downloader.download_images()

    def test_show_image(self):
        self.controller.image_comparator.show_image(os.listdir(self.controller.file_manager.telechargement_dir)[0])

    def __del__(self):
        shutil.rmtree(self.controller.file_manager.root_dir)
