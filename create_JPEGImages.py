# -*- coding:utf-8 -*-

__auth__ = 'peic'

'''
读取图片，重命名图片，读取gt，生成output文件
'''

import re
import os
from PIL import Image

# 图片名称起始编号
name_number = 1
# 图片名称编号长度
name_length = 6

# Train annotations 位置
TRAIN_ANNO = r'G:\pycharm\INRIA2VOC\INRIADATA\original_images\Train\annotations'

# Test annotations 位置
TEST_ANNO = r'G:\pycharm\INRIA2VOC\INRIADATA\original_images\Test\annotations'

# 图片所在位置
ORIGIN_IMAGES = r'G:\pycharm\INRIA2VOC\INRIADATA\original_images'

# 输出文件
fout = open('output.txt', 'w')

# 创建另存为的文件夹
if not os.path.exists('JPEGImages'):
    os.mkdir('JPEGImages')
    print "mkdir donw"


# 定义处理函数
def process(anno_path):
    train_anno_files = os.listdir(anno_path)
    for anno in train_anno_files:
        with open(os.path.join(anno_path, anno), 'r') as f:
            for line in f:
                line = line.strip()
                # 匹配图片名称
                sg = re.search(r'Image filename : "([\w\d/_.]+)"', line)
                if sg:
                    image_filename =  sg.group(1)
                    #print image_filename

                    # 构建新的图片名称
                    global name_number
                    new_name_str = (name_length - len(str(name_number))) * '0' + str(name_number) + ".jpg"
                    image = Image.open(os.path.join(ORIGIN_IMAGES, image_filename))
                    image.save(os.path.join("JPEGImages", new_name_str), 'jpeg')
                    name_number += 1

                # 匹配bbox坐标
                sg = re.search('\((\d+), (\d+)\) - \((\d+), (\d+)\)$', line)
                if sg:
                    bbox = [sg.group(i) for i in range(1,5)]
                    if new_name_str:
                        fout.write(new_name_str + ' ' + ' '.join(bbox) + '\n')

    print "process \n{} \ndone".format(anno_path)



# 处理Train
process(TRAIN_ANNO)
print name_number

# 处理Test
process(TEST_ANNO)
print name_number


fout.close()








