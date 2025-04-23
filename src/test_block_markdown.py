import unittest
from block_markdown import (
    BlockType,
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node,
    extract_title
)


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_markdown_to_blocks_3_newlines(self):
        md = """
This is **bolded** paragraph


This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_markdown_to_blocks_trailing_spaces(self):
        md = """
              This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line              

- This is a list
- with items                              
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_block_to_block_type_heading1(self):
        md = "# Hello heading1"
        type = block_to_block_type(md)
        self.assertEqual(
            type,
            BlockType.HEADING,
        )


    def test_block_to_block_type_heading2(self):
        md = "## Hello heading2"
        type = block_to_block_type(md)
        self.assertEqual(
            type,
            BlockType.HEADING,
        )


    def test_block_to_block_type_heading3(self):
        md = "### Hello heading3"
        type = block_to_block_type(md)
        self.assertEqual(
            type,
            BlockType.HEADING,
        )


    def test_block_to_block_type_heading4(self):
        md = "#### Hello heading4"
        type = block_to_block_type(md)
        self.assertEqual(
            type,
            BlockType.HEADING,
        )


    def test_block_to_block_type_heading5(self):
        md = "##### Hello heading5"
        type = block_to_block_type(md)
        self.assertEqual(
            type,
            BlockType.HEADING,
        )


    def test_block_to_block_type_heading6(self):
        md = "###### Hello heading6"
        type = block_to_block_type(md)
        self.assertEqual(
            type,
            BlockType.HEADING,
        )


    def test_block_to_block_type_code(self):
        md = "```Code Blocking```"
        type = block_to_block_type(md)
        self.assertEqual(
            type,
            BlockType.CODE,
        )


    def test_block_to_block_type_quote(self):
        md = ">This is a quote"
        type = block_to_block_type(md)
        self.assertEqual(
            type,
            BlockType.QUOTE,
        )


    def test_block_to_block_type_quotes(self):
        md = ">quote1\n>quote2\n>quote3"
        type = block_to_block_type(md)
        self.assertEqual(
            type,
            BlockType.QUOTE,
        )


    def test_block_to_block_type_unordered_list_single(self):
        md = "- list item 1"
        type = block_to_block_type(md)
        self.assertEqual(
            type,
            BlockType.UNORDERED_LIST,
        )


    def test_block_to_block_type_unordered_list_multiple(self):
        md = "- list item 1\n- list item 2\n- list item 3"
        type = block_to_block_type(md)
        self.assertEqual(
            type,
            BlockType.UNORDERED_LIST,
        )


    def test_block_to_block_type_ordered_list(self):
        md = "1. item 1"
        type = block_to_block_type(md)
        self.assertEqual(
            type,
            BlockType.ORDERED_LIST,
        )


    def test_block_to_block_type_ordered_list_multiple(self):
        md = "1. item 1\n2. item 2\n3. item 3"
        type = block_to_block_type(md)
        self.assertEqual(
            type,
            BlockType.ORDERED_LIST,
        )


    def test_block_to_block_type_paragraph(self):
        md = "This is a plain ol' paragraph"
        type = block_to_block_type(md)
        self.assertEqual(
            type,
            BlockType.PARAGRAPH,
        )


    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


    def test_headingblock(self):
        md = """
### This is a heading3 block
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>This is a heading3 block</h3></div>",
        )


    def test_quoteblock(self):
        md = """
>This is a quote
>that I want to
>see if it works
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote that I want to see if it works</blockquote></div>",
        )


    def test_unordered_list_block(self):
        md = """
- Item 1
- Item 2
- Item 3
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>",
        )


    def test_ordered_list_block(self):
        md = """
1. Item 1
2. Item 2
3. Item 3
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Item 1</li><li>Item 2</li><li>Item 3</li></ol></div>",
        )


    def test_ordered_list_block_with_formatting(self):
        md = """
1. Item 1 **bold**
2. Item 2 _italic_
3. Item 3 `code`
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Item 1 <b>bold</b></li><li>Item 2 <i>italic</i></li><li>Item 3 <code>code</code></li></ol></div>",
        )


    def test_extract_title(self):
        md = "# Hello There"
        title = extract_title(md)
        self.assertEqual(
            title,
            "Hello There"
        )

    def test_extract_title_from_multiple_lines(self):
        md = """
# Hello There

this is not a title
this is a different block
"""
        title = extract_title(md)
        self.assertEqual(
            title,
            "Hello There"
        )