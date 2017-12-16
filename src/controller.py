import settings
from src.file_manager import FileManager
from src.image_downloader import ImageDownloader
from src.input_controller import InputController
from src.theme_manager import ThemeManager


class Controller:

    def __init__(self):
        self.settings = settings
        self.input_controller = InputController(self)
        self.theme_manager = ThemeManager(self.input_controller.get_theme_name(auto=True))
        self.file_manager = FileManager(self)
        self.image_downloader = ImageDownloader(self)
