tree_str = '''
- 0 jixin
- - 1 security
- - 2 accounting
- - 3 nan_hai
- - - 4 office
- - - 5 team1
- - 6 CQ_north
- - - 7 office
- - - 8 team1
- - - - 9 team1-1
- - - - 10 team1-2
- - 11 jiu_long_po
- - - 12 office
'''

tree_str_list = tree_str.split('\n')[1:-1]
nodes = []
for line in tree_str_list:
    id, name = (line.lstrip('- ').split(' '))
    print(line)
    indent = len(line) - len(line.lstrip('- '))
    nodes.append({'id': id, 'name': name, 'indent': indent})


def construct_tree(nodes: list):
    if not tree_str_list:
        return
    current_node = tree_str_list.pop(0)
    next_node = None
    if len(tree_str_list) > 0:
        next_node = tree_str_list[0]

    if next_node == None:
        return

    current_indent = len(current_node) - len(current_node.lstrip('- '))
    next_indent = len(next_node) - len(next_node.lstrip('- '))

    id, name = (current_node.lstrip('- ').split(' '))
    current_object = {'id': id, 'name': name, 'children': []}
    if (current_indent < next_indent):  # child
        current_object['children'].append(next)
    elif (current_indent == next_indent):  # brother
        pass
    else:  # other level
        pass

    print(current_node.strip('- '), current_indent)
    construct_tree(tree_str_list)


# construct_tree(tree_str_list)
print(nodes)
