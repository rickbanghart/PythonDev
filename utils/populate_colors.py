import mysql.connector

def save_color(red, green, blue, dmc):
    query = "INSERT INTO colors (red, green, blue, dmc) VALUES (%s,%s,%s,%s)"
    data = (red, green, blue,dmc)
    cursor.execute(query,data)
    cnx.commit()

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='test')
cursor = cnx.cursor()

fname = 'DMCFlossArray.txt'
fh = open(fname,'r')
my_list = []
all_text = '';
for line in fh:
    all_text += line.rstrip()
    all_text += ','
my_list.append(eval(all_text))
colors_list = my_list[0]
for color in colors_list:
    red = color['r']
    green = color['g']
    blue = color['b']
    dmc = color['colorName']
    save_color(red, green, blue, dmc)

cnx.close()