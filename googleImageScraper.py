from bs4 import BeautifulSoup as bs
import urllib.request as ur
import re
import json


url_constant = 'http://images.google.com/images?q='
# url_constant = 'http://www.google.com/images?q=' #ALSO WORKS

# url_variable = input('Enter Seach Term:') #Tested
url_variable = 'modi memes' #for testing

# print(type(url_variable))
# url_variable.replace(" ","_") #DIDN'T WORK
url_variable = re.sub(r'\s+', '%20', url_variable)
print(url_variable)

url = url_constant+url_variable


header = {'User-Agent': 'Mozilla/5.0'}  # Needed to prevent 403 error on Wikipedia
req = ur.Request(url, headers=header)
page = ur.urlopen(req)
soup = bs(page,'html.parser')

# print(soup)
image_list = soup.findAll("img")
print("image_list length:",len(image_list))
for i in image_list:
	print(i)
	# print("link:",i.src)
	print("Link:",i["src"])

# ActualImages=[]# contains the link for Large original images, type of  image

# for a in soup.find_all("div",{"class":"rg_meta"}):
# 	link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
# 	ActualImages.append((link,Type))

# print(ActualImages)	    
# # url = driver.current_url
# # page = open(url)
# # page = (driver.page_source)
# # soup = BeautifulSoup(page,'html.parser')