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

country = df['Name']
population = df['Population']
label=list(population)

warna = "Blue Orange Green Red Purple Brown Pink Grey Black Cyan Blue".split()

plt.figure(figsize=(15,6))
plt.bar(country, population, align='center', data=population, color=(warna))
plt.xticks(country, rotation=45)
plt.xlabel('Country')
plt.ylabel('Population x 100jt jiwa')
plt.title('Asean Population')
plt.tight_layout()
for i in range(len(country)):
    plt.text(country[i],population[i]+1000,population[i])

plt.show()