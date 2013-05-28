#!/usr/bin/python

#NOTE: outputting some unicode characters to apple terminal wont work. Instead run this in the terminal first:
#export LANG='en_US.UTF-8'

from BeautifulSoup import BeautifulSoup
import urllib   
#import re



################
## ALBERTSONS ##
################
print("Beginning Albertson's Crawl...")

# read in website                                    
sock = urllib.urlopen("http://www.albertsons.com/savings/view-ads/view-circular.html")
htmlSource = sock.read()
sock.close()
soup = BeautifulSoup(htmlSource)
numpages = int(soup.findAll("li", {"class":"pages"})[0].findAll("a")[-1].getText())	#get the number of pages of adds

f = open("albertsons.csv","w")
f.write("Name,Price,Qprice,Desc,Expir\n")	#write Headers to files
#loop through all the pages
for j in range(1, numpages+1):
	print("Page %s of %s" % (j,numpages) )

	sock = urllib.urlopen("http://www.albertsons.com/savings/view-ads/view-circular.html?circularId=85916&sneakPeek=false&storeId=6390&currentPageNumber=" + str(j))
	htmlSource = sock.read()
	sock.close()

	soup = BeautifulSoup(htmlSource)
	itemName = soup.findAll("h3", {"class":"item-name"})
	itemPrice = soup.findAll("p", {"class":"item-price"})
	itemQprice = soup.findAll("p", {"class":"item-qprice"})
	itemDesc = soup.findAll("p", {"class":"item-desc"})
	itemExpir = soup.findAll("p", {"class":"item-expiry"})


	for i in range(0,len(itemName)-1):
		line =  (itemName[i].getText() +"\t"+ itemPrice[i].getText() +"\t"+ itemQprice[i].getText() +"\t"+ itemDesc[i].getText() +"\t"+ itemExpir[i].getText().replace('"', '') ).encode("utf-8")
		line = line.replace("\r\n"," ").replace(',',' ').replace('\t',',')+"\n"
		f.write( line )
		
f.close()	
	
print("Albertson's Crawl Complete!")