import mysql.connector
from classes.ColorObj import *
        
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

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='test')
cursor = cnx.cursor()
query = "SELECT red, green, blue, dmc FROM colorsAJ"
cursor.execute(query)
colors = cursor.fetchall()
for row in colors:
    color_list.append(colorObj(row[0], row[1], row[2], row[3]))
print color_list

cnx.close()