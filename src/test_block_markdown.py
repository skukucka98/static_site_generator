import unittest
from block_markdown import (
    BlockType,
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node
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
            BlockType.HEADING1,
        )

    def test_block_to_block_type_heading2(self):
        md = "## Hello heading2"
        type = block_to_block_type(md)
        self.assertEqual(
            type,
            BlockType.HEADING2,
        )

    def test_block_to_block_type_heading3(self):
        md = "### Hello heading3"
        type = block_to_block_type(md)
        self.assertEqual(
            type,
            BlockType.HEADING3,
        )

    def test_block_to_block_type_heading4(self):
        md = "#### Hello heading4"
        type = block_to_block_type(md)
        self.assertEqual(
            type,
            BlockType.HEADING4,
        )

    def test_block_to_block_type_heading1(self):
        md = "##### Hello heading5"
        type = block_to_block_type(md)
        self.assertEqual(
            type,
            BlockType.HEADING5,
        )

    def test_block_to_block_type_heading1(self):
        md = "###### Hello heading6"
        type = block_to_block_type(md)
        self.assertEqual(
            type,
            BlockType.HEADING6,
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