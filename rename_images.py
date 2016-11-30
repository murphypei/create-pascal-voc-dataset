
# _*_ coding:utf-8 _*_
# 
from PIL import Image
import os
import re
import sys

if __name__ == "__main__":

    if(len(sys.argv) != 2):
        print("args is not 2!")
        sys.exit(1);

    BASE_PATH = sys.argv[1];
    print(BASE_PATH)

    # os.walk返回一个walk对象，是一个三元组
    for rootpath, dirnames, filenames in os.walk(BASE_PATH):
        name_number = 1
        name_length = 6
        for filename in filenames:
            if(re.match("^(\d*).jpg", filename)):
                name_str = (name_length - len(str(name_number))) * '0' + str(name_number) + ".jpg"
                print name_str, '\n'
                name_number = name_number + 1
                image = Image.open(os.path.join(BASE_PATH, filename))
                image.save(os.path.join(BASE_PATH, name_str), 'jpeg')