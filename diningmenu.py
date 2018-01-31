

#import beautifulsoup 
from bs4 import BeautifulSoup
from urllib.request import urlopen

html=urlopen('#address')
source=html.read()
html.close()


soup=BeautifulSoup(source,"lxml")
print(soup.prettify())
div_contents = soup.find("div","contents")

print(div_contents.prettify())

table = div_contents.find_all("table")
print(table[0])
menu_table=table[0]
trs=menu_table.find_all('tr')

sun_trs=trs[1]
sun_tds=sun_trs.find_all('td')
sun_mon=sun_tds[1].get_text(strip=True)
