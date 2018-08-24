# -*- coding:utf-8 -*-

import xml.dom
import xml.dom.minidom


# create a simple element
def create_element_node(doc, tag, attr):

    element_node = doc.createElement(tag)
    text_node = doc.createTextNode(attr)
    element_node.appendChild(text_node)

    return element_node


# add a child node
def create_child_node(doc, tag, attr, parent_node):
    child_node = create_element_node(doc, tag, attr)
    parent_node.appendChild(child_node)


# create pascal voc object node
def create_object_node(doc, attrs, box):
    object_node = doc.createElement('object')
    create_child_node(doc, 'name', box[0], object_node)
    create_child_node(doc, 'pose', attrs['pose'], object_node)
    create_child_node(doc, 'truncated', attrs['truncated'], object_node)
    create_child_node(doc, 'difficult', attrs['difficult'], object_node)

    bndbox_node = doc.createElement('bndbox')
    create_child_node(doc, 'xmin', box[1], bndbox_node)
    create_child_node(doc, 'ymin', box[2], bndbox_node)
    create_child_node(doc, 'xmax', box[3], bndbox_node)
    create_child_node(doc, 'ymax', box[4], bndbox_node)
    object_node.appendChild(bndbox_node)

    return object_node


# create xml file
def create_xml_file(anno_file, attrs):

    my_dom = xml.dom.getDOMImplementation()
    doc = my_dom.createDocument(None, attrs['root'], None)

    root_node = doc.documentElement

    create_child_node(doc, 'folder', attrs['folder'], root_node)

    create_child_node(doc, 'filename', attrs['image_name'], root_node)

    source_node = doc.createElement('source')
    create_child_node(doc, 'database', attrs['database'], source_node)
    create_child_node(doc, 'annotation', attrs['annotation'], source_node)
    create_child_node(doc, 'image', 'flickr', source_node)
    create_child_node(doc, 'flickrid', 'NULL', source_node)
    root_node.appendChild(source_node)

    owner_node = doc.createElement('owner')
    create_child_node(doc, 'flickrid', 'NULL', owner_node)
    create_child_node(doc, 'name', attrs['author'], owner_node)
    root_node.appendChild(owner_node)

    size_node = doc.createElement('size')
    create_child_node(doc, 'width', attrs['width'], size_node)
    create_child_node(doc, 'height', attrs['height'], size_node)
    create_child_node(doc, 'depth', attrs['depth'], size_node)
    root_node.appendChild(size_node)

    create_child_node(doc, 'segmented', attrs['segmented'], root_node)

    for box in attrs['boxes']:
        object_node = create_object_node(doc, attrs, box)
        root_node.appendChild(object_node)

    write_xml_without_head(doc, anno_file)


def write_xml_without_head(doc, file):

    tmpfile = open('tmp.xml', 'w')
    doc.writexml(tmpfile, addindent=' ' * 4, newl='\n', encoding='utf-8')
    tmpfile.close()

    fin = open('tmp.xml')
    fout = open(file, 'w')
    lines = fin.readlines()

    for line in lines[1:]:
        if line.split():
            fout.writelines(line)

    fin.close()
    fout.close()
