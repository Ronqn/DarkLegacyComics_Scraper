import requests
import os
import bs4

url = 'https://www.darklegacycomics.com/621'
os.makedirs('darklegacy', exist_ok=True)

while not url.endswith('#'):
    # Download the webpage
    print('Downloading the webpage %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image

    comicElem = soup.select('#gallery img')
    if comicElem == []:
        print('Can\'t find the comic')
    else:
        comicUrl = 'https://darklegacycomics.com/' + comicElem[0].get('src')

    # Download the image

    print('Downloading picture %s...' % (comicUrl))
    res = requests.get(comicUrl)
    res.raise_for_status()

    # Save the image to ./xkcd

    imageFile = open(os.path.join('darklegacy', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    #Get the previous button's url

    prevLink = soup.select('a[title*="Previous"]')[0]
    url = 'https://www.darklegacycomics.com/' + prevLink.get('href')

print('Done.')