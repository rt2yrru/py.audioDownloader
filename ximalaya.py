
import os
import requests
import subprocess
from bs4 import BeautifulSoup

def proc_track(title, track_id):
    title = title.strip(' \t\r\n')
    title = title.rstrip(' \t\r\n')

    href = 'http://www.ximalaya.com/tracks/' + track_id + '.json'

    r = requests.get(href)
    j = r.json()
    path = j.get('play_path')
    ext = path[path.rfind('.'):]

    print('Title : ', title, ', Href : ', path)

    title = '\'' + title + ext + '\''
    cmd = 'wget -c ' + path + ' -O ' + title

    subprocess.call(cmd, shell=True)


def proc_audio(title, href):
    href = 'http://www.ximalaya.com' + href
    #print('Href : ', href)

    r = requests.get(href)
    soup = BeautifulSoup(r.text, "html.parser")

    for i in soup.find_all('a', class_='shareLink'):
        track = i.get('track_id')
        #print('Track id : ', track)
        proc_track(title, track)

def proc_album(album):
    r = requests.get(album)
    soup = BeautifulSoup(r.text, "html.parser")

    for i in soup.find_all('a', class_='title'):
        title = i.get('title')

        if len(title) != 0:
            proc_audio(title, i.get('href'))

    i = soup.find('a', class_='pagingBar_page', rel='next')

    if i:
        proc_album('http://www.ximalaya.com' + i.get('href'))


