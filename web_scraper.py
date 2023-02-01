import urllib.request as urlb
# web scraper https://www.youtube.com/watch?v=IvuK1hdmVjc
response = urlb.urlopen("https://www.google.com")
print(response.info())
html=response.read()
print(html)
response.close()