import random

import src.exceptions


class InputController:

    def __init__(self, controller):
        """
        :type controller: src.controller.Controller
        """
        self.controller = controller

    def input(self, message, possible_values=None):
        if self.controller.settings.DEBUG:
            assert possible_values, "En mode debug veuillez fournir une liste des valeurs possibles"
            received = random.choice(possible_values)
        else:
            received = input(message)
        if received.lower() == 'stop':
            self.controller.save()
            raise src.exceptions.EndProgramSignal
        return received

    def get_theme_name(self):
        return self.input(
            "Choisissez un nom pour ce système de gestion : >>> ",
            (self.controller.settings.DEFAULT_APP_NAME,)
        )

    def get_fav_image(self, nbr=2):
        while True:
            rep = self.input("Choisissez votre image favorite. >>> ", ('1', '2'))
            try:
                if 0 < int(rep) <= nbr:
                    return int(rep) - 1
            # todo: test
            except ValueError:
                pass
            print(f"Vous devez choisir un nombre entre 1 et {nbr} inclus")
