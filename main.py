import os
import json 
import requests
from bs4 import BeautifulSoup
os.system("clear")


# Получение HTML (Уникальна)
def get_html (url, header): #get_html(url, header): URL мен headers параметрлерін қабылдайтын функция.
    response= requests.get(url, headers=header) #Kөрсетілген URL-ға HTTP GET сұрауын жібереді.

    if response.status_code !=200: #Егер жауап коды 200-ге тең болмаса (яғни, сұрау сәтті орындалмаса), қате хабарламасын қайтарады.
        return f"Error: {response.status_code}"
    else:
        return response.text #Әйтпесе, HTML мәтінін қайтарады.

# Обработка HTML (процесс)
def processing(html): #HTML мәтінін қабылдайтын және оны өңдейтін функция.
    soup = BeautifulSoup(html, "lxml").find('div', {'class': 'product-grid'}) #HTML-ды BeautifulSoup арқылы парсинг жасап, product-grid класындағы div элементін табады.
    products = soup.find_all('div', {'class': 'product-card'}) #Барлық product-card класындағы div элементтерін табады.

    data = [] # Мәліметтерді сақтау үшін бос тізім жасайды.

    for product in products: #Әрбір өнімді өңдеу үшін цикл бастайды.
        a = product.find('a') #Өнім ішіндегі 'a' тегін табады.
        product_url ='https://www.lcwaikiki.kz' + a.get('href') #Өнім сілтемесін құрайды.
        product_id = a.get('data-optionid') #Өнімнің идентификаторын алады.
        product_title = a.get('title') #Өнімнің атауын алады.

        product_price =a.find(
            'div', {'class':'product-price'}).find(
            'span', {'class': 'product-price__price'}).text

        data.append({ 
            'product_url': product_url,
            'product_id': product_id,
            'product_title': product_title,
            'product_price': product_price.replace(' ',' ') #('\xa0 ',' ')
        })#Мәліметтер тізіміне өнім туралы ақпаратты қосады.

    return data #Мәліметтерді қайтарады.

        # print(product_url)
        # print(product_id)
        # print(product_title)

    # return0 products


# Запуск кода  (Уникальна)
def main(): #Негізгі функция, бағдарламаны іске қосады.
    header = { 
            'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0"
        } #HTTP сұрауының headers параметрлері, браузердің пайдаланушы агентін қамтиды.
   
    data=[]
    for page in range (1,10):
        url = 'https://www.lcwaikiki.kz/ru-RU/KZ/tag/tshirt-7-5?PageIndex={page}' 
       
        if page < 2:
            url = 'https://www.lcwaikiki.kz/ru-RU/KZ/tag/tshirt-7-5'

        html = get_html (url, header) #HTML мәтінін алу үшін get_html функциясын шақырады.
        soup = processing(html) #HTML мәтінін өңдеу үшін processing функциясын шақырады.
        
        data.extend(soup)
        print(f"Page: {page} | {url [0:len(url)//2]}...")

        # with open ("index.html", "w", encoding="utf-8") as file:
        #     file.write(str(soup))
        
    with open ("data.json", "w",) as file: #Нәтижені JSON файлына жазу үшін файлды ашады.
        json.dump(soup, file, indent=4, ensure_ascii=False) #Мәліметтерді JSON форматына сақтайды.
        
main()







# import os
# import json 
# import requests
# from bs4 import BeautifulSoup
# os.system("clear")


# # Получение HTML (Уникальна)
# def get_html (url, header): #get_html(url, header): URL мен headers параметрлерін қабылдайтын функция.
#     response= requests.get(url, headers=header) #Kөрсетілген URL-ға HTTP GET сұрауын жібереді.

#     if response.status_code !=200: #Егер жауап коды 200-ге тең болмаса (яғни, сұрау сәтті орындалмаса), қате хабарламасын қайтарады.
#         return f"Error: {response.status_code}"
#     else:
#         return response.text #Әйтпесе, HTML мәтінін қайтарады.

# # Обработка HTML (процесс)
# def processing(html): #HTML мәтінін қабылдайтын және оны өңдейтін функция.
#     soup = BeautifulSoup(html, "lxml").find('div', {'class': 'product-grid'}) #HTML-ды BeautifulSoup арқылы парсинг жасап, product-grid класындағы div элементін табады.
#     products = soup.find_all('div', {'class': 'product-card'}) #Барлық product-card класындағы div элементтерін табады.

#     data = [] # Мәліметтерді сақтау үшін бос тізім жасайды.

#     for product in products: #Әрбір өнімді өңдеу үшін цикл бастайды.
#         a = product.find('a') #Өнім ішіндегі 'a' тегін табады.
#         product_url ='https://www.lcwaikiki.kz' + a.get('href') #Өнім сілтемесін құрайды.
#         product_id = a.get('data-optionid') #Өнімнің идентификаторын алады.
#         product_title = a.get('title') #Өнімнің атауын алады.

#         data.append({ #Мәліметтер тізіміне өнім туралы ақпаратты қосады.
#             'product_url':product_url,
#             'product_id':product_id,
#             'product_title':product_title
#         })

#     return data #Мәліметтерді қайтарады.

#         # print(product_url)
#         # print(product_id)
#         # print(product_title)

#     # return0 products


# # Запуск кода  (Уникальна)
# def main(): #Негізгі функция, бағдарламаны іске қосады.
#     url = 'https://www.lcwaikiki.kz/ru-RU/KZ/tag/toys-kz' #Сұрау жасалатын URL.
#     header = { 
#         'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0"
#     } #HTTP сұрауының headers параметрлері, браузердің пайдаланушы агентін қамтиды.

#     html = get_html (url, header) #HTML мәтінін алу үшін get_html функциясын шақырады.
#     soup = processing(html) #HTML мәтінін өңдеу үшін processing функциясын шақырады.
    
#     # with open ("index.html", "w", encoding="utf-8") as file:
#     #     file.write(str(soup))
    
#     with open ("data.json", "w",) as file: #Нәтижені JSON файлына жазу үшін файлды ашады.
#         json.dump(soup, file, indent=4, ensure_ascii=False) #Мәліметтерді JSON форматына сақтайды.

#     print(soup)#Мәліметтерді консольге шығарады.

# main()

