import os
import shutil
from block_markdown import markdown_to_html_node, extract_title
from inline_markdown import *

    
def copy_dir(from_path, dest_path):
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    else:
        shutil.rmtree(dest_path)

    for item in os.listdir(from_path):
        s = os.path.join(from_path, item)
        d = os.path.join(dest_path, item)
        print(f"{s} -> {d}")
        
        if os.path.isdir(s):
            copy_dir(s, d)
        else:
            shutil.copy(s, d)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = ""
    with open(from_path, "r") as f:
        markdown = f.read()

    template_html = ""
    with open(template_path, "r") as f:
        template_html = f.read()

    content_html = markdown_to_html_node(markdown).to_html()
    content_title = extract_title(markdown)
    generated_html = template_html.replace("{{ Title }}", content_title).replace("{{ Content }}", content_html)
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(generated_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)
    for item in os.listdir(dir_path_content):
        s = os.path.join(dir_path_content, item)
        d = os.path.join(dest_dir_path, item)
        print(f"{s} -> {d}")
        
        if os.path.isdir(s):
            generate_pages_recursive(s, template_path, d)
        else:
            generate_page(s, template_path, d.replace(".md", ".html"))
    

def main():
    copy_dir("static", "public")
    generate_pages_recursive("content", "template.html", "public")

main()