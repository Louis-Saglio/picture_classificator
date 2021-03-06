import dill
# I use dill instead of pickle because pickle can't dump module objects and controller.settings is a module object

import settings
from src.file_manager import FileManager
from src.image_comparator import ImageComparator
from src.image_downloader import ImageDownloader
from src.image_selector import ImageSelector
from src.input_controller import InputController
from src.signals_manager import SignalManager
from src.theme_manager import ThemeManager


class Controller:

    def __init__(self, name=None, delete=True):
        self.settings = settings
        self.input_controller = InputController(self)
        self.signals_manager = SignalManager(self)
        if name is None:
            name = self.input_controller.get_theme_name()
        self.theme_manager = ThemeManager(name)
        self.file_manager = FileManager(self, delete)
        self.image_downloader = ImageDownloader(self)
        self.image_comparator = ImageComparator(self)
        self.image_selector = ImageSelector(self)

    def save(self):
        with open(self.file_manager.saved_app_file, 'wb') as f:
            dill.dump(self, f)

    @staticmethod
    def load(name):
        controller = Controller(name, False)
        with open(controller.file_manager.saved_app_file, 'rb') as f:
            return dill.load(f)
