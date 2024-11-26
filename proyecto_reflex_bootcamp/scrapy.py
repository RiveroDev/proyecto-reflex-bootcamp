import requests
from bs4 import BeautifulSoup as bs 

URL = "https://shopgoodwill.com/categories/new?st=&sg=New&c=30&s=&lp=0&hp=999999&sbn=&spo=false&snpo=false&socs=false&sd=false&sca=false&caed=11%2F25%2F2024&cadb=7&scs=false&sis=false&col=1&p=1&ps=40&desc=true&ss=0&UseBuyerPrefs=true&sus=false&cln=2&catIds=-1,7,30&pn=&wc=false&mci=false&hmt=false&layout=grid&ihp="

def get_URL(URL) -> int:
   """recibe una url de donde se ontendra toa la informacion
   y retonara objeto requert"""
   response = requests.get(URL)
   return response

def status_URl(response, number = 200) -> bool:
   """recibe un objeto requests.get de una URL """
   status = response.status_code == number
   return status

def objetRespondeText(response):
   content = response.text
   return content

def obj_bs():
    pass




if __name__ == "__main__":

    res = get_URL(URL)

    soup = objetRespondeText(res)
    with open("resumen.html", "w+") as file:
        file.write(soup)

    soup1 = bs(objetRespondeText(res), 'html.parser')
    #print(soup1.body)

    info = soup.find("title")
    #print(info)

    info2 = soup1.find_all("div", {})

    for i in info2:
      pass# print(i , "\n")

    idObjet = soup1.find_all("id")

    for i in idObjet:
       print(i , "\n")

    """
      with open("resumen.html", "w+") as file:
        file.write(content)
        """
#print(content)
