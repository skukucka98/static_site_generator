from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

def main():
    text_node = TextNode("This is some text in my node", TextType.LINK, "https://www.boot.dev")
    html_node = HTMLNode("<span>", "oh shoot it's dat boi", None, {"href": "https://www.google.com","target": "_blank"})
    leaf_node = LeafNode(None, "this is a test", {"href": "https://www.google.com","target": "_blank"})
    parent_node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text", {"href": "https://yahoo.com","target": "_something"}),
            LeafNode("i", "italic text", {"href": "https://yahoo.com","target": "_something"}),
            LeafNode(None, "Normal text"),
        ],
        {"href": "https://www.google.com","target": "_blank"}
    )

    print(text_node)
    print(html_node)
    print(leaf_node.to_html())
    print(parent_node.to_html())

main()
    
