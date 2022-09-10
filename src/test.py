import xml.etree.cElementTree as ET
from utils.Utils import Utils
from utils.XmlToRpy import xml_to_rpy


file_path = "test/xml/demo.xml"
out_path = "test/rpy/demo.rpy"


fp = open(file_path, "r", encoding="utf8")
root = ET.fromstring(fp.read())   
fp.close()


util = Utils(root)
'''util.create_label("start", "1")
util.create_label("start2", "2")
util.create_label("start3", "3")

font_style = {
    "who_font": 'Gunshihei.ttf',
    'who_color': '#055584',
    "who_outlines": '[(absolute(1), "#ffffff", absolute(0), absolute(0))]'
}
util.create_character("甲", "a", font_style, "jia")
util.create_character("乙", "b", font_style, "yi")
util.set_cur("1")
util.add_dialogue("甲", "hello world!")
util.add_dialogue("乙", "hello world!")
util.add_dialogue("甲", "hello world!")

util.write_xml(file_path)
'''
util.set_cur('s3')
util.add_dialogue("乙", "hello world!")
util.write_xml(file_path)
xml_to_rpy(file_path, out_path)