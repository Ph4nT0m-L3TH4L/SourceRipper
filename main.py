import requests
from bs4 import BeautifulSoup


logo = '''                                              
 _____                     _____ _                 
|   __|___ _ _ ___ ___ ___| __  |_|___ ___ ___ ___ 
|__   | . | | |  _|  _| -_|    -| | . | . | -_|  _|
|_____|___|___|_| |___|___|__|__|_|  _|  _|___|_|  
                                  |_| |_|    

SourceRipper | Developed by RaidTheWeb for Ph4nT0m/L3TH4L      
'''

print(logo)
print()
print('> https://example.com')
print()
site = input('site > ')
print()

r = requests.get(site)

print('HTTP CODE %s > %s' % (r.status_code, site))

soup = BeautifulSoup(r.text, 'html.parser')

scripts = soup.find_all('script')
stylesheets = soup.find_all('link')

for script in scripts:
    try:
        print(script['src'])
        if script['src'].startswith('https://') or script['src'].startswith('http://'):
            r = requests.get(script['src'])
            filename = script['src'].split('/')
            filename = filename[len(filename) - 1]
            with open(filename, 'wb') as _file:
                _file.write(r.content)
        else:
            r = requests.get(site + script['src'])
            filename = script['src'].split('/')
            filename = filename[len(filename) - 1]
            with open(filename, 'wb') as _file:
                _file.write(r.content)
    except KeyError:
        pass

for sheet in stylesheets:
    try:
        print(sheet['href'])
        if sheet['href'].startswith('https://') or sheet['href'].startswith('http://'):
            src = sheet['href']
            r = requests.get(src)
            filename = src.split('/')
            filename = filename[len(filename) - 1]
            try:
                with open(filename, 'wb') as _file:
                    _file.write(r.content)
            except FileNotFoundError:
                pass
        else:
            src = sheet['href']
            if src.startswith('/'):
                r = requests.get(site + src)
                filename = src.split('/')
                filename = filename[len(filename) - 1]
                with open(filename, 'wb') as _file:
                    _file.write(r.content)
            else:
                r = requests.get(site + src)
                filename = src.split('/')
                filename = filename[len(filename) - 1]
                with open('/' + filename, 'wb') as _file:
                    _file.write(r.content)
    except KeyError:
        pass
