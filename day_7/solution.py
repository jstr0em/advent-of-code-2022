class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size


class Dir:
    def __init__(self, name, parent=None) -> None:
        self.name = name
        self.content = []
        self.parent = parent

    def __repr__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_parent(self):
        return self.parent

    def add_content(self, item):
        #print("Adding " + item.get_name() + " to " + self.get_name())
        if isinstance(item, Dir) or isinstance(item, File):
            self.content.append(item)

    def get_content(self):
        return self.content

    def is_empty(self):
        return len(self.content) == 0

    def find(self, name):
        #print("Looking for " + name + " in " + self.get_name())
        if name == "..":
            return self.parent
        for item in self.get_content():
            if item.get_name() == name:
                return item
        return None

    def get_size(self):
        size = 0
        for item in self.get_content():
            size += item.get_size()
        return size

    def get_dirs(self):
        dirs = []
        for item in self.get_content():
            if isinstance(item, Dir):
                dirs.append(item.get_dirs())

        return self.get_name()


def get_dirs(tree):
    dirs = []
    dirs_to_traverse = [tree]

    while dirs_to_traverse:
        current_dir = dirs_to_traverse.pop()
        dirs.append(current_dir)
        for item in current_dir.get_content():
            if isinstance(item, Dir):
                dirs_to_traverse.append(item)

    return dirs


def create_tree(terminal_output):
    terminal_output = [line.split(" ")
                       for line in terminal_output.splitlines()]

    tree = Dir("/")
    current_dir = tree
    for line in terminal_output[1:]:
        if line[0] == "$":  # Command
            if line[1] == "cd":
                current_dir = current_dir.find(line[2])
        elif line[0] == "dir":
            current_dir.add_content(Dir(line[1], parent=current_dir))
        elif line[0].isdigit():
            current_dir.add_content(File(line[1], int(line[0])))

    return tree


def test_solution():
    test_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
    test_tree = create_tree(test_input)

    dir_sizes = {dir: dir.get_size()
                 for dir in get_dirs(test_tree) if dir.get_size() <= 100000}
    total_size = sum(dir_sizes.values())
    assert (total_size == 95437)
    assert (test_tree.get_size() == 48381165)


test_solution()


def solution():
    with open("input.txt", "r") as f:
        terminal_output = f.read()

    tree = create_tree(terminal_output)

    total_space = 70000000
    desired_space = 30000000

    dir_sizes = {dir: dir.get_size() for dir in get_dirs(tree)
                 if dir.get_size() <= 100000}
    total_size = sum(dir_sizes.values())

    sorted_dir = {dir.get_name(): dir.get_size() for dir in get_dirs(tree)}
    current_space = total_space - sorted_dir["/"]
    space_to_free_up = abs(current_space - desired_space)

    min_dir = {dir: size-space_to_free_up for dir, size in sorted_dir.items()}

    min_dir = dict(sorted(min_dir.items(), key=lambda item: item[1]))

    print("Solution 1:", total_size)
    print("Solution 2:", sorted_dir["dqbnbl"])


solution()
