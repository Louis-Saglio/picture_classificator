class InputController:

    def __init__(self, controller):
        self.controller = controller

    def input(self, message):
        received = input(message)
        if received.lower() == 'stop':
            self.controller.save()
            exit(0)
        return received

    def get_theme_name(self, auto=True):
        if auto:
            return self.controller.settings.DEFAULT_APP_NAME
        return self.input("Choisissez un nom pour ce système de gestion : >>> ")

    def get_fav_image(self, nbr=2):
        while True:
            rep = self.input("Choisissez votre image favorite. >>> ")
            try:
                if 0 < int(rep) <= nbr:
                    return int(rep) - 1
            except TypeError:
                pass
            print(f"Vous devez choisir un nombre entre 1 et {nbr} inclus")
