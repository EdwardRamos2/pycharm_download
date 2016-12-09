#!/usr/bin/env python3
#Autor: Edward Ramos  <edward.ramos@linuxmail.org>
#Date: 12/08/2016 U.S.A

import urllib.request
import os , sys
print('Download + Install [PyCharm 2016.3] - Version 0.1.0')
def download_arquivos():
    print('[1] Direct download: ')
    print('[2] Custom download: ')
    print('[3] Install')
    opcao = input('option: >> ')
    if opcao == '1':
        #import urllib.request
        url = 'https://dw.uptodown.com/dwn/35g50nV9UabTpPqNoxNPJlyKU8arD8JpU5Jssi0050Hr5gSWvfEFjkA65gfidf3xPHek0ARgJqbMkocbW57db4mI9tOAaHsDlUVBs6-Q65ga17Gveaazj1zXgcYWt5dr/51Lfyh0QdjYqUeXRphT_b67E7mpylCowxoy4BNl2pG5iwcEGGgcOeUmD7yCNJZRMmjDhc_7yPtro9CL5qAMiKJ7A1lK5tj0v1a7JdGb_XHf3OooDl7Cesk-LUa3hzu5m/HOWK4RVmJxaqsXzJUg9rLQr3WSMK5BLA_9CCot-nLsd9D7twkI73GuTntziptr6w4oov5hUHMp-NB9TUWhZBY7KxaGwwLJyLRhRJ-Al2ZlP0HkHdMnJb5MzYJHFeII_b/_zaEUkcnk4byxEcqvGkke8SqPGxUwM8-83x6-bB6altFrX7ysXYJzK3_Bu7gkbtkKLPF0kbLOSPmqRUFiPTIvw==/'
        file_name = 'universalUSB22.exe'
        # Download the file from `url` and save it locally under `file_name`:
        with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
            data = response.read() # a `bytes` object
            out_file.write(data)
    if opcao == '2':
        #import urllib.request
        url = input('Insira a URL para realizar o DOWNLOAD: \n')
        file_name = input('Insira o NOME do ARQUIVO seguido da extensao! \n')
        # Download the file from `url` and save it locally under `file_name`:
        with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
            data = response.read() # a `bytes` object
            out_file.write(data)

    if opcao == '3':
        print('Archive Extract into /tmp')
        os.system('tar xvzf pycharm-community*.tar.gz -C /tmp/')
        print('Relocating PyCharm > Set the SuperUser as holder: ')
        os.system('su -c "chown -R root:root /tmp/pycharm*"')
        print('Then Switch the PyCharm contents: ')
        os.system('su -c "mv /tmp/pycharm-community* /opt/pycharm-community"')
        print('Making PyCharm Binaries Symlinks: ')
        os.system('su -c "ln -s /opt/pycharm-community/bin/pycharm.sh /usr/local/bin/pycharm"')
        os.system('su -c "ln -s /opt/pycharm-community/bin/inspect.sh /usr/local/bin/inspect"')
        print('Launching PyCharm Python IDE > From Shell:')
        os.system('pycharm')
download_arquivos()
