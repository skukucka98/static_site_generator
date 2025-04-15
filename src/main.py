from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    text_node = TextNode("This is some text in my node", TextType.LINK, "https://www.boot.dev")
    html_node = HTMLNode("<span>", "oh shoot it's dat boi", None, {"href": "https://www.google.com","target": "_blank"})
    print(text_node)
    print(html_node)

main()
    
