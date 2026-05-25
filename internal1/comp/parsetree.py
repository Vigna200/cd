import xml.etree.ElementTree as ET
class SmallLangParser:
    def parser(self, filename):
        tree = ET.parse(filename)
        return tree.getroot()
    def build_tree(self, node):
        if len(node) == 0:
            if node.text and node.text.strip():
                return node.text.strip()
            return node.tag
        children = [self.build_tree(child) for child in node]

        if node.tag == "assign":
            return ("=", children[0], children[1])
        elif node.tag in ["add", "sub", "mul", "div"]:
            op_map = {
                "add": "+",
                "sub": "-",
                "mul": "*",
                "div": "/"
            }
            return (op_map[node.tag], children[0], children[1])
        elif node.tag == "expr":
            return children[0]
        else:
            return (node.tag, *children)
    def print_tree(self, node, level=0):
        indent = "  " * level
        if isinstance(node, tuple):
            print(indent + str(node[0]))
            for child in node[1:]:
                self.print_tree(child, level + 1)
        else:
            print(indent + str(node))
parser = SmallLangParser()
root = parser.parser("input.xml")
tree = parser.build_tree(root)
parser.print_tree(tree)