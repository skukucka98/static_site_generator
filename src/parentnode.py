from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag)
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None or self.tag == "":
            raise ValueError("a tag is required")
        if self.children is None:
            raise ValueError("children is required")
        
        html = f"<{self.tag}"
        if self.props is None:
            html += ">"
        else:
            html += f"{self.props_to_html()}>"

        for child in self.children:
            html += child.to_html()
        
        html = f"{html}</{self.tag}>"

        return html