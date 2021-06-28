# This is a sample Python script.
import sysconfig
# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import json
import statistics

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def cuenta_letras(text_input):
    return (len(text_input))

def cuenta_palabras(text_input):
    txt = text_input.split(" ")
    #print(txt)
    return len(txt)

def cuenta_silabas(text_input):
    words = text_input.split(" ")
    silabas = 0
    vocales = ['a', 'e', 'i', 'o', 'u']
    for word in words:
        print(word)
        # en caso de mas de 2 letras intenta partirlo
        if len(word)>3:
            if word

        else:
            silabas+=1
    txt = text_input.split(" ")
    return(silabas)

def cuenta_frases(text_input):
    frases = text_input.split(".")
    return(len(frases)-1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    entrada = ""
    #entrada=input()
    if (entrada == ""):
        entrada = "NADA"
    print("Input was: {entrada}".format(entrada = entrada+" 1"))

    text_content="el amigo rocinante le gustaba mucho correr entre los molinos."
    print("Numero de letras: {}".format(cuenta_letras(text_input=text_content)))
    print("Numero de palabras: {}".format(cuenta_palabras(text_input=text_content)))
    print("Numero de silabas: {}".format(cuenta_silabas(text_input=text_content)))
    print("Numero de frases: {}".format(cuenta_frases(text_input=text_content)))

r = requests.get("http://demo3827929.mockable.io/urls")
data = r.text
soup = BeautifulSoup(data, 'html.parser')
dict = json.loads(str(soup))
dict_titles = {}
data = {}
title_lengths = []
data_to_export = ""

for key in dict:
    for url in dict[key]["urls"]:
        r = requests.get(url)
        data = r.text
        only_title_tags = SoupStrainer("title")
        soup = BeautifulSoup(data, 'html.parser', parse_only=only_title_tags)
        title_lengths.append(len(soup.title.text))
        domain = list(reversed(url.split("/")[2].split(".")))[1] + "." + list(reversed(url.split("/")[2].split(".")))[0]
        if domain in dict_titles.keys():
            dict_titles[domain].append(soup.title.text)
        else:
            dict_titles[domain] = [soup.title.text]


for url in dict_titles:
    median = statistics.median(title_lengths)
    data = {"domain": url, "median": median}
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "x-Auth-Token": "ABCDEFGHI12345678ASDFASD",
    }
    r = requests.request("POST", "http://demo2514549.mockable.io/tittle-length", data=json.dumps(data), headers=headers)
    print r.status_code


for url in dict_titles:
    data_to_export += url + ";"
    for title in dict_titles[url]:
        data_to_export += title.strip() + ","
    data_to_export += "\n"

f = open("dict.txt", "w")
f.write(str(data_to_export.encode('utf-8')))
f.close()
