import re

class Directory:

    def __init__(self, name, parent_dir):
        self.name = name
        self.parent_dir = parent_dir
        self.child_dirs = []
        self.file_size = 0
    
    def __str__(self):
        return self.name

    def add_child_dir(self, child_dir):
        self.child_dirs.append(child_dir)
    
    def add_file_size(self, file_size):
        self.file_size += file_size

    def get_total_size(self):
        total_size = self.file_size
        for child in self.child_dirs:
            total_size += child.get_total_size()
        return(total_size)


curr_dir = Directory('/', None)
dir_list = [curr_dir]

with open("07/input.txt") as file:
    lines = file.readlines()
    for line in lines:

        # dir (add child dir)
        dir_line = re.match(r"^dir ([a-z]+)", line)
        if dir_line:
            new_dir = Directory(dir_line.group(1), curr_dir)
            curr_dir.add_child_dir(new_dir)
            dir_list.append(new_dir)

        # file (add file size)
        file_line = re.match(r"^([0-9]+)", line)
        if file_line:
            curr_dir.add_file_size(int(file_line.group(1)))

        # cd (cd into dir, it should already exit!)
        cd_line = re.match(r"^\$ cd ([a-z]+)", line)
        if cd_line:
            dir_name = cd_line.group(1)
            curr_dir = next((obj for obj in curr_dir.child_dirs if obj.name == dir_name), None)

        # cd ..  (directory up)
        dir_up_line = re.match(r"^\$ cd \.\.", line)
        if dir_up_line:
            curr_dir = curr_dir.parent_dir

# result
total_size = sum(dir.get_total_size() for dir in dir_list if dir.get_total_size() <= 100000)
print(total_size)
