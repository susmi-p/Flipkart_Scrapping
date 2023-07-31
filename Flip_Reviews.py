import pandas as pd
import requests
from bs4 import BeautifulSoup

#url="https://www.flipkart.com/"
Name_Of_Person=[]
Comment_Title=[]
Rating=[]
Description=[]

#for i in range(2,22):
url="https://www.flipkart.com/apple-iphone-14-purple-128-gb/product-reviews/itm0b581eba85e08?pid=MOBGHWFHQFSQYBFU&lid=LSTMOBGHWFHQFSQYBFUUF0OWI&marketplace=FLIPKART&page=1"

response=requests.get(url)
#print(response)

Soup=BeautifulSoup(response.text,"html.parser")
#print(Soup)

#np=Soup.find("a",class_="_1LKTO3").get("href")
#print(np)

#cnp="https://www.flipkart.com"+np
#print(cnp)

#for i in range(2,10):#1st page data we have
    #url="https://www.flipkart.com/apple-iphone-14-purple-128-gb/product-reviews/itm0b581eba85e08?pid=MOBGHWFHQFSQYBFU&lid=LSTMOBGHWFHQFSQYBFUUF0OWI&marketplace=FLIPKART&page="+str(i)
    #here we are add str i at end as page no's changing then page changes to 2 to 10 as the link is same for every page
    #response=requests.get(url)
    #Soup=BeautifulSoup(response.content,"html.parser")
    #np=Soup.find("a",class_="_1LKTO3").get("href")
    #cnp="https://www.flipkart.com"+np
    #print(cnp)


box=Soup.find("div",class_="_1YokD2 _3Mn1Gg col-9-12")
#in that page thare are other than this product descrption also available with same tags for that we will add that part div where we want extract data
names=box.find_all("p",class_="_2sc7ZR _2V5EHH")
#print(names)

for i in names:
    name=i.text
    Name_Of_Person.append(name)
#print(Name_Of_Person)
#print(len(Name_Of_Person))

comment=box.find_all("p",class_="_2-N8zT")
#print(comment)

for i in comment:
    comment=i.text
    Comment_Title.append(comment)
#print(Comment_Title)

Desc=box.find_all("div",class_="t-ZTKy")
#print(Desc)

for i in Desc:
    Desc=i.text
    Description.append(Desc)
#print(Description)

review=box.find_all("div",class_="_3LWZlK _1BLPMq")
#print(review)

for i in review:
    review=i.text
    Rating.append(review)
#print(Rating)
#print(len(Description))


df=pd.DataFrame({"Person Name":Name_Of_Person,"Title":Comment_Title,"Rating":Rating,"Description":Description})
#print(len(Name_Of_Person))
#print(len(Comment_Title))
#print(len(Rating))
#print(len(Description))
#print(df)
df.to_csv(r"C:\Users\hp\Flipkart_review_scrapping.csv")





