import unittest

from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_eq_props_to_html(self):
        node = HTMLNode("span", "oh shoot it's dat boi", HTMLNode("p", "oh shoot whaddup"), {"href": "https://www.google.com","target": "_blank"})
        prop_str = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(node.props_to_html(), prop_str)

    def test_not_eq_props_to_html(self):
        node = HTMLNode("span", "oh shoot it's dat boi", HTMLNode("p", "oh shoot whaddup"), {"href": "https://www.google.com","target": "_blank"})
        prop_str = " href=\"https://www.google.co\" target=\"_blank\""
        self.assertNotEqual(node.props_to_html(), prop_str)

    def test_eq_none_props_to_html(self):
        node = HTMLNode("span", "oh shoot it's dat boi", HTMLNode("p", "oh shoot whaddup"))
        prop_str = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertNotEqual(node.props_to_html(), prop_str)

if __name__ == "__main__":
    unittest.main()