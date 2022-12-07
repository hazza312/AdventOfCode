from sys import stdin

ROOT_DIR = ()
MIN_DIR_SIZE = 100000
FS_SIZE = 70000000
UPDATE_SIZE = 30000000

def read_files(lines):
    folders = {}
    curr_path = ROOT_DIR
    
    for line in lines:
        parts = line.split()
        
        if parts[:2] == ["$", "cd"]:
            if parts[2] == '/':
                curr_path = ROOT_DIR
            elif parts[2] == '..':
                curr_path = curr_path[:-1]
            else:
                curr_path += (parts[2],)
                
            if curr_path not in folders:
                folders[curr_path] = set()
                
        elif parts[0] not in ('dir', '$'):
            folders[curr_path].add((int(parts[0]), parts[1]))

    return folders


def folder_sums(folders):
    folders = sorted(folders, key=lambda f: len(f[0]), reverse=True)
    sums = {}
   
    for folder, files in folders:
        file_sum = sum(size for size, _ in files)
        child_dir_sum = sums.get(folder, 0)
        sums[folder] = file_sum + child_dir_sum

        if folder != ROOT_DIR:
            parent = folder[:-1]
            if parent not in sums:
                sums[parent] = 0
            
            sums[parent] += sums[folder]

    return sums


folders = read_files(stdin)
sums_by_folder = folder_sums(folders.items())
folder_sums = sums_by_folder.values()        
print(sum(s for s in folder_sums if s <= MIN_DIR_SIZE))

required = sums_by_folder[ROOT_DIR] + UPDATE_SIZE - FS_SIZE
min_suitable_folder_size = min(s for s in folder_sums if s >= required)
print(min_suitable_folder_size)