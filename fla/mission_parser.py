import xml.etree.ElementTree as ET

tree = ET.parse('indoor-mission/mission.xml')
root = tree.getroot()

# missionInfo is where START and GOAL locations are stored
missionInfo = root.find('missionInfo')


# START location, parsed in Cartesian coordinates
start = missionInfo.find('start')
# for child in start:
#   print child.tag, child.attrib

startLocation = start.find('location')
# for child in startLocation:
#   print child.tag, child.attrib

cartesianStartLocation = startLocation.find('cartesianLocation')
xStartMeter = cartesianStartLocation.attrib['xMeter']
yStartMeter = cartesianStartLocation.attrib['yMeter']
zStartMeter = cartesianStartLocation.attrib['zMeter']

print xStartMeter, yStartMeter, zStartMeter


# GOAL location, parsed in Cartesian coordinates
goal = missionInfo.find('goal')
# for child in goal:
#   print goal.tag, goal.attrib

goalLocationList = goal.findall('location')
for child in goalLocationList:
  if child.attrib['locationType'] == 'cartesian':
    cartesianGoalLocation = child


cartesianGoalLocation = cartesianGoalLocation.find('cartesianLocation')
xGoalMeter = cartesianGoalLocation.attrib['xMeter']
yGoalMeter = cartesianGoalLocation.attrib['yMeter']
#zGoalMeter = cartesianGoalLocation.attrib['zMeter']

print xGoalMeter, yGoalMeter