__author__ = 'peteflorence'

import xml.etree.ElementTree as ET


missionXMLFile = 'indoor-mission/mission.xml'


tree = ET.parse(missionXMLFile)
root = tree.getroot()

# missionInfo is where START and GOAL locations are stored
missionInfo = root.find('missionInfo')

# Helper function that sets coordinate to 0 if not specified
def readCoordinate(cartesianLocation, coordinate):
  if cartesianLocation.attrib.get(coordinate) is None:
    return 0
  else:
    return cartesianLocation.attrib[coordinate]

# START location, parsed in Cartesian coordinates
start = missionInfo.find('start')
startLocation = start.find('location')
cartesianStartLocation = startLocation.find('cartesianLocation')

xStartMeter = readCoordinate(cartesianStartLocation, 'xMeter')
yStartMeter = readCoordinate(cartesianStartLocation, 'yMeter')
zStartMeter = readCoordinate(cartesianStartLocation, 'ZMeter')

print xStartMeter, yStartMeter, zStartMeter


# GOAL location, parsed in Cartesian coordinates
goal = missionInfo.find('goal')
goalLocationList = goal.findall('location')
for child in goalLocationList:
  if child.attrib['locationType'] == 'cartesian':
    goalLocation = child
cartesianGoalLocation = goalLocation.find('cartesianLocation')

xGoalMeter = readCoordinate(cartesianGoalLocation, 'xMeter')
yGoalMeter = readCoordinate(cartesianGoalLocation, 'yMeter')
zGoalMeter = readCoordinate(cartesianGoalLocation, 'zMeter')

print xGoalMeter, yGoalMeter, zGoalMeter