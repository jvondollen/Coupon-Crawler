#!/usr/bin/python

#NOTE: outputting some unicode characters to apple terminal wont work. Instead run this in the terminal first:
#export LANG='en_US.UTF-8'

from BeautifulSoup import BeautifulSoup
import urllib
import urllib2   

#############
## SAFEWAY ##
#############
print("Beginning Safeway's Crawl...")


opener = urllib2.build_opener()
#opener.addheaders.append(('Cookie', 'drpstorid=1954'))
#f = opener.open("http://safeway.inserts2online.com/I2O_MainFrame.jsp?pageNumber=1&drpStoreID=1954&adId=48948&adPath=SafewaySafeway05222013NorcalWeeklyAd")
#htmlSource = f.read()

# read in website                                    
sock = urllib.urlopen("http://safeway.inserts2online.com/storeReview.jsp?drpStoreID=1682&showFlash=false&shoppingFlag=shoppingFlag&JSESSIONID=7E2E955AE0C17BF38A4B833BF8BFEC1C")
htmlSource = sock.read()
sock.close()
soup = BeautifulSoup(htmlSource)

print(soup)

print("Safeway's Crawl Complete!")




#http://weeklyspecials.safeway.com/customer_Frame.jsp?drpStoreID=1682
#view-source:http://weeklyspecials.safeway.com/pageLarge.jsp?pageNumber=1&drpStoreId=1682&showFlash=false
#http://safeway.inserts2online.com/storeReview.jsp?drpStoreID=1682&showFlash=false&shoppingFlag=shoppingFlag
#http://safeway.inserts2online.com/I2O_MainFrame.jsp?pageNumber=1&drpStoreID=1682&adId=47493&adPath=SafewaySafeway02202013NorcalWeeklyAd




#http://safeway.inserts2online.com/storeReview.jsp?drpStoreID=1954&showFlash=false&shoppingFlag=shoppingFlag&JSESSIONID=7E2E955AE0C17BF38A4B833BF8BFEC1C