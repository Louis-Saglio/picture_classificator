class InputController:

    def __init__(self, controller):
        self.controller = controller

    def get_theme_name(self, auto=True):
        if auto:
            return self.controller.settings.DEFAULT_APP_NAME
        return input("Choisissez un nom pour ce système de getsion : >>> ")
