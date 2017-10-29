import random
import bs4
import typing
import requests
import PIL.Image
import os
import hashlib


IMAGE_URLS = os.path.join(os.getcwd(), "image_urls")


def get_image_search_url(topic: str, search_face=True) -> str:
    """
    return the url for searching an image about <topic> in google image
    topic: the search query
    search_face: if True, will try to find images with human face in it
    """
    return f"https://www.google.fr/search?q=" \
           f"{topic.strip().replace(' ', '+')}&tbm=isch" \
           f"{'&tbs=itp:face' if search_face else ''}"


def get_image_urls(url: typing.Iterable, image_urls_path) -> typing.Generator:
    """
    Return a Generator containing urls of images found on GoogleImage with the url <url>
    url: the search url for finding images on GoogleImage
    """
    with open(image_urls_path, 'r') as f:
        saved_urls = f.read().splitlines()
    soupe = bs4.BeautifulSoup(requests.get(url).content, "html.parser")
    return (image.attrs["src"] for image in soupe.findAll("img") if image.attrs["src"] not in saved_urls)


def register_image_url(url: str, file: str):
    """
    register images in the file './images_urls'"
    """
    with open(file, 'a') as f:
        f.write(url + '\n')


def download_image(url: str, path: str, image_urls_file):
    with open(os.path.join(path, hashlib.md5(bytes(url, encoding="utf-8")).hexdigest()), 'wb') as f:
        f.write(requests.get(url).content)
    register_image_url(url, image_urls_file)


def download_images(urls, path: str, image_urls_file, log=False):
    for url in urls:
        if log:
            print("Loading : ", url)
        download_image(url, path, image_urls_file)


def show_image(path: str):
    """
    show the image <image> in a new window
    """
    with PIL.Image.open(path) as img:
        img.show()


def get_random_image(directory):
    try:
        file = random.choice([file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))])
    except IndexError:
        return None
    return os.path.join(directory, file)


def test():
    import shutil

    # get or create test app
    if os.path.isdir('data_for_test'):
        shutil.rmtree('data_for_test')
    os.mkdir('data_for_test')
    if os.path.isfile(IMAGE_URLS):
        os.remove(IMAGE_URLS)
    os.mknod(IMAGE_URLS)

    # Tests
    url = get_image_search_url('ordre', True)
    images = get_image_urls(url, 'images_url')
    download_images(images, 'data_for_test', 'image_urls')
    image = get_random_image('data_for_test')
    if image:
        show_image(image)

    # Remove tests app
    os.remove(IMAGE_URLS)
    shutil.rmtree('data_for_test')


if __name__ == '__main__':
    test()
