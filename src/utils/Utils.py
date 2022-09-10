import xml.etree.cElementTree as ET
from xml.etree.cElementTree import Element
from typing import List, Dict, Union
from utils.CustomException import PositionOutOfIndexError


class Utils:

    def __init__(self, root: Element):
        self.__root: Element = root
        self.__cur: Element = self.__root[1]
        self.__pos: List[int] = [0]

    def __set_tag(self, elem: Element, tag_dict: Dict[str, str]):
        for key in tag_dict.keys():
            elem.set(key, tag_dict[key])

    def __get_character_tag(self, character_name: str) -> str:
        for i in self.__root[0][0].getchildren():
            if (attrib_dict := i.attrib)["character_name"] == character_name:
                return attrib_dict["character_tag"]
        raise Exception(f"'{character_name}' is not existing!")

    def __generate_elem(self, elem_name: str, tag_dict: Dict[str, str] = None, text: str =None) -> bool:
        elem = ET.SubElement(self.__cur, elem_name)
        if tag_dict is not None:
            self.__set_tag(elem, tag_dict)
        if text is not None:
            elem.text = text
        return True

    # 操作类接口
    def set_cur(self, name: str) -> bool:
        '''
        将光标设置到指定name标签的层级
        '''
        for i in range(len(child_list := self.__root[1].getchildren())):
            if child_list[i].attrib["name"] == name:
                try:
                    self.__cur: Element = self.__root[1][i]
                except IndexError:
                    raise PositionOutOfIndexError(f"child index '{i}' out of range;" \
                                          f"(0-{len(self.__cur.getchildren())})")
                return True
        raise Exception(f"'{name}' is not existing!")
    
    def remove_element(self, pos) -> bool:
        return False

    def show(self):
        '''
        在控制台输出当前xml内容(调试用)
        '''
        ET.dump(self.__root)

    def write_xml(self, out_path: str):
        xml = ET.ElementTree(self.__root)
        xml.write(out_path, encoding="utf8", xml_declaration=True)

    def create_image(self, image_name: str, image_path: str) -> bool:
        self.__cur = self.__root[0][2]
        tag_dict = {
            "image_name": image_name,
            "image_path": image_path
        }
        text = f'image {image_name} = "{image_path}"'
        return self.__generate_elem(elem_name="image", tag_dict=tag_dict, text=text)

    def create_label(self, label_tag: str, label_name: str) -> bool:
        '''
        创建一个label
        :params label_tag: renpy中label TAG:
        :params label_name: 识别名
        :generate <label name=label_name>label_tag</label>  
        '''
        tag_dict = {
            "name": label_name,
            "tag": label_tag,
        }
        return self.__generate_elem(elem_name="label", tag_dict=tag_dict)

    def create_character(self, character_name: str, character_tag: str,
                            font_style: Dict[str, str], painting_tag: str) -> bool:
        '''
        创建角色, 储存在define/characters中
        :params character_name: 角色识别名
        :params character_tag: renpy中变量名
        :params painting_tag: 立绘前缀 
        '''
        self.__cur = self.__root[0][0]
        tag_dict = {
            "character_name": character_name,
            "character_tag": character_tag,
            "painting_tag": painting_tag,
        }
        params_text = ""
        for key in font_style.keys():
            params_text = f'{params_text},{key}={font_style[key]}'
        
        text = f'define {character_tag} = ' \
               f'Character("{character_name}"{params_text})'
        return self.__generate_elem(elem_name="character", tag_dict=tag_dict, text=text)
    
    def add_dialogue(self, character_name: str, dialogue: str) -> bool:
        '''
        添加对话
        '''
        tag_dict = {
            "character_name": character_name
        }
        text = f'{self.__get_character_tag(character_name)} "{dialogue}"'
        return self.__generate_elem(elem_name="dialogue", tag_dict=tag_dict, text=text)

    def add_image(self, image_name: str) -> bool:
        '''
        添加图片, 如果未提前定义会返回False
        '''
        temp_cur = self.__root[0][1]
        for child in temp_cur.getchildren():
            if child.attrib["image_name"] == image_name:
                tag_dict = {
                    "image_name": image_name
                }
                text = f"show {image_name}"
                return self.__generate_elem(elem_name="image", tag_dict=tag_dict, text=text)
        return False

    def add_video(self, video_path: str) -> bool:
        text = f"$ renpy.movie_cutscene('{video_path}')"
        return self.__generate_elem("video", text=text)

    def add_choice(self, choice_params_dict: Dict[str, str]) -> bool:
        return True

    def add_transform(self, type_list: List[str], **args) -> bool:
        return True

    # 预览类接口
    
