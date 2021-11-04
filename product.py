import tkinter
import requests 
from bs4 import BeautifulSoup
from tkinter import *



r = requests.get("https://webscraper.io/test-sites/e-commerce/allinone")
if r.status_code == 200:
    print("the page is available for mining")

else : 
    print("check another url")


soup = BeautifulSoup(r.content,'html.parser')

text = soup.get_text()
print()

div = soup.findAll("div",{"class":"thumbnail"})
x = []
y = []
r = []
z = []
for i in div:
    title_of_product = i.find("a",{"class":"title"})
    x.append(title_of_product.get_text())
    price = i.find("h4",{"class":"pull-right price"})
    y.append(str((price.get_text())))
    image = i.find("img",{"class":"img-responsive"})    
    z.append(image.attrs["src"])
    rating = i.find_all("span")
    print(rating)
    r.append(str(len(rating)))
    #saving the image in a file
    

print(r)
print(x)
print(y)
print(z)






#user interface
win = Tk()
win.geometry("1000x500")
win.title("product and their price")
#buttons
count = 0
def next():
    global count
    title_of_product = Label(win,text = "The product is : ", font= ('Aerial', 17))
    Product = Label(win,text = x[count], font= ('Aerial', 17))
    title_of_price = Label(win,text = "The price is : ", font= ('Aerial', 17))
    Price = Label(win,text=y[count], font= ('Aerial', 17))
    ratings = Label(win,text = "The rating is : ", font= ('Aerial', 17))
    rating = Label(win,text = r[count], font= ('Aerial', 17))
    title_of_product.grid(column=0, row=0)
    title_of_price.grid(column=0, row=1)
    ratings.grid(column=0,row=2)
    Product.grid(column=1, row=0)
    Price.grid(column=1, row=1)
    rating.grid(column=1, row=2)
    count = count+1
def exit():
    win.destroy()

#show
title_of_product = Label(win,text = "The product is : ", font= ('Aerial', 17))
Product = Label(win,text = x[0], font= ('Aerial', 17))
title_of_price = Label(win,text = "The price is : ", font= ('Aerial', 17))
Price = Label(win,text=y[0], font= ('Aerial', 17))
ratings = Label(win,text = "The rating is : ", font= ('Aerial', 17))
rating = Label(win,text = r[0], font= ('Aerial', 17))

#buttons
n = tkinter.Button(win,text='next item',command= next)
ex = tkinter.Button(win,text="exit",command = exit)



#placement of the texts
title_of_product.grid(column=0, row=0)
title_of_price.grid(column=0, row=1)
ratings.grid(column=0, row=2)

Product.grid(column=1, row=0)
Price.grid(column=1, row=1)
rating.grid(column=1, row=2)
n.grid(column=2, row=2)
ex.grid(column=3, row=2)







win.mainloop()