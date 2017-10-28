import random
import bs4
import typing
import requests
import PIL.Image
import os
import hashlib


def salt_function() -> str:
    """
    return a random character in "azertyuiopqsdfghjklmwxcvbn123456789"
    """
    return random.choice("azertyuiopqsdfghjklmwxcvbn123456789")


def get_image_search_url(topic: str, search_face=True) -> str:
    """
    return the url for searching an image about <topic> in google image
    topic: the search query
    search_face: if True, will try to find images with human face in it
    """
    return f"https://www.google.fr/search?q=" \
           f"{topic.strip().replace(' ', '+')}&tbm=isch" \
           f"{'&tbs=itp:face' if search_face else ''}"


def get_image_urls(url: typing.Iterable) -> typing.Generator:
    """
    Return a Generator containing urls of images found on GoogleImage with the url <url>
    url: the search url for finding images on GoogleImage
    """
    with open("image_urls", 'r') as f:
        saved_urls = f.read().splitlines()
    soupe = bs4.BeautifulSoup(requests.get(url).content, "html.parser")
    return (image.attrs["src"] for image in soupe.findAll("img") if image.attrs["src"] not in saved_urls)


def register_image_url(url: str):
    """
    register images in the file './images_urls'"
    """
    with open("image_urls", 'a') as f:
        f.write(url + '\n')


def download_image(url: str, path: str):
    with open(os.path.join(path, hashlib.md5(bytes(url, encoding="utf-8")).hexdigest()), 'wb') as f:
        f.write(requests.get(url).content)
    register_image_url(url)


def download_images(urls, path: str):
    for url in urls:
        download_image(url, path)


def show_image(path: str):
    with PIL.Image.open(path) as img:
        img.show()


def get_random_image(directory):
    return random.choice([file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))])


def main():
    url = get_image_search_url("ordre", True)
    images = get_image_urls(url)
    download_images(images, 'level')
    print(get_random_image('level'))


if __name__ == '__main__':
    main()
