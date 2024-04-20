
# Construct the tree
root = {
    "id": 0,
    "name": "jixin",
    "parent_id": None,
    "children": [
        {
            "id": 1,
            "name": "security",
            "parent_id": 0,
            "children": []
        },
        {
            "id": 2,
            "name": "accounting",
            "parent_id": 0,
            "children": []
        },
        {
            "id": 3,
            "name": "nan_hai",
            "parent_id": 0,
            "children": [
                {
                    "id": 4,
                    "name": "office",
                    "parent_id": 3,
                    "children": []
                },
                {
                    "id": 5,
                    "name": "team1",
                    "parent_id": 3,
                    "children": []
                }
            ]
        },
        {
            "id": 6,
            "name": "CQ_north",
            "parent_id": 0,
            "children": [
                {
                    "id": 7,
                    "name": "office",
                    "parent_id": 6,
                    "children": []
                },
                {
                    "id": 8,
                    "name": "team1",
                    "parent_id": 6,
                    "children": [
                        {
                            "id": 9,
                            "name": "team1-1",
                            "parent_id": 8,
                            "children": []
                        },
                        {
                            "id": 10,
                            "name": "team1-2",
                            "parent_id": 8,
                            "children": []
                        }
                    ]
                }
            ]
        },
        {
            "id": 11,
            "name": "jiu_long_po",
            "parent_id": 0,
            "children": [
                {
                    "id": 12,
                    "name": "office",
                    "parent_id": 11,
                    "children": []
                }
            ]
        }
    ]
}


def flatten_tree(node, flattened=[]):
    flattened.append(node)
    for child in node.get("children", []):
        flatten_tree(child, flattened)
    return flattened


# Flatten the tree
flattened_tree = flatten_tree(root)
for node in flattened_tree:
    print(node)
