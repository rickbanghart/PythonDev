import mysql.connector
import math
from ColorObj import *

#class colorObj():
#    def __init__(self, red, green, blue, colorName):
#        self.red = red
#        self.green = green
#        self.blue = blue
#        self.colorName = colorName
  

def colorDistance(c1, c2):
    distance = math.sqrt(
        (c1.red - c2.red) * (c1.red - c2.red) 
        + (c1.green - c2.green) * (c1.green - c2.green) 
        + (c1.blue - c2.blue) * (c1.blue - c2.blue))
    return distance

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='test')
cursor = cnx.cursor()

query = "SELECT red, green, blue, dmc, color_id FROM colors"
cursor.execute(query)
rows = cursor.fetchall()
color_list = []

for row in rows:
    color_list.append(colorObj(row[0], row[1], row[2], row[3]))

for i in range(len(color_list) - 1):
    distance = colorDistance(color_list[i],color_list[i + 1])
    if (distance == 0):
        print "distance is zero for " 
        print color_list[i].colorName
        print color_list[i + 1].colorName
cnx.close()