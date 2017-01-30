import mysql.connector
import math
from ColorObj import *
from operator import itemgetter  
      
def to_hex(num):
    num = int(num)
    if num < 16:
        return '0' + str(hex(num))[-1:]
    else:
        return str(hex(num))[-2:]
            
def colorDistance(c1, c2):
    distance = math.sqrt(
        (c1.red - c2.red) * (c1.red - c2.red) 
        + (c1.green - c2.green) * (c1.green - c2.green) 
        + (c1.blue - c2.blue) * (c1.blue - c2.blue))
    return distance    

def closestColors(colorTuple,srcObj):
    colorsDistance = []
    for color in colorTuple:
        distance = colorDistance(color,srcObj)
        colorsDistance.append({'distance':distance,'dmc':color.colorName})
    neighbors = sorted(colorsDistance, key=itemgetter('distance'))
    return neighbors

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='test')
cursor = cnx.cursor()
query = "SELECT red, green, blue, dmc FROM colorsAJ"
cursor.execute(query)
colors = cursor.fetchall()
colorList = []
for row in colors:
    colorList.append(colorObj(row[0], row[1], row[2], row[3]))
colorTuple = tuple(colorList)

print len(colorTuple)
neighbors = closestColors(colorTuple,colorTuple[25])
print neighbors

cnx.close()