import requests, sqlite3, time
from bs4 import BeautifulSoup

def get_online():
    r = requests.get('https://osu.ppy.sh/home')
    soup = BeautifulSoup(r.text, 'html.parser')
    numbers = list(map(str, soup.find_all('strong')))
    start = numbers[1].find('>')
    finish = numbers[1].find('</')
    return ''.join(numbers[1][start+1:finish].split(','))

conn = sqlite3.connect('osu_online.db')
c = conn.cursor()
c.execute('CREATE TABLE online (date, players)')

for i in range(48):
    wrap = (str(time.ctime()), get_online())
    c.execute('INSERT INTO online VALUES (?, ?)', wrap)
    conn.commit()
    time.sleep(1800)

c.close()

