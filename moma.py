# required libraries in order of appearance
import pandas as pd
import urllib
from bs4 import BeautifulSoup
from skimage import io

url = 'https://www.moma.org/collection/works/8970' 
site = urllib.request.urlopen(url)
soup = BeautifulSoup(site)
bild = soup.select('section div img')
# ev insert loop for cases where there are several images
b = bild[0]
if 'srcset' in b.attrs:
	prts = b['srcset'].split(', ')
	# prts[-1] takes the biggest resolution (2000 px) available
	# alternative resolutions are 320, 640, ..., 1440 px
	pth = prts[-1].split(' ')[0]
	pic = io.imread('http://www.moma.org/'+pth)
	io.imsave('toros.png',pic)
else:
	# if no image available
	print(url)
