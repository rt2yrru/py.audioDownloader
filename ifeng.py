import os, sys, json
import requests
import subprocess
from bs4 import BeautifulSoup

def proc_audio(href):
    href = 'http://music.163.com' + href
    print('Href : ', href)

    r = requests.get(href)
    soup = BeautifulSoup(r.text, "html.parser")

    node = soup.find('textarea', id='program-data')
    node = node.getText()
    js = json.loads(node)

    title = js.get('mainSong').get('name')
    title = title + '.' + js.get('mainSong').get('bMusic').get('extension')
    url = js.get('mainSong').get('mp3Url')

    cmd = 'wget -c ' + url + ' -O ' + title
    print('CMD : ', cmd)

    subprocess.call(cmd, shell=True)


def proc_album(album):

    album = album.replace('/#/', '/m/')

    print('ifeng : ', album)

    os.sys.exit()

    r = requests.get(album)
    soup = BeautifulSoup(r.text, "html.parser")

    i = soup.find('h2', class_='f-ff2')
    album = i.getText()


    for i in soup.find_all('div', class_='tt f-thide'):
        j = i.findChild('a')
        title = j.get('title')

        if len(title) != 0:
            proc_audio(j.get('href'))

