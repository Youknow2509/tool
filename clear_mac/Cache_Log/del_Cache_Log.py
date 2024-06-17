import os
import shutil

# Đường dẫn đến tệp chứa danh sách các thư mục cần xóa
file_path = 'fileRm.txt'

def delete_directories_from_file(file_path):
    with open(file_path, 'r') as file:
        directories = file.readlines()
        
    for directory in directories:
        directory = directory.strip()  # Loại bỏ ký tự xuống dòng và khoảng trắng
        if os.path.isdir(directory):
            try:
                shutil.rmtree(directory)
                print(f"Deleted: {directory}")
            except Exception as e:
                print(f"Failed to delete {directory}: {e}")
        else:
            print(f"Not a directory: {directory}")

# Xóa các thư mục được liệt kê trong tệp
delete_directories_from_file(file_path)
