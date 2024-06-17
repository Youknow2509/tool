import os
import time
from datetime import datetime, timedelta

def find_files_last_opened_older_than(root_directory, months):
    current_time = time.time()
    cutoff_time = current_time - (months * 30 * 24 * 60 * 60)  # Chuyển đổi tháng thành giây

    matching_files = []
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                last_access_time = os.path.getatime(file_path)
                if last_access_time < cutoff_time:
                    matching_files.append(file_path)
            except Exception as e:
                print(f"Could not access {file_path}: {e}")

    return matching_files

# Chỉ định thư mục gốc và số tháng
root_dir = '/'  # Đặt đường dẫn thư mục cần quét ở đây
months = 1  # Số tháng

# Tìm và in các tệp phù hợp
matching_files = find_files_last_opened_older_than(root_dir, months)
for file in matching_files:
    print(file)
