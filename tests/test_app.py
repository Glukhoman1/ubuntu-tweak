import os
import shutil
import unittest

from ubuntutweak.modules import ModuleLoader
from ubuntutweak.common import consts
from ubuntutweak.main import UbuntuTweakWindow

class TestApp(unittest.TestCase):
    def setUp(self):
        self.window = UbuntuTweakWindow()

    def test_app(self):
        # tweaks
        self.window.select_target_feature('tweaks')
        self.assertEqual(self.window.loaded_modules, {})
        self.assertEqual(self.window.current_feature, 'tweaks')
        self.assertEqual(self.window.feature_dict, {'overview': 0,
                                                    'apps': 1,
                                                    'tweaks': 2,
                                                    'admins': 3,
                                                    'janitor': 4,
                                                    'search': 6,
                                                    'wait': 5})
        self.assertEqual(self.window.navigation_dict, {'tweaks': (None, None)})

        # tweaks->Nautilus
        self.window._load_module('Nautilus')
        self.assertEqual(self.window.loaded_modules, {'Nautilus': 7})
        self.assertEqual(self.window.current_feature, 'tweaks')
        self.assertEqual(self.window.navigation_dict, {'tweaks': ('Nautilus', None)})
        # Nautilus->tweaks
        self.window.on_back_button_clicked(None)
        self.assertEqual(self.window.current_feature, 'tweaks')
        self.assertEqual(self.window.navigation_dict, {'tweaks': (None, 'Nautilus')})
        # tweaks->Compiz
        self.window._load_module('Window')
        self.assertEqual(self.window.current_feature, 'tweaks')
        self.assertEqual(self.window.navigation_dict, {'tweaks': ('Window', None)})

    def todo(self):
        #TODO toggled has different behavir
        # admins->DesktopRecovery
        self.window._load_module('DesktopRecovery')
        self.window.admins_button.toggled()
        self.assertEqual(self.window.current_feature, 'admins')
        self.assertEqual(self.window.navigation_dict, {'tweaks': ('Compiz', None),
                                                       'admins': ('DesktopRecovery', None)})

        # DesktopRecovery->admins
        self.window.on_back_button_clicked(None)
        self.assertEqual(self.window.current_feature, 'admins')
        self.assertEqual(self.window.navigation_dict, {'tweaks': ('Compiz', None),
                                                       'admins': (None, 'DesktopRecovery')})

        # tweaks->Compiz
        self.window.select_target_feature('tweaks')
        self.assertEqual(self.window.current_feature, 'tweaks')
        self.assertEqual(self.window.navigation_dict, {'tweaks': ('Compiz', None),
                                                       'admins': (None, 'DesktopRecovery')})

    def tearDown(self):
        del self.window

if __name__ == '__main__':
    unittest.main()
