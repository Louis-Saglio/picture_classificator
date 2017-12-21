import hashlib
import os

import bs4
import requests

from src.utils import read_from_file


class ImageDownloader:
    def __init__(self, controller):
        """
        :type controller: src.controller.Controller
        """
        self.controller = controller

    def _write_search_url(self):
        return f"https://www.google.fr/search?q={self.controller.theme_manager.generate_query()}" \
               f"&tbm=isch{'&tbs=itp:face' if self.controller.theme_manager.search_options['face'] else ''}"

    def get_image_urls(self, url=None):
        if url is None:
            url = self._write_search_url()
        saved_urls = read_from_file(self.controller.file_manager.get_saved_urls_file_path())
        soupe = bs4.BeautifulSoup(requests.get(url).content, "html.parser")
        return [image.attrs["src"] for image in soupe.findAll("img") if image.attrs["src"] not in saved_urls]

    def download_images(self, image_urls=None, image_nbr=20):
        # todo: test
        # todo: merge image_urls & image_nbr
        if image_urls is None:
            image_urls = set()
            while len(image_urls) < image_nbr:
                image_urls.update(self.get_image_urls())
        for url in image_urls:
            file_name = hashlib.sha256(bytes(url, "utf-8")).hexdigest()
            if file_name not in os.listdir(self.controller.file_manager.telechargement_dir):
                self.controller.file_manager.save_to_download(
                    requests.get(url).content,
                    file_name
                )
