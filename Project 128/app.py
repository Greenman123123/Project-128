from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(URL)
soup = bs(page.text,'html.parser')

star_data = soup.find_all('table',{"class":"wikitable sortable"})
total_data = len(star_data)

temp_list = []

table_rows = star_data[1].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]

print(temp_list)

for i in range(1,len(temp_list)):
    
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

headers = ['Star_name','Distance','Mass','Radius']  
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

df2.to_csv('dwarf_stars.csv', index=True, index_label="id")