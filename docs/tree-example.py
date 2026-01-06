"""
dp dir path codes
0 none means is file
1-99 documentation
100-199 data locations
    100-109 raw
    110-119 interim
    120-129 processed
    130-139 external
    140-189 other data drops
    190-199 databases

"""
type Tree = dict[str, int | Tree]

tree = {
    "data": {
        "raw": 100,
        "interim": 110,
        "processed": 120,
        "external": 130,
    },
}

# want trie (prefix tree)
tree = {
    ("data", 1): {
        "raw": 100,
        "interim": 110,
        "processed": 120,
        "external": 130,
    },
}

# typed node eg
tree = {
    "name": "root",
    "id": 0,
    "children": [
        {
            "name": "data",
            "id": 1,
            "type": "directory",
            "children": [
                {
                    "name": "raw",
                    "id": 100,
                    "type": "file",
                },
                {
                    "name": "interim",
                    "id": 110,
                    "type": "file",
                },
            ],
        }
    ],
}


"""
standardise trees
hash trees to compare other trees
order tree alphabetically
"""
