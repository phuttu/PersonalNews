import tkinter as tk
from tkinter import Label, Text
from tkinter.font import BOLD 
from newsapi import NewsApiClient
import webbrowser

def main():
    newsWindow(getNews())

def newsWindow(newsAndUrl):
    listArticle = newsAndUrl[0]
    listUrl = newsAndUrl[1]
    window = tk.Tk()
    window.title("News")
    window
    lname = Label(window, text = "Personal News")
    lname.config(font =("algerian", 33, BOLD,))
    lname.pack(pady=20)
    canvas = tk.Canvas(window, height= 700, width=700)
    canvas.pack()


    
    for i in range(10):
        label = tk.Label(canvas, justify = "left")
        label.pack(padx=20)
        label.config(text = str(i+1) +". "+listArticle[i], font=("verdana", 10, BOLD))
        link = tk.Label(canvas, justify = "left")
        link.pack(padx=20)
        link.config(text = listUrl[i], font=("verdana", 10), fg="blue", cursor="hand2")
        lspace = Label(canvas)
        lspace.pack()
        createLink(listUrl[i],link)
    
    window.mainloop()

def getNews():
    newsapi = NewsApiClient(api_key='---put your API key here---')
    all_articles = newsapi.get_everything(
    q='Artificial intelligence',
    language='en')
    my_articles = []
    my_url = []
    for x in all_articles['articles']:
        my_articles.append(x['title'])
        my_url.append(x['url'])

    return [my_articles, my_url]


def openUrl(url):
    webbrowser.open_new(url)

def createLink(url,link):
    url = url
    link.bind("<Button-1>", lambda e: openUrl(url))




main()