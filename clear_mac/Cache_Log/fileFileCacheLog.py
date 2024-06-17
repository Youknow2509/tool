import os

# Chỉ định thư mục gốc và các tên thư mục cần tìm
root_dir = '/'  # Thư mục hiện tại
target_dirs = {'log', 'cache', 'logs', 'caches'}  # Các tên thư mục cần tìm
file_name = 'fileRm.txt'

def find_directories_with_specific_names(root_directory, target_names):
    matching_directories = []
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for dirname in dirnames:
            if dirname.lower() in target_names:
                d = os.path.join(dirpath, dirname)
                print(d)
                matching_directories.append(d)
    return matching_directories

def save_to_file(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write(f"{line}\n")

# Tìm và in các thư mục phù hợp
matching_dirs = find_directories_with_specific_names(root_dir, target_dirs)
# Save to file 
save_to_file(file_name, matching_dirs)