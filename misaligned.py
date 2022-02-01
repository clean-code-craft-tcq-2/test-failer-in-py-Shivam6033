major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]


def get_color_map(delimiter: str):
    color_map = ""
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map += f'{i * 5 + j + 1}{delimiter}{major}{delimiter}{minor}\n'
    return color_map


def print_color_map(delimiter: str):
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j + 1}{delimiter}{major}{delimiter}{minor}')


print_color_map(delimiter='\t\t')
result = get_color_map(delimiter=',')
assert('1,White,Blue' == result.split('\n')[0])
result = get_color_map(delimiter='|')
assert('1|White|Blue' == result.split('\n')[0])

