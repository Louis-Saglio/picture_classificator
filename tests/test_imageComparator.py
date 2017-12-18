import os
import shutil
from unittest import TestCase

from src.controller import Controller


class TestImageComparator(TestCase):

    def setUp(self):
        self.controller = Controller()

    def test_show_image(self):
        self.controller.image_downloader.download_images()
        self.controller.image_comparator.show_image(os.listdir(self.controller.file_manager.telechargement_dir)[0])

    def test_build_app(self):
        self.controller.image_comparator.build_app()

    def test_compare(self):
        self.controller.image_downloader.download_images()
        self.controller.image_comparator.build_app()
        self.controller.image_comparator.compare()
        self.assertIn(110, self.controller.image_comparator.images.values())

    def __del__(self):
        shutil.rmtree(self.controller.file_manager.root_dir)
