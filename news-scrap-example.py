from bs4 import BeautifulSoup
import requests
import pandas as pd

titles = []
contents = []
#define total page
total_page = 1
for i in range(1,2):
    link = requests.get("https://turnbackhoax.id/page/"+str(i)+"/")
    html = link.text
    soup = BeautifulSoup(html, "html.parser")
    for title , content in zip(soup.select('.mh-loop-content h3>a'),soup.select('.mh-excerpt>p')):
        titles.append(title.text.strip())
        contents.append(content.text.strip())
        
df = pd.DataFrame({"Title":titles,"Content":contents})
print(df)
#print(titles)
 