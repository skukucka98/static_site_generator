from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import (
    extract_markdown_images, 
    extract_markdown_links, 
    split_nodes_delimiter, 
    split_nodes_image, 
    split_nodes_link,
    text_to_textnodes
)
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type
)

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

    # images = extract_markdown_images("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)")
    # print(images[1][0])

    # text = "This is _italic text_ with an **image** ![to boot dev](https://www.boot.dev) and a `code block` link [to youtube](https://www.youtube.com/@bootdotdev)"

    # print(text_to_textnodes(text))

#     md = """
#               This is **bolded** paragraph

#             This is another paragraph with _italic_ text and `code` here
# This is the same paragraph on a new line              

# - This is a list
# - with items                              
#         """
#     blocks = markdown_to_blocks(md)
#     print(blocks)

    block = "1. Hello there baby\n3. Testtest"
    print(block_to_block_type(block))


main()
    
