from typing import List, Dict


class Utils:

    def __init__(self, data_linked_obj, pos):
        self._data_linked_list = data_linked_obj
        self.pos = pos

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

    def add_transform(self, type_list: List(str), **args) -> bool:
        pass

