import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '************',
    database = 'world'
)

df = pd.read_sql('select * from country where Region="Southeast Asia" order by Name', con = mydb)

country = df['Name']
gnp = df['GNP']

warna = "Blue Orange Green Red Purple Brown Pink Grey Black Cyan Blue".split()

plt.figure(figsize=(15,6))
plt.bar(country, gnp, align='center', color=(warna))
plt.xticks(country, rotation=45)
plt.xlabel('Country')
plt.ylabel('Gross National Product')
plt.title('Pendapatan Bruto Nasional ASEAN')
for i in range(len(country)):
    plt.text(country[i],gnp[i],gnp[i])
plt.tight_layout()

plt.show()