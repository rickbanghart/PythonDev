import mysql.connector
import Tkinter
top = Tkinter.Tk()
top.mainloop()
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='test')
cnx.get_warnings = True
cursor = cnx.cursor()
query = "INSERT INTO colors (red, green, blue, dmc) VALUES (%s,%s,%s,%s)"
data = (1, 2, 3,'104')
cursor.execute(query,data)
crs_warnings = cursor.fetchwarnings()
print crs_warnings
cnx.commit()
cnx.close()