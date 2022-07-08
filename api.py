import requests
from bs4 import BeautifulSoup
import bs4
import json


def get_fon(kod:list):

    arr = {}
    detail = {}
    for i in kod:
        link = f'https://www.tefas.gov.tr/FonAnaliz.aspx?FonKod={i}'
        r = requests.get(link)

        soup = BeautifulSoup(r.content,'lxml')
        div = soup.find("div", {"class": "main-indicators"})
        div_income = soup.find("div",{"price-indicators"})

        for ul1,ul2 in zip(div.find_all('ul'),div_income.find_all(('ul'))):
            for i,j in zip(ul1,ul2):
                if type(i) ==  bs4.element.Tag :
                    detail[i.text.split("\n")[0]] =i.span.text
                if type(j) ==  bs4.element.Tag :
                    detail[j.text.split("\n")[0]] =j.span.text

        
        
        header = soup.find_all("td", {"class": "fund-profile-header"})
        value = soup.find_all("td", {"class": "fund-profile-item"})

        for i,j in zip(header,value) :  
            if i.text != 'Kodu' :
                detail[i.text] = j.text
            else :
                arr[j.text] = detail
                
    arr = json.dumps(arr, ensure_ascii=False,indent = 4)
    return arr

