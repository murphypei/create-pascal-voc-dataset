## VOC2007数据集制作

**数据准备**

* 图片

	* jpg格式
	* 命名随意，可以包含路径

* 标注
	
    * 类似给出的output.txt形式的标注
    * 可以使用LabelPicture的标注工具来标注

**使用**

* 首先用rename_images.py来遍历保存图片的文件夹，以编号的形式命名所有图片

* 然后使用create_annotations.py来生成xml形式的VOC标注

* 使用create_imagesets.py来生成ImageSets的文件

	* 可以自己修改train、test、val的比例