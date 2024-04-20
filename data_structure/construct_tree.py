# Import the required libraries
# Define a function to construct the tree from the flat list of nodes
def construct_tree(nodes):
    # Create a dictionary to store nodes by their IDs for easy lookup
    node_dict = {node['id']: node for node in nodes}

    # Initialize the root node
    root = None

    # Iterate over each node
    for node in nodes:
        # If the node has no parent (parent_id is None), it's the root node
        if node['parent_id'] is None:
            root = node
        else:
            # Get the parent node from the dictionary using parent_id
            parent = node_dict.get(node['parent_id'])
            if parent:
                # Ensure 'children' key exists in the parent node
                parent['children'] = parent.get('children', [])
                # Add the current node as a child of its parent
                parent['children'].append(node)
            else:
                # Handle the case where the parent node doesn't exist
                print(
                    f"Parent node with id {node['parent_id']} not found for node {node}")

    return root


# Sample data
nodes = [
    {'id': 0, 'name': 'jixin', 'parent_id': None},
    {'id': 1, 'name': 'security', 'parent_id': 0},
    {'id': 2, 'name': 'accounting', 'parent_id': 0},
    {'id': 3, 'name': 'nan_hai', 'parent_id': 0},
    {'id': 4, 'name': 'office', 'parent_id': 3},
    {'id': 5, 'name': 'team1', 'parent_id': 3},
    {'id': 6, 'name': 'CQ_north', 'parent_id': 0},
    {'id': 7, 'name': 'office', 'parent_id': 6},
    {'id': 8, 'name': 'team1', 'parent_id': 6},
    {'id': 9, 'name': 'team1-1', 'parent_id': 8},
    {'id': 10, 'name': 'team1-2', 'parent_id': 8},
    {'id': 11, 'name': 'jiu_long_po', 'parent_id': 0},
    {'id': 12, 'name': 'office', 'parent_id': 11}
]

# Construct the tree
tree = construct_tree(nodes)

# Print the tree
print(tree)
