## VOC2007数据集制作(以INRIA数据集为例)

**使用**

1. 首先在`create_JPEGImages.py`中设置好：

    * `TRAIN_ANNO` : Train数据的标注文件夹路径 
    * `TEST_ANNO` : Test数据的标注文件夹路径 
    * `ORIGIN_IMAGES` : 图片的文件夹路径 

* 使用`create_JPEGImages.py`来遍历，生成`JPEGImages`文件夹，图片名称为VOC2007的6位编号，JPEG格式。将提取的标注信息保存在`output.txt`文件中

2. 使用`create_Annotations.py`文件，利用1中生成`output.txt`标注信息来生成VOC2007格式的`xml`文件，保存在`JPEGImages`文件夹中
3. 使用`create_ImageSets.py`来生成`ImagesSets`文件夹
4. 将生成的`JPEGImages`，`JPEGImages`，`ImagesSets`替换掉VOC2007中的五个文件夹，制作完成


**注意**

* 不同数据集标注格式、路径均不一样，需要适当修改
* 不同数据集的`trainval.txt`和`test.txt`也不一样，需要自己设置