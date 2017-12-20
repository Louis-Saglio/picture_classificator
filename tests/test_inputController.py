from unittest import TestCase

import shutil

from src.controller import Controller
import src.exceptions


class TestInputController(TestCase):

    def setUp(self):
        self.controller = Controller('test')

    def test_input(self):
        self.controller.settings.DEBUG = False
        self.assertRaises(
            src.exceptions.EndProgramSignal,
            lambda: self.controller.input_controller.input("Ecrivez stop >>> ")
        )

    def test_get_fav_image(self):
        pass

    def __del__(self):
        shutil.rmtree(self.controller.file_manager.root_dir)
