import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

        node3 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node4 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertEqual(node3, node4)

        node5 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node5)

    def test_not_eq(self):
        node = TextNode("This is not text node", "normal")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

        node3 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node4 = TextNode("This is a text node", "bold", None)
        self.assertNotEqual(node3, node4)

if __name__ == "__main__":
    unittest.main()
