from io import TextIOWrapper
import os


def construct_node(prev_node: object, f: TextIOWrapper):
    current_line = f.readline()
    if not current_line:
        return
    node = to_node(current_line)
    if node['indent'] > prev_node['indent']:  # child
        node['parent'] = prev_node
        prev_node['children'].append(node)
    elif node['indent'] == prev_node['indent']:  # sibling
        prev_node['parent']['children'].append(node)
        node['parent'] = prev_node['parent']
    else:  # super
        super = prev_node['parent']
        while super:
            if super['indent'] == node['indent']:
                super = super['parent']
                super['children'].append(node)
                node['parent'] = super
                break
            super = super['parent']
        if super is None:
            raise Exception('Invalid tree')
    construct_node(node, f)


def to_node(line: str) -> object:
    node = {}
    temp = line.lstrip('- ')
    indent = len(line) - len(temp)
    id, name = temp.split(' ')
    node['id'] = id
    node['name'] = name
    node['indent'] = indent
    node['parent'] = None
    node['children'] = []
    return node


f = open(os.path.join(os.path.dirname(__file__), "tree_data.txt"), "r")

root_line = f.readline()
root_node = to_node(root_line)
construct_node(root_node, f)
print(root_node)

f.close()


def BFS(root: object):
    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)
        print(node['name'].strip())
        for child in node['children']:
            queue.append(child)


print('BFS:')
BFS(root_node)


def DFS(root: object) -> None:
    stack = [root]
    while stack:
        node = stack.pop()
        print(node['id'], node['name'].strip())
        for child in node['children']:
            stack.append(child)


print("DFS:")
DFS(root_node)
