import os
import shutil

from src.utils import get_random_string


class FileManager:

    def __init__(self, controller, delete=True):
        """
        :type controller: src.controller.Controller
        """
        self.controller = controller
        self.root_dir = self.get_root_dir()
        self.telechargement_dir = os.path.join(self.root_dir, self.controller.settings.TELECHARGEMENT_DIR)
        self.saved_app_file = os.path.join(
            self.root_dir,
            self.controller.settings.SAVED_APP_FILE_NAME_PREFIX + self.controller.theme_manager.name
        )
        if os.path.isdir(self.root_dir) and delete:
            shutil.rmtree(self.root_dir)
            os.makedirs(self.telechargement_dir)

    def get_root_dir(self):
        """Retourne le dossier racine des données de l'application"""
        return os.path.join(self.controller.settings.APP_DIR, self.controller.theme_manager.name)

    def get_saved_urls_file_path(self):
        return os.path.join(self.root_dir, self.controller.settings.SAVED_URLS_FILE)

    def get_random_file_name(self, directory):
        filename = None
        while filename in os.listdir(directory) or filename is None:
            filename = get_random_string(
                self.controller.settings.CHAR_FOR_FILE_NAME,
                self.controller.settings.FILE_NAME_LENGTH
            )
        return filename

    def save_to_download(self, content, file_name=None):
        if file_name is None:
            # todo: test
            file_name = self.get_random_file_name(self.telechargement_dir)
        with open(os.path.join(self.telechargement_dir, file_name), 'wb') as f:
            f.write(content)
