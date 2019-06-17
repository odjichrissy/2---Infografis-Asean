import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'hiddenhand12',
    database = 'world'
)

df = pd.read_sql('select * from country where Region="Southeast Asia" order by Name', con = mydb)

labels = df['Name']
sizes = df['SurfaceArea']
warna = "Blue Orange Green Red Purple Brown Pink Grey Black Cyan Blue".split()

plt.pie(sizes, labels=labels, colors=warna, autopct='%1.1f%%', textprops={'color':'w'})
plt.title('Asean Country Surface Area')


plt.show()