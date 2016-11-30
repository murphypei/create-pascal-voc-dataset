# -*- coding:utf-8 -*-

import os

__author__ = 'peic'

_IMAGE_SETS_PATH = 'ImageSets'
_MAin_PATH = 'ImageSets\\Main'
_XML_FILE_PATH = 'Annotations'

if __name__ == '__main__':

    if os.path.exists(_IMAGE_SETS_PATH):
        print('ImageSets dir is already exists')
        if os.path.exists(_MAin_PATH):
            print('Main dir is already in ImageSets')
    else:
        os.mkdir(_IMAGE_SETS_PATH)
        os.mkdir(_MAin_PATH)

    print _MAin_PATH

    # 测试集, 总数据的50%
    f_test = open(os.path.join(_MAin_PATH, 'test.txt'), 'w')
    # 训练和验证集, 除去测试的剩余50%
    f_trainval = open(os.path.join(_MAin_PATH, 'trainval.txt'), 'w')
    # trainval中训练部分, trainval的50%
    f_train = open(os.path.join(_MAin_PATH, 'train.txt'), 'w')
    # trainval中验证集, trainval的50%
    f_val = open(os.path.join(_MAin_PATH, 'val.txt'), 'w')

    # 遍历XML文件夹
    for root, dirs, files in os.walk(_XML_FILE_PATH):
        i = 1
        j = 1
        for file in files:
            if i % 2:
                # 作为测试集
                f_test.writelines(str(file).split('.')[0] + '\n')
            else:
                # 训练和验证集
                f_trainval.writelines(str(file).split('.')[0] + '\n')
                if j % 2:
                    # 训练集
                    f_train.writelines(str(file).split('.')[0] + '\n')
                else:
                    # 验证集
                    f_val.writelines(str(file).split('.')[0] + '\n')
                j += 1
            i += 1

    f_test.close()
    f_train.close()
    f_trainval.close()
    f_val.close()