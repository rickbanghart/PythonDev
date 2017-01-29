import mysql.connector
import csv
from Tkinter import Tk, Frame, BOTH

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
        
        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=1)
        
def to_hex(num):
    num = int(num)
    if num < 16:
        return '0' + str(hex(num))[-1:]
    else:
        return str(hex(num))[-2:]
            
def save_color(red, green, blue, dmc,rgb,description,row):
    query = "INSERT INTO colorsAJ (red, green, blue, dmc, rgb, description, row) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    data = (red, green, blue,dmc,rgb,description,row)
    try:
        cursor.execute(query,data)
        cnx.commit()
    except:
        print '*********'
        print query
        print data
        print '*********'
    
class MyDialect(csv.Dialect):
    strict = True
    skipinitialspace = True
    quoting = csv.QUOTE_ALL
    quotechar = '"'
    delimiter = ','
    lineterminator = '\n'
    
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='test')
cursor = cnx.cursor()

fname = '../docs/DMCFlossRGB.csv'


#root = Tk()
#root.geometry("250x150+300+300")
#app = Example(root)
#root.mainloop()

fh = open(fname,'r')
my_list = []
all_text = '';
with open(fname,'r') as fh:
    reader = csv.reader(fh)
    next(reader)
    for row in reader:
        dmc = row[0]
        description = row[1]        
        red = row[2]
        green = row[3]
        blue = row[4]
        rgb = to_hex(red) + to_hex(green) + to_hex(blue)
        rowDesc = row[6]
        print (red, green, blue, dmc,rgb,description,rowDesc)
        print to_hex(red)
        save_color(red, green, blue, dmc,rgb,description,rowDesc)
        print description
   

cnx.close()