import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("testing textnode", TextType.BOLD)
        node2 = TextNode("testing textnode", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("testing textnode", TextType.BOLD)
        node2 = TextNode("different content", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("testing textnode", TextType.BOLD)
        node2 = TextNode("testing textnode", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_none_as_url(self):
        node = TextNode("testing textnode", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_url_eq(self):
        node = TextNode("testing textnode", TextType.ITALIC, "http://example.com")
        node2 = TextNode("testing textnode", TextType.ITALIC, "http://example.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("testing textnode", TextType.ITALIC)
        self.assertEqual("TextNode(testing textnode, italic, None)", repr(node))

if __name__ == "__main__":
    unittest.main()
