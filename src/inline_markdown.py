from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def recursive_split(text, delimiters):
        if not delimiters:
            return [text]
        current_delimiter = delimiters[0]
        remaining_delimiters = delimiters[1:]
        split_texts = re.split(re.escape(current_delimiter), text)
        result = []
        for subtext in split_texts:
            result.extend(recursive_split(subtext, remaining_delimiters))
        return result

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        images = extract_markdown_images(old_node.text)
        if old_node.text_type == TextType.IMAGE or images == []:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        delimiters = []
        for i in range(len(images)):
            delimiters.append(f"![{images[i][0]}]({images[i][1]})")
        sections = recursive_split(old_node.text, delimiters)
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            split_nodes.append(TextNode(sections[i], TextType.TEXT))
            if i >= len(sections)-1:
                continue
            split_nodes.append(TextNode(images[i][0], TextType.IMAGE, images[i][1]))
                    
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        links = extract_markdown_links(old_node.text)
        if old_node.text_type == TextType.IMAGE or links == []:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        delimiters = []
        for i in range(len(links)):
            delimiters.append(f"[{links[i][0]}]({links[i][1]})")
        sections = recursive_split(old_node.text, delimiters)
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            split_nodes.append(TextNode(sections[i], TextType.TEXT))
            if i >= len(sections)-1:
                continue
            split_nodes.append(TextNode(links[i][0], TextType.LINK, links[i][1]))
                    
        new_nodes.extend(split_nodes)
    return new_nodes

def text_to_textnodes(text):
    initial_node = TextNode(text, TextType.TEXT)
    bold_nodes = split_nodes_delimiter([initial_node], "**", TextType.BOLD)
    italic_nodes = split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC)
    code_nodes = split_nodes_delimiter(italic_nodes, "`", TextType.CODE)
    image_nodes = split_nodes_image(code_nodes)
    final_nodes = split_nodes_link(image_nodes)
    return final_nodes
