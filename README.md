## CREATE PASCAL VOC 2007 DATASET

Refactor all the project ! Now it's more efficient and the structure is more clear. 

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

### Usage

1. Get your dataset annotations file, parse and save it to two files `trainval_annotations.txt` and `test_annotations.txt`, file name doesn't matter.

2. Your annotations file must have the format like this:

    `image_full_path object1_class x1_min y1_min x1_max y1_max object2_class x2_min y2_min x2_max y2_max...`
    
    * You can check `examples/Train_annotation.txt` file to understand the annotation format more clearly, this is the INRIA annotations file after my processing, your annotations file should be like this.
    
    * You should write your own dataset annotation process program, I just write for INRIA dataset and you can reference it in `preprocess/inria_preprocess.py`.
    
    * If I have more time, I will write more process program, you can send your requires in issues.

3. Edit your dataset config and run file；
   
    * Check the `examples/inria_example.py` to understand how to call the `PASCALVOC07` class
    
    * Config your own information in your pascal voc dataset
    
    * Set the dataset directory, annotations file and output directory, then just run `build`, wait for your own pascal voc dataset.


### Example

* I have writen an example of the INRIA dataset:

```sh
python preprocess/inria_preprocess.py /path/to/INRIAPerson
python examples/inria_example.py /path/to/INRIAPerson /path/to/output
```

Anything can be send to issues and forgive my poor English...
