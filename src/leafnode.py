from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value)
        self.props = props

    def to_html(self):
        if self.value is None:
            raise ValueError("a value is required")
        if self.tag is None or self.tag == "":
            return f"{self.value}"
        
        html = f"<{self.tag}"
        if self.props is None:
            html += ">"
        else:
            html += f"{self.props_to_html()}>"

        return f"{html}{self.value}</{self.tag}>"