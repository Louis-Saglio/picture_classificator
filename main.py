import os
import shutil
import time
import helpers.app_manager as app_mgr
import helpers.image_manager as image_mgr
import random


class Topic:
    ROOT = app_mgr.load_json("/home/louis/Projects/picture_classificator/config/config.json")["app_root"]

    def __init__(self, name: str, topic: str, create_files=True, minor_keywords=()):
        self.name = name
        self.topic = topic
        self.root = os.path.join(Topic.ROOT, name)
        self.image_dir = os.path.join(self.root, "images")
        self.main_keywords = [topic]
        self.minor_keywords = list(minor_keywords)
        if create_files:
            self.initialize()

    def initialize(self):
        if os.path.isdir(self.root):
            shutil.rmtree(self.root)
        os.makedirs(self.image_dir, 0o700)
        os.mknod(os.path.join(self.root, "image_urls"))

    def remove_files(self):
        shutil.rmtree(self.root)

    def add_minor_keywords(self, *keywords: str):
        for keyword in keywords:
            self.minor_keywords.append(keyword)

    def add_main_keywords(self, *keywords: str):
        for keyword in keywords:
            self.main_keywords.append(keyword)

    def create_search_url(self, face=False, log=False):
        keywords = app_mgr.choice(self.main_keywords, random.randint(1, len(self.main_keywords)))
        keywords.extend(app_mgr.choice(self.minor_keywords, random.randint(0, len(self.minor_keywords)), False))
        random.shuffle(keywords)
        if log:
            print(keywords)
        return image_mgr.get_image_search_url('+'.join(keywords), face)

    def get_images(self, search_face=False, log=False):
        image_mgr.download_images(
            image_mgr.get_image_urls(self.create_search_url(search_face, log), os.path.join(self.root, 'image_urls')),
            self.image_dir,
            os.path.join(self.root, 'image_urls'),
            log=log
        )

    def show_random(self):
        image_mgr.show_image(image_mgr.get_random_image(self.image_dir))

    def show_all(self):
        for img_path in app_mgr.rlistdir(self.image_dir):
            image_mgr.show_image(img_path)
            time.sleep(0.5)


def main():
    topic = Topic("Arbres", "tree", minor_keywords=("tronc", "branche"))
    topic.add_minor_keywords("plante", "forêt", "forest", "nature")
    topic.get_images(True, True)
    topic.show_random()


if __name__ == '__main__':
    main()
