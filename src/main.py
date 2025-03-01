from textnode import TextNode, TextType

def main():
    test_node = TextNode("go away", TextType.BOLD, "http://example.com")
    print(test_node)

if __name__ == "__main__":
    main()
