import shutil
import unittest
import requests
import src.controller

# TODO: Supprimer les dépenance dans les tests


class TestImageDownloader(unittest.TestCase):

    def setUp(self):
        self.controller = src.controller.Controller()
        self.controller.theme_manager.add_keyword("test", 0)
        self.controller.theme_manager.search_options["face"] = True

    def test__write_search_url(self):
        self.assertIn("&tbs=itp:face", self.controller.image_downloader._write_search_url())
        requests.head(self.controller.image_downloader._write_search_url()).close()
        url = self.controller.image_downloader._write_search_url()
        self.assertIn(
            url,
            (
                "https://www.google.fr/search?q=default&tbm=isch&tbs=itp:face",
                "https://www.google.fr/search?q=test&tbm=isch&tbs=itp:face"
            )
        )

    def test_get_image_urls(self):
        print(self.controller.image_downloader.get_image_urls())

    def test_download_image(self):
        pass

    def __del__(self):
        shutil.rmtree(self.controller.file_manager.root_dir)
