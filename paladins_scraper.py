import requests
from bs4 import BeautifulSoup


def main():
    url = "https://paladins.fandom.com/wiki/Treasure_Chests"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    column = soup.find("div", "div-col")
    c = column.find_all('a')
    chests = []
    for i in c:
        chests.append(i.attrs['title'])
    return (set(chests))

if __name__ == '__main__':
    main()