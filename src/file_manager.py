import os
import settings


class FileManager:

    def __init__(self, controller):
        """
        :type controller: src.controller.Controller
        """
        self.controller = controller
        self.root_dir = self.get_root_dir()
        self.telechargement_dir = os.path.join(self.root_dir, self.controller.settings.TELECHARGEMENT_DIR)
        os.makedirs(self.root_dir)
        os.makedirs(self.telechargement_dir)

    def get_root_dir(self):
        return os.path.join(settings.APP_DIR, self.controller.theme_manager.name)

    def get_saved_urls_file_path(self):
        return os.path.join(self.root_dir, self.controller.settings.SAVED_URLS_FILE)
