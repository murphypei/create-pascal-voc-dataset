# -*- coding:utf-8 -*-

import os

__author__ = 'peic'

'''
设置trainval和test数据集包含的图片
'''

# ImageSets文件夹
_IMAGE_SETS_PATH = 'ImageSets'
_MAin_PATH = 'ImageSets\\Main'
_XML_FILE_PATH = 'Annotations'


# Train数据集编号
_TRAIN_NUMBER = 614

if __name__ == '__main__':

    # 创建ImageSets数据集
    if os.path.exists(_IMAGE_SETS_PATH):
        print('ImageSets dir is already exists')
        if os.path.exists(_MAin_PATH):
            print('Main dir is already in ImageSets')
    else:
        os.mkdir(_IMAGE_SETS_PATH)
        os.mkdir(_MAin_PATH)

    f_test = open(os.path.join(_MAin_PATH, 'test.txt'), 'w')
    f_train = open(os.path.join(_MAin_PATH, 'trainval.txt'), 'w')

    # 遍历XML文件夹
    for root, dirs, files in os.walk(_XML_FILE_PATH):
        print len(files)
        for f in files:
            i = int(f.split('.')[0])
            if i > _TRAIN_NUMBER:
                f_test.write(f.split('.')[0] + '\n')
            else:
                f_train.write(f.split('.')[0] + '\n')

            i += 1

    f_test.close()
    f_train.close()