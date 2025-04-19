from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import extract_markdown_images, extract_markdown_links

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

    # print(text_node)
    # print(html_node)
    # print(leaf_node)
    # print(parent_node)
    # print(text_node_to_html_node(text_node))
    print(extract_markdown_links(""))


main()
    
