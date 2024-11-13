import unittest
import importlib
from snapshot_restore_py import get_before_snapshot, get_after_restore

class TestHooks(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.get_before_snapshot_registry = []
        self.get_after_restore_registry = []
        super(TestHooks, self).__init__(*args, **kwargs)

    def setUp(self):
        importlib.import_module("tests.samples")
        self.get_before_snapshot_registry = get_before_snapshot()
        self.get_after_restore_registry = get_after_restore()
        super(TestHooks, self).setUp()

    def test_all_hooks_are_registered(self):
        self.assertEqual(len(self.get_before_snapshot_registry), 2)
        self.assertEqual(len(self.get_after_restore_registry), 2)

    def test_registering_before_snapshot_decorator_works(self):
        from tests.samples import fun_1
        self.assertEqual(self.get_before_snapshot_registry[0], (fun_1, (), {}))

    def test_registering_after_restore_decorator_works(self):
        from tests.samples import fun_2
        self.assertEqual(self.get_after_restore_registry[0], (fun_2, (), {}))

    def test_registering_before_snapshot_works(self):
        from tests.samples import fun_3
        self.assertEqual(self.get_before_snapshot_registry[1], (fun_3, (1,), {}))

    def test_registering_after_restore_works(self):
        from tests.samples import fun_3
        self.assertEqual(self.get_after_restore_registry[1], (fun_3, (2,), {"arg1": "Lambda", "arg2": "SnapStart"}))

    def test_decorated_functions_work_normally(self):
        from tests.samples import fun_1, fun_2
        self.assertEqual(fun_1(), 1)
        self.assertEqual(fun_2(), 2)
