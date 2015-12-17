import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')
root = tree.getroot()

print "root.tag: ", root.tag
print "root.attrib: ", root.attrib


print "Indexing into root[0][1].text"

print root[0][1].text
print root[0][4].text


print "Printing tag and attribute for each child in root"

for child in root:
  print child.tag, child.attrib
  print "Just country name"
  print child.attrib['name']
  #print child[0].text

print "Printing attribute for each neighbor"

for neighbor in root.iter('neighbor'):
  print neighbor.attrib


print "Printing each year"

for year in root.iter('year'):
  print year.text


print "Printing each child, and the root of each child"

for child in root:
  print child
  #for k, v in child.iteritems():
  #  print k, v


print "Printing name and rank of each country"

for country in root.findall('country'):
  rank = country.find('rank').text
  name = country.get('name')
  print name, rank

print "Printing name and rank of each country again?"

for country in root:
  rank = country.find('rank').text
  name = country.get('name')
  print name, rank


print "Everything"

for child in root:
  for grandkid in child:
    print grandkid.items()

print "Everything different way"

for something in root.iter():
  print something





