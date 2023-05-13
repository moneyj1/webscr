from bs4 import BeautifulSoup as bs

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = bs(content, 'lxml')
    ids = soup.find('h2')
    ida = soup.find('h1')
    jk = soup.find_all('h5')
    nj = soup.find_all('h5', class_='hm')
    for txt in jk:
        print(txt.text)

    print(nj)
    #hello!!!!!!!
    #new comm
    #hello i'm back