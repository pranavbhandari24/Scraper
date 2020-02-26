import requests, os, bs4

#url of website
url = 'https://xkcd.com/'

#counter of how many we want (CAP LIMIT)
count = 12

for i in range(count):
    response = requests.get(url)
    response.raise_for_status()

    #pasing the html page and making a beautiful soup object to make it simpler
    soup  = bs4.BeautifulSoup(response.text, 'html.parser')

    #looking for the image through id of the division ('comic') in html page
    comic_element = soup.select('#comic img')
    #getting the navigation element from the html page
    navigation_element = soup.select('.comicNav li')

    # checking if we get something
    if comic_element == []:
        print('No comic found!')
    else:
        # Extracting the source if we got something
        comic_url = 'https:' + comic_element[0].get('src')
        print(comic_url)
        image = requests.get(comic_url)
        image.raise_for_status()

    # Updating url to go the next page
    url = 'https://xkcd.com' + navigation_element[1].get('href')
