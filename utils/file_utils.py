import os
import shutil


def create_if_not_exists(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def copy_file_to_dir(src_file, dst_dir):
    if os.path.isfile(src_file):
        shutil.copy(src_file, dst_dir)


def copy_file(src_file, dst_dir, new_name):
    if os.path.isfile(src_file):
        shutil.copy(src_file, dst_dir)
        old_name = src_file.strip().split(os.sep)[-1]
        os.rename(os.path.join(dst_dir, old_name), os.path.join(dst_dir, new_name))


def file_count(dir):
    count = 0
    for root, dirs, files in os.walk(dir):
        for _ in files:
            count += 1
    return count


if __name__ == "__main__":
    print(file_count("."))
