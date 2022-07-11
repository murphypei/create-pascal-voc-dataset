## 创建 PASCAL VOC 2007 数据集

本项目主要是将其他目标检测数据集转换成 Pascal Voc 2007 的格式，方便直接用于现有很多开源目标检测代码。

本项目以 INRIA 行人检测数据集为例。

### 用法

1. 根据你的标注数据生成你的 annotation 文件，文件名可以随意。
2. annotation 文件格式如下：
   1. 每一行表示一张图片的标注信息，目标可以有多个，`<文件绝对路径> [<目标1 类型> <目标1 x_min> <目标1 y_min> <目标1 x_max> <目标1 y_max> ...]`。box 坐标是左上角和右下角 4 个坐标（和 Pascal Voc 一致）。
   2. 可以编写 preprocess 文件，将你的数据集标注数据转换成 2 展示的标注格式。这里已经放置了 INRIA 数据集标注数据的处理，可以作为参考 `preprocess/inria_preprocess.py`。
3. 配置你的数据集信息，主要是配置 annotation 的路径。因为 Pascal Voc 的标注很仔细，包含了 `pose`，`segmented`，`difficult`，`truncated` 等多种信息，一般数据集可以不用配置这些，使用默认就行，然后运行 build。
   1. 这一步可以参考 `examples/inria_example.py`。

### 示例

假如我已经下载了 INRIA 数据集，运行：

```sh
python preprocess/inria_preprocess.py /path/to/INRIAPerson
python examples/inria_example.py /path/to/INRIAPerson /path/to/output
```

第一个命令是预处理，得到 annotation 文件，第二个就是生成 Pascal Voc 2007 格式的数据集。

**有任何问题都可以通过中英文提 issue，我看到就会及时解决**。