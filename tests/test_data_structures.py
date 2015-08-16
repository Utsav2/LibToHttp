from LibToHttp import data_structures
from tests.base import TestCase


class DataStructuresTestCase(TestCase):
    def test_no_duplicate_keys(self):
        data = data_structures.NoDuplicateDict()
        data['test'] = 0
        self.assertRaises(ValueError, data.__setitem__, 'test', 1)

    def test_otherwise_regular_dict(self):
        data = data_structures.NoDuplicateDict()
        data['test'] = 0
        # Would throw an exception if anything breaks
        data['test2'] = 0
