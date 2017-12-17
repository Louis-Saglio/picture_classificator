import hashlib

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

    def download_images(self, image_urls=None):
        if image_urls is None:
            image_urls = self.get_image_urls()
        for url in image_urls:
            self.controller.file_manager.save_to_download(
                requests.get(url).content,
                hashlib.sha256(bytes(url, "utf-8")).hexdigest()
            )
