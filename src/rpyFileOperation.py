"""
    Rpy文件操作
"""

import os
import typing

class RpyFileOperation(object):
    def __init__(self, path: str):
        self.path = path

    def writeDialog(self, char: str, dial: str): #TODO char应为对应角色在chara.rpy文件中对应映射名,暂用test替代
        with open(f"{self.path}/rpy/script.rpy", "w", encoding="utf-8") as f:
            f.write(f"{char} \"{dial}\"")
