from enum import Enum
from htmlnode import LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING1 = "heading1"
    HEADING2 = "heading2"
    HEADING3 = "heading3"
    HEADING4 = "heading4"
    HEADING5 = "heading5"
    HEADING6 = "heading6"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    for i in range(len(blocks)):
        if blocks[i] == "":
            blocks[i] = blocks.pop(i)
            continue
        blocks[i] = blocks[i].strip()
    return blocks

def block_to_block_type(markdown):
    if markdown.startswith("###### "):
        return BlockType.HEADING6
    if markdown.startswith("##### "):
        return BlockType.HEADING5
    if markdown.startswith("#### "):
        return BlockType.HEADING4
    if markdown.startswith("### "):
        return BlockType.HEADING3
    if markdown.startswith("## "):
        return BlockType.HEADING2
    if markdown.startswith("# "):
        return BlockType.HEADING1
    if markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.CODE
    
    lines = markdown.split("\n")
    if all(map(lambda l: l.startswith(">"), lines)):
        return BlockType.QUOTE
    if all(map(lambda l: l.startswith("- "), lines)):
        return BlockType.UNORDERED_LIST
    
    ordered_list_check = []
    for i in range(len(lines)):
        if lines[i].startswith(f"{i+1}. "):
            ordered_list_check.append(True)
        else:
            ordered_list_check.append(False)
            break
    if all(ordered_list_check):
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        html_nodes.append(block_to_html_node(block))
    return ParentNode("div", html_nodes)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    lines = block.split("\n")
    match block_type:
        case BlockType.HEADING1:
            return LeafNode("h1", block.strip("# "))
        case BlockType.HEADING2:
            return LeafNode("h2", block.strip("## "))
        case BlockType.HEADING3:
            return LeafNode("h3", block.strip("### "))
        case BlockType.HEADING4:
            return LeafNode("h4", block.strip("#### "))
        case BlockType.HEADING5:
            return LeafNode("h5", block.strip("##### "))
        case BlockType.HEADING6:
            return LeafNode("h6", block.strip("###### "))
        case BlockType.QUOTE:
            leaf_nodes = []
            for line in lines:
                leaf_nodes.append(LeafNode("blockquote", line.replace(">", "")))
            return leaf_nodes
        case BlockType.UNORDERED_LIST:
            children = []
            for line in lines:
                children.append(LeafNode("li", line.replace("- ", "")))
            return ParentNode("ul", children)
        case BlockType.ORDERED_LIST:
            children = []
            for i in range(len(lines)):
                children.append(LeafNode("li", lines[i].replace(f"{i+1}. ", "")))
            return ParentNode("ol", children)
        case BlockType.CODE:
            return text_node_to_html_node(TextNode(block.replace("```"), TextType.CODE))
        case _:
            return LeafNode("p", block)
                