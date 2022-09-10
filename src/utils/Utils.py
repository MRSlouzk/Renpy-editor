import xml.etree.cElementTree as ET
from xml.etree.cElementTree import Element
from typing import List, Dict, Union
from utils.CustomException import InvalidPosition, PositionOutOfIndexError


def get_pos(root, pos):
    global pos_dict
    pos_dict = {
            "header": 0,
            "footer": -1 if len(root[1].getchildren()) > 0 else 0,
        }

    return pos_dict[pos]

class Utils:

    def __init__(self, root: Element):
        self.__root: Element = root
        self.__cur: Element = self.__root[1]
        self.__pos: int = 0

    def __set_cur(self, pos: Union[str, int] = "footer"):
        try:
            self.__pos = get_pos(self.__root, pos) if type(pos) is str else pos
        except KeyError:
            raise InvalidPosition(f"\'{pos}\' is not a valid position;" \
                                  f"valid pos: {','.join(i for i in pos_dict.keys())}")
        try:
            self.__cur: Element = self.__root[1][pos]
        except IndexError:
            raise PositionOutOfIndexError(f"child index '{self.pos}' out of range;" \
                                          f"(0-{len(self.__root[1].getchildren())})")

    def __set_tag(self, et_sub, tag_dict: Dict[str, str]):
        for key in tag_dict.keys():
            et_sub.set(key, tag_dict[key])

    def __get_character_tag(self, character_name: str) -> str:
        for i in self.__root[0][0].getchildren():
            if (attrib_dict := i.attrib)["character_name"] == character_name:
                return attrib_dict["character_tag"]
        raise Exception(f"'{character_name}' is not existing!")

    def reset_cur(self):
        '''
        将游标返回到body层级
        '''
        self.__cur = self.__root[1]

    def set_cur(self, name: str) -> bool:
        '''
        将光标设置到指定name标签的层级
        '''
        for i in range(len(child_list := self.__root[1].getchildren())):
            if child_list[i].attrib["name"] == name:
                self.__set_cur(i)
                return True
        raise Exception(f"'{name}' is not existing!")
        
    def show(self):
        '''
        在控制台输出当前xml内容(调试用)
        '''
        ET.dump(self.__root)

    def write_xml(self, out_path: str):
        xml = ET.ElementTree(self.__root)
        xml.write(out_path)

    def add_dialogue(self, character_name: str, dialogue: str) -> bool:
        '''
        添加对话
        '''
        dialogue_elem = ET.SubElement(self.__cur, "dialogue")
        tag_dict = {
            "character_name": character_name
        }
        self.__set_tag()
        dialogue_elem.text = f'{self.__get_character_tag(character_name)} "{dialogue}"'

    def add_video(self, video_path: str) -> bool:
        return True

    def add_choice(self, choice_params_dict: Dict[str, str]) -> bool:
        return True

    def create_label(self, label_tag: str, label_name: str) -> bool:
        '''
        创建一个label
        :params label_tag: renpy中label TAG:
        :params label_name: 识别名
        :generate <label name=label_name>label_tag</label>  
        '''
        label_elem = ET.SubElement(self.__cur, "label")
        tag_dict = {
            "name": label_name,
        }
        text = label_tag
        self.__set_tag(label_elem, tag_dict)
        label_elem.text = text
        return True

    def create_character(self, character_name: str, character_tag: str,
                            font_style: Dict[str, str], painting_tag: str) -> bool:
        '''
        创建角色, 储存在config/characters中
        :params character_name: 角色识别名
        :params character_tag: renpy中变量名
        :params painting_tag: 立绘前缀 
        '''
        character_elem = ET.SubElement(self.__root[0][0], "character")
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
        self.__set_tag(character_elem, tag_dict)
        character_elem.text = text
        return True

    def add_transform(self, type_list: List[str], **args) -> bool:
        return True
