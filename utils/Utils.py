from typing import List, Dict, Tuple, Union
from CustomException import InvalidPosition


pos_dict = {
            "header": [0],
            "footer": [-1],
        }

class Utils:
    
    def __init__(self, xml_data_obj, pos: Union[str, List[int], Tuple[int]] = "footer"):
        try:
            self.pos = pos_dict[pos] if type(pos) is str else pos
        except KeyError:
            raise InvalidPosition(f"\'{pos}\' is not a valid position;valid pos: {','.join(i for i in pos_dict.keys())}")
        
        self.__xml_data_obj = xml_data_obj

    def add_dialogue(self, character_name: str, dialogue: str) -> bool:
        pass

    def add_video(self, video_path: str) -> bool:
        pass

    def add_choice(self, choice_params_dict: Dict[str, str]) -> bool:
        pass

    def create_label(self, label_tag: str, label_name: str) -> bool:
        pass

    def create_character(self, character_name: str, character_tag: str,
                            font_style_path: str, name_tag: str = "default") -> bool:
        pass

    def add_transform(self, type_list: List[str], **args) -> bool:
        pass

    def get_data_linked_list(self):
        return self._data_linked_list
