import xml.etree.cElementTree as ET
from xml.etree.ElementTree import ParseError
from utils.Utils import Utils


file_path = "test/xml/demo.xml"
try:
    etree = ET.parse(file_path)
    root = etree.getroot()
except ParseError:
    meta_xml = "<root><config><characters></characters><paintings></paintings><images></images></config><body></body></root>"
    root = ET.fromstring(meta_xml)

    # print(root[1].getchildren())

util = Utils(root)
util.create_label("start", "1")
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
util.write_xml("test/xml/demo.xml")
