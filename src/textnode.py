from enum import Enum

class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"


class TextNode():
    def __init__(self, text, text_type, url=None):
        """
        text: content of the node
        text_type: type of content (member of TextType Enum)
        url: url to a link or image (optional)
        """

        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    def __repr__(self):
        # the .value is needed to access the value of enum. e.g. Color["ITALIC"].value
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
