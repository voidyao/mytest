import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('Janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确处理像wolf amade mozart这样的姓名吗？"""
        formatted_name = get_formatted_name('wo', 'mozat', 'amadus')
        self.assertEqual(formatted_name, 'Wo Amadus Mozat')

unittest.main()