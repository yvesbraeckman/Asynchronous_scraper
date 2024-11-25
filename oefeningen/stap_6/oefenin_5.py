folder_hierarchy = {
    "name": "level 1 directory",
    "children": [
        {
            "name": "level 2 directory A",
            "children": [
                {"name": "level 3 directory A1", "children": []},
                {"name": "level 3 directory A2", "children": []},
            ],
        },
        {
            "name": "level 2 directory B",
            "children": [{"name": "level 3 directory B1", "children": []}],
        },
        {
            "name": "level 2 directory C",
            "children": [
                {"name": "level 3 directory C1", "children": []},
                {"name": "level 3 directory C2", "children": []},
                {"name": "level 3 directory C3", "children": []},
            ],
        },
    ],
}

def pretty_print(folder, level=0):
    print("  " * level + folder["name"])

    for child in folder.get("children", []):
        pretty_print(child, level + 1)


pretty_print(folder_hierarchy)
