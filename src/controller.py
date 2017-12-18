import settings
from src.file_manager import FileManager
from src.image_comparator import ImageComparator
from src.image_downloader import ImageDownloader
from src.input_controller import InputController
from src.theme_manager import ThemeManager


class Controller:

    def __init__(self, name=None):
        if name is None:
            name = self.input_controller.get_theme_name()
        self.settings = settings
        self.input_controller = InputController(self)
        self.theme_manager = ThemeManager(name)
        self.file_manager = FileManager(self)
        self.image_downloader = ImageDownloader(self)
        self.image_comparator = ImageComparator(self)
