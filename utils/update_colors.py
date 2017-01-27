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
        

def update_color(red, green, blue, dmc):
    query = "INSERT INTO colors (red, green, blue, dmc) VALUES (%s,%s,%s,%s)"
    data = (red, green, blue,dmc)
    cursor.execute(query,data)
    cnx.commit()
    
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

fname = 'DMCFlossRGB.csv'


root = Tk()
root.geometry("250x150+300+300")
app = Example(root)
root.mainloop()

#fh = open(fname,'r')
my_list = []
all_text = '';
with open(fname,'r') as fh:
    reader = csv.reader(fh)
    
    for row in reader:
        print row[0]
   

cnx.close()