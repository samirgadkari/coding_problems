# Given the root to a binary tree, implement serialize(root),
# which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.

import json
import re


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return '{' + 'left: ' + str(self.left) + ',' + \
            ' val: ' + str(self.val) + ',' + \
            ' right: ' + str(self.right) + '}'


class NodeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Node):
            left = serialize(obj.left).replace('"', '')
            right = serialize(obj.right).replace('"', '')
            res = f'{{left: {left}, ' f'val: {obj.val}, ' f'right: {right}}}'
        else:
            res = super().default(self, obj)

        return res


class NodeDecoder(json.JSONDecoder):
    def decode(self, s):
        regex = r"^\{left:\s(\{.+\}|null),\sval:\s(.+?)," + \
            r"\sright:\s(\{.+\}|null)\}$"

        # Don't know why there are quotes in the string here.
        stripped_str = s.replace('"', '')
        matches = re.search(regex, stripped_str)

        if matches:
            left = matches.group(1)
            val = matches.group(2)
            right = matches.group(3)

            # print(f'left: {left}')
            # print(f'val: {val}')
            # print(f'right: {right}')

            if '{' in left:
                left = deserialize(left)
            elif left == 'null':
                left = None
            if '{' in right:
                right = deserialize(right)
            elif right == 'null':
                right = None

            res = Node(val, left, right)
            # print(f'returning res: {res} of type: {type(res)}')
            return res

        print(f'returning None for s: {s}')
        return None


def serialize(node):
    return json.dumps(node, cls=NodeEncoder)


def deserialize(s):
    return json.loads(s, cls=NodeDecoder)


if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert (deserialize(serialize(node)).left.left.val == 'left.left')
