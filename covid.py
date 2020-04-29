import notify2
import requests
import time
from bs4 import BeautifulSoup

def notifyMe(title,message):
    notify2.init("Covid-19")
    noti = notify2.Notification(title,message,"/home/sparsh/Desktop/Covid/new.jpg")   
    noti.show()

def getDataurl(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    notifyMe("Sparsh","Lets stop spreading of this virus together")
    myhtmlData = getDataurl("https://www.mohfw.gov.in/")

    mydatastr = " "
    soup = BeautifulSoup(myhtmlData,'html.parser')
    for tr in soup.find_all('tbody')[-1].find_all('tr'):
         mydatastr += tr.get_text()
    mydatastr = mydatastr[2:]
    itemlist = mydatastr.split("\n\n")
    #print (itemlist)
    #total = ['Total number of confirmed cases in India']
    states = ['Rajasthan','Uttarakhand','Karnataka','Jammu and Kashmir','Total number of confirmed cases in India']
    for item in itemlist[0:33]:
        datalist = (item.split('\n'))
        if datalist[1] in states:
            ntitle = 'Cases of Covid-19 in INDIA'
            ntext = f"{datalist[1]}\n Total: {datalist[2]}\n Cured: {datalist[3]}\n Death: {datalist[4]}\n"
            notifyMe(ntitle,ntext)
            time.sleep(2.0)
    time.sleep(10.0)
            