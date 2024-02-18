import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from datetime import datetime
import time
from winotify import Notification

# IDENTIFICAÇÃO PARA O SITE LIBERAR
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"}

# MAGAZINE LUIZA s22
url1 = "https://www.magazineluiza.com.br/smartphone-samsung-galaxy-s22-128gb-preto-5g-octa-core-8gb-ram-61-cam-tripla-selfie-10mp-dual-chip/p/237061600/te/gs22/"
site1 = requests.get(url1, headers=headers)
soup1 = BeautifulSoup(site1.content, 'html.parser')
try:
    preco_pix1 = soup1.find('p', class_='sc-kpDqfm eCPtRw sc-hoLEA kXWuGr').get_text()
except:
    preco_pix1 = "Não disponível"

# MAGAZINE LUIZA s22+
url2 = "https://www.magazineluiza.com.br/smartphone-samsung-galaxy-s22-128gb-branco-5g-8gb/p/234439600/te/gs22/"
site2 = requests.get(url2, headers=headers)
soup2 = BeautifulSoup(site2.content, 'html.parser')
try:
    preco_pix2 = soup2.find('p', class_='sc-kpDqfm eCPtRw sc-hoLEA kXWuGr').get_text()
except:
    preco_pix2 = "Não disponível"
time.sleep(5)

# MAGAZINE LUIZA s23
url3 = "https://www.magazineluiza.com.br/smartphone-samsung-galaxy-s23-128gb-preto-5g-8gb-ram-61-cam-tripla-selfie-12mp/p/232853700/te/gs23/"
site3 = requests.get(url3, headers=headers)
soup3 = BeautifulSoup(site3.content, 'html.parser')
try:
    preco_pix3 = soup3.find('p', class_='sc-kpDqfm eCPtRw sc-hoLEA kXWuGr').get_text()
except:
    preco_pix3 = "Não disponível"
time.sleep(5)

# ATUALIZA A PLANILHA
excel_file = 'preços_celulares.xlsx'
data_atual = datetime.today().strftime('%Y-%m-%d')

try:
    df = pd.read_excel(excel_file)
except FileNotFoundError:
    df = pd.DataFrame(columns=['Data', 's22 Magalu', 's22+ Magalu', 's23 Magalu'])

novo_dado = {'Data': data_atual, 's22 Magalu': preco_pix1, 's22+ Magalu': preco_pix2, 's23 Magalu': preco_pix3}
novo_df = pd.DataFrame([novo_dado])
df = pd.concat([df, novo_df], ignore_index=True)
df.to_excel(excel_file, index=False)

# NOTIFICAÇÃO NO WINDOWS
notificacao = Notification(app_id="Monitoramento de preços de celular",
                           title="Planilha atualizada",
                           msg="Os preços dos celulares monitorados foram adicionados à planilha.",
                           duration="short",
                           icon=r"C://Users/pedro/Desktop/Python/notificação_windows/logo.png")

notificacao.add_actions(label="Abrir planilha", launch="file:///C:/Users/pedro/Desktop/Python/preços_celulares.xlsx")
notificacao.show()