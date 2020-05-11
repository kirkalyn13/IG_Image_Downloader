import requests
import random
from bs4 import BeautifulSoup
import webbrowser
import urllib.request   #lib for download
from tkinter import *

def dljpg(url):
##    name = random.randrange(1,1000)
    filename = entname.get()
    fullname = str(filename) + '.png'
    urllib.request.urlretrieve(url,fullname)    #download image
    
def click():
    entered_text=txtent.get() #get data from entry box
    url = str(entered_text)

    response = requests.get(url)    #get response from webpage

    restotxt = BeautifulSoup(response.text) #convert to string/text

    image = restotxt.find('meta', property = 'og:image')    #search for image og filename
    image_url = image['content']    #extract image url from search

    webbrowser.open(image_url, new=0, autoraise = True )    #open image in webpage

    dljpg(image_url)
    
    out.delete(0.0, END)
   
window = Tk()
window. title("Instagram OG File Locator")
window.configure(background = 'purple')

photo1 = PhotoImage(file='580b57fcd9996e24bc43c521.png')
Label (window, image=photo1, bg = 'purple') .grid(row=0, column=0, sticky=S)

Label (window, text='Enter URL: ', bg = 'purple', fg = 'orange', font='none 12 bold')\
      .grid(row = 1, column = 0, sticky = W)

txtent = Entry(window, width = 75, bg = 'white')
txtent.grid(row = 2, column = 0, sticky = W)

Label (window, text='Save as: ', bg = 'purple', fg = 'orange', font='none 12 bold')\
      .grid(row = 3, column = 0, sticky = W)

entname = Entry(window, width = 75, bg = 'white')
entname.grid(row = 4, column = 0, sticky = W)

Button(window, text = 'DOWNLOAD', width =10, command = click)\
               .grid(row = 5, column = 0, sticky = W)



#exit
Label (window, text = 'Click to exit: ', bg = 'purple', fg = 'orange', font = 'none 12 bold') \
      .grid (row = 7, column = 0, sticky = W)


#exit func
def closewin():
    window.destroy()
    exit()
    
#add exit button
Button(window, text='Exit', width = 14, command = closewin) \
               .grid(row = 8, column = 0, sticky = W)



#Run main loop
window.mainloop()


