from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from urllib.error import HTTPError
myurl="https://play.google.com/store/apps?hl=en"
req=urlopen(myurl)
page_1=req.read()
req.close()
page_2=soup(page_1,"html.parser")
categories=page_2.findAll("a",{"class":"r2Osbf"})
hrefs_cat=[]
names=[]
hrefs_sim=[]
for i in range(len(categories)):
    hrefs_cat.append(categories[i]["href"])
for href in hrefs_cat:
    try:
        opurl=urlopen("https://play.google.com"+href)
    except HTTPError as err:
        if err.code==404:
            Continue
        else:
            raise
    page=opurl.read()
    opurl.close()
    soup_page=soup(page,"html.parser")
    apps=soup_page.findAll("div",{"class":"WsMG1c nnK0zc"})
    similars=soup_page.findAll("a",{"class":"LkLjZd ScJHi U8Ww7d xjAeve nMZKrb id-track-click"})
    for i in range(len(similars)):
        hrefs_sim.append(similars[i]["href"])
    for hrf in hrefs_sim:
        try:
            opurl_1=urlopen("https://play.google.com"+hrf)
        except HTTPError as err:
            if err.code==404:
                Continue
            else:
                raise
        page_3=opurl_1.read()
        opurl_1.close()
        sim_soup_page=soup(page_3,"html.parser")
        sim_apps=sim_soup_page.findAll("div",{"class":"WsMG1c nnK0zc"})
        for i in range(len(sim_apps)):
            names.append(sim_apps[i]["title"])
            if len(names)>=300000:
                break
            else:
                print("app_name; "+sim_apps[i]["title"])
names_set=set(names)
print(len(names))
print(len(names_set))
