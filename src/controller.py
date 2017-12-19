import dill
# I use dill instead of pickle because pickle can't dump module objects and controller.settings is a module object

import settings
from src.file_manager import FileManager
from src.image_comparator import ImageComparator
from src.image_downloader import ImageDownloader
from src.input_controller import InputController
from src.theme_manager import ThemeManager


class Controller:

    def __init__(self, name=None):
        self.settings = settings
        self.input_controller = InputController(self)
        if name is None:
            name = self.input_controller.get_theme_name()
        self.theme_manager = ThemeManager(name)
        self.file_manager = FileManager(self)
        self.image_downloader = ImageDownloader(self)
        self.image_comparator = ImageComparator(self)

    def save(self):
        with open(self.file_manager.saved_app_file, 'wb') as f:
            dill.dump(self, f)
