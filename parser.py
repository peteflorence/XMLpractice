import xml.etree.ElementTree as ET

tree = ET.parse('plant_catalog.xml')
root = tree.getroot()

print root
print root.tag
print root.attrib

for child in root:
  print child.tag, child.attrib
  print child[0].text



print root[0][1].text

