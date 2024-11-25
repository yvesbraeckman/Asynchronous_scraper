def find_value_in_tree(tree, value, path="top level"):
    if tree["value"] == value:
        return path

    for index, child in enumerate(tree["children"]):
        child_path = f"{path} → kind op index {index}"
        result = find_value_in_tree(child, value, child_path)
        if result:
            return result

    return None


# Boomstructuur
tree = {
    "children": [
        {"children": [], "value": 74},
        {
            "children": [
                {
                    "children": [
                        {"children": [], "value": 44},
                        {"children": [], "value": 35},
                        {"children": [], "value": 67},
                        {"children": [], "value": 66},
                    ],
                    "value": 60,
                },
                {
                    "children": [
                        {"children": [], "value": 21},
                        {"children": [], "value": 47},
                        {"children": [], "value": 71},
                    ],
                    "value": 36,
                },
                {
                    "children": [
                        {"children": [], "value": 25},
                        {"children": [], "value": 18},
                    ],
                    "value": 24,
                },
            ],
            "value": 89,
        },
        {
            "children": [
                {
                    "children": [
                        {"children": [], "value": 75},
                        {"children": [], "value": 73},
                    ],
                    "value": 36,
                },
                {
                    "children": [
                        {"children": [], "value": 55},
                        {"children": [], "value": 9},
                    ],
                    "value": 78,
                },
            ],
            "value": 80,
        },
        {
            "children": [
                {
                    "children": [
                        {"children": [], "value": 35},
                        {"children": [], "value": 26},
                        {"children": [], "value": 100},
                        {"children": [], "value": 75},
                        {"children": [], "value": 45},
                    ],
                    "value": 78,
                },
                {
                    "children": [
                        {"children": [], "value": 41},
                        {"children": [], "value": 45},
                    ],
                    "value": 9,
                },
                {
                    "children": [
                        {"children": [], "value": 40},
                        {"children": [], "value": 28},
                    ],
                    "value": 12,
                },
            ],
            "value": 9,
        },
    ],
    "value": 55,
}


print(find_value_in_tree(tree, 47))

