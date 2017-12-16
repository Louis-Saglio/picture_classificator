import os
import shutil
from unittest import TestCase

from src.controller import Controller


class TestFileManager(TestCase):

    def setUp(self):
        self.controller = Controller()

    def test_get_root_dir(self):
        root_dir = self.controller.file_manager.get_root_dir()
        self.assertEqual(
            root_dir,
            os.path.join(self.controller.settings.APP_DIR, self.controller.settings.DEFAULT_APP_NAME)
        )

    def test_get_saved_urls_file_path(self):
        self.assertEqual(
            self.controller.file_manager.get_saved_urls_file_path(),
            os.path.join(
                os.path.join(self.controller.settings.APP_DIR, self.controller.settings.DEFAULT_APP_NAME),
                self.controller.settings.SAVED_URLS_FILE
            )
        )

    def test_get_random_file_name(self):
        self.controller.settings.CHAR_FOR_FILE_NAME = "a"
        self.controller.settings.FILE_NAME_LENGTH = 3
        self.assertEqual(
            "aaa",
            self.controller.file_manager.get_random_file_name(self.controller.file_manager.telechargement_dir)
        )

    def test_save_to_download(self):
        self.controller.file_manager.save_to_download(b"foo bar", 'test')
        self.assertIn('test', os.listdir(self.controller.file_manager.telechargement_dir))

    def __del__(self):
        shutil.rmtree(self.controller.file_manager.root_dir)
