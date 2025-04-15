from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value == None:
            return ValueError("a value is required")
        if self.tag == None:
            return f"{self.value}"
        
        # Get into the meat and potatoes here