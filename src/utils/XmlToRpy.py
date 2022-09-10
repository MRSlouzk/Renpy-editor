import xml.etree.cElementTree as ET
from xml.etree.cElementTree import Element


def xml_to_rpy(file_path, out_path):

    fp = open(file_path, "r", encoding="utf8")
    root = ET.fromstring(fp.read())   
    fp.close()

    fp = open(out_path, "w", encoding="utf8")
    # define
    for i in root[0]:
        for child in i.getchildren():
            fp.write(f'{child.text}\n\n')
    
    # body
    func_dict = {
        "dialogue": turn_dialogue,
        "video": turn_video,
        "image": turn_image,
    }
    for label in root[1]:
        if not label.getchildren():
            continue
        fp.write(f'label {label.attrib["tag"]}:\n\n')
        for child in label.getchildren():
            text = func_dict[child.tag](child)
            
            fp.write(f'\t{text}\n\n')

    fp.close()


def turn_dialogue(elem: Element) -> str:
    return elem.text

def turn_video(elem: Element) -> str:
    return elem.text

def turn_image(elem: Element) -> str:
    return elem.text
