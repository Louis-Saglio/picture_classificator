from unittest import TestCase

import pickle as dill

from src.controller import Controller


class TestController(TestCase):

    def setUp(self):
        self.controller = Controller("test")

    def test_save(self):
        self.controller.save()
        with open(self.controller.file_manager.saved_app_file, 'rb') as f:
            saved_controller: Controller = dill.load(f)
        assert type(self.controller) is type(saved_controller)
        for attr in self.controller.__dict__:
            field = getattr(self.controller, attr)
            for field_attr in field.__dict__:
                if field_attr == "controller":
                    continue
                self.assertEqual(getattr(field, field_attr), getattr(getattr(saved_controller, attr), field_attr))
