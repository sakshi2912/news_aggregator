from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import re




r1 = requests.get("https://www.hindustantimes.com/india-news/")
r2 = requests.get("https://timesofindia.indiatimes.com/briefs")
r3 = requests.get("https://www.newsbtc.com/")
r4 = requests.get("https://www.ndtv.com/world-news")




ht_soup = BeautifulSoup(r1.content, 'html5lib')
toi_soup = BeautifulSoup(r2.content, 'html5lib')
cryp_soup = BeautifulSoup(r3.content, 'html5lib')
soup_ndtv = BeautifulSoup(r4.content, 'html5lib')
ht_headlines = []
ht_headcontent=[]
templista=[]
templistb=[]

ht_headings = ht_soup.findAll("div", {"class": "media-heading headingfour"})
ht_links = ht_soup("a", {"class":"title"})


for i in ht_headings:
  for link in i.find_all('a'):
       if link.has_attr('href'):
          templistb.append(link.attrs['href'])  
        
for i in ht_headings:
    for c in ht_links:
        ht_headlines.append(c[title])
       
for hth in ht_headings:
    ht_headlines.append(hth.text)

for news in ht_soup.find_all('div', attrs={'class': 'media-body'}):
    for c in news.find_all('p'):
        ht_headcontent.append(c.text)


ht_cont_link=[list(x) for x in zip(ht_headcontent,templistb)]

newsdict=dict(zip(ht_headlines,ht_cont_link))

for i in newsdict:
     regex=re.compile(r'[\n\r\t]')
     if(i.startswith("\n\t\t\t\t")):
        i= regex.sub("",i)
        templista.append(i)
        
     else:
        pass
    
ht_full_dict=dict(zip(templista,ht_cont_link))
ht_first5={k: ht_full_dict[k] for k in list(ht_full_dict)[:5]}

#times of india


toi_headings = toi_soup.find_all('h2')
toi_headings = toi_headings[0:-13] 

templistc=[]
templistd=[]
templiste=[]
templistf=[]
newsdivs=toi_soup.find_all('div', attrs={'class': 'brief_box'})
toi_headings = toi_soup.find_all('h2')
for foo in newsdivs:
    
    #print(foo)
    for data in foo.find_all('p'):
       templistc.append((data.text))
         
toi_news = []

for th in toi_headings:
    toi_news.append(th.text)
#res=dict(zip(toi_news,templistc))
#print(res)
for i in newsdivs:
  for link in i.find_all('a'):
       if link.has_attr('href'):
          templistd.append(link.attrs['href'])
        
for i in range(0,len(templistd),3):
    if(not(templistd[i].startswith('/briefs'))):
      templiste.append(templistd[i])
    
   
  
for i in templiste:
    string='https://timesofindia.indiatimes.com'
    string=string+i
    templistf.append(string)
    string=""
    
new_lst = [list(x) for x in zip(templistc,templistf)]

toi_full_dict=dict(zip(toi_news,new_lst))
toi_first5={k: toi_full_dict[k] for k in list(toi_full_dict)[:5]}


###################crypt




templistg=[]
templisth=[]
templisti=[]
headings = cryp_soup.find_all("h2",{"class": "title medium"})
last_a_tag = cryp_soup.findAll("h2", {"class": "title medium"})
for i in last_a_tag:
       for link in i.find_all('a'):
          if link.has_attr('href'):
            templisti.append(link.attrs['href'])
#print(list3)            
for new in headings:
    for newdata in new.find_all("a"):
       # print(newdata.text)
        templisth.append(newdata.text)
newsDivs = cryp_soup.findAll("article")
for c in newsDivs:       
        for data in c.find_all('p'):
                templistg.append(data.text)
              #  print("\n")

newlist=[list(x) for x in zip(templistg,templisti)]
crypt_full_dict=dict(zip(templisth,newlist))
crypt_first5={k: crypt_full_dict[k] for k in list(crypt_full_dict)[:5]}


#####ndtv
list5a=[]
list5b=[]
list5c=[]
r4 = requests.get("https://www.ndtv.com/world-news")
soup_ndtv = BeautifulSoup(r4.content, 'html5lib')
ht_ra = requests.get("https://economictimes.indiatimes.com/news/international/world-news")
ht_soupa = BeautifulSoup(ht_ra.content, 'html5lib')
headings = ht_soupa.find_all("div", {"class":"eachStory"})
for i in headings:
    for data in i.find("h3"):
        list5a.append(data.text)
    for cont in i.find_all("p"):
        list5b.append(cont.text)
    for link in i.find_all("a"):
        if link.has_attr('href'):
            list5c.append('https://economictimes.indiatimes.com'+link.attrs['href'])

newlist_it=[list(x) for x in zip(list5b,list5c)]
inddict=dict(zip(list5a,newlist_it))


templistj=[]
templistk=[]
head=soup_ndtv.find_all("div",{"class":"description"})
for title in head:
    for x in title.find_all('a'):
        templistj.append(x.text)
        if x.has_attr('href'):
            templistk.append(x.attrs['href'])
ndtv_trend=dict(zip(templistj,templistk))        
#print(trend)
        
templistl=[]
templistm=[]
templistn=[]

title=soup_ndtv.find("div",{"class":"ins_left_rhs"});
for item in title.find_all("li"):
    for divi in item.find_all("div",{"class":"new_storylising_contentwrap"}):
        for anch in divi.find_all("a"):
            if anch.has_attr('title'):
                templistm.append(anch.attrs['title'])
            if anch.has_attr('href'):
                templistn.append(anch.attrs['href'])
        for dis in divi.find_all("div",{"class":"nstory_intro"}):
            templistl.append(dis.text)

        
newlist_ndtv=[list(x) for x in zip(templistl,templistn)]

ndtv_dict=dict(zip(templistm,newlist_ndtv))
ndtv_first5={k: ndtv_dict[k] for k in list(ndtv_dict)[:5]}

world={}
world['Economic Times']=inddict
world['NDTV']=ndtv_dict


# hind sport

ht_r = requests.get("https://www.hindustantimes.com/india-news/")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
ht_headings = ht_soup.findAll("div", {"class": "media-heading headingfour"})
links = ht_soup("a", {"class":"title"})
ht_headlines = []
ht_headcontent=[]
list4=[]
for i in ht_headings:
  for link in i.find_all('a'):
       if link.has_attr('href'):
          list4.append(link.attrs['href'])  
        
for i in ht_headings:
    for c in links:
        ht_headlines.append(c[title])
       
for hth in ht_headings:
    ht_headlines.append(hth.text)

for news in ht_soup.find_all('div', attrs={'class': 'media-body'}):
    for c in news.find_all('p'):
        ht_headcontent.append(c.text)

list3=[]
newlist=[list(x) for x in zip(ht_headcontent,list4)]

        

newsdict=dict(zip(ht_headlines,newlist))
#print(newsdict)
    #f(i.startswith('')
for i in newsdict:
     regex=re.compile(r'[\n\r\t]')
     if(i.startswith("\n\t\t\t\t")):
        i= regex.sub("",i)
        list3.append(i)
        
     else:
        pass
    
newsdict1=dict(zip(list3,newlist))


#################times of india
toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[0:-13] 



list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
newsdivs=toi_soup.find_all('div', attrs={'class': 'brief_box'})
toi_headings = toi_soup.find_all('h2')
for foo in newsdivs:
    
    #print(foo)
    for data in foo.find_all('p'):
       list2.append((data.text))
         
toi_news = []

for th in toi_headings:
    toi_news.append(th.text)
#res=dict(zip(toi_news,list2))
#print(res)
for i in newsdivs:
  for link in i.find_all('a'):
       if link.has_attr('href'):
          list4.append(link.attrs['href'])
        
for i in range(0,len(list4),3):
    if(not(list4[i].startswith('/briefs'))):
      list5.append(list4[i])
    
   
  
for i in list5:
    string='https://timesofindia.indiatimes.com'
    string=string+i
    list6.append(string)
    string=""
    
new_lst = [list(x) for x in zip(list2,list6)]
mynewdict=dict(zip(toi_news,new_lst))
##################3cryp 
list11=[]
list12=[]
list13=[]
list14=[]
ht_r = requests.get("https://www.newsbtc.com/")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
last_a_tag = ht_soup.findAll("h2", {"class": "title medium"})
good_a_tag = ht_soup.findAll("p", {"class":"excerpt"})
for i in last_a_tag:
    list11.append(i.text)
#for i in good_a_tag:
  # print(i.text)  
for i in good_a_tag:
    list12.append(i.text)
    

for i in last_a_tag:
    
        
       for link in i.find_all('a'):
       
          if link.has_attr('href'):
            list13.append(link.attrs['href']) 
            
newlist=[list(x) for x in zip(list12,list13)]
newdict=dict(zip(list11,newlist))


#sportsnews
ht_r = requests.get("https://www.hindustantimes.com/sports-news/")
list21=[]
list22=[]
list23=[]
list24=[]
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
ht_headings = ht_soup.findAll("div", {"class": "media-heading headingfour"})
links = ht_soup("a", {"class":"title"})
for i in ht_headings:
  for link in i.find_all('a'):
       if link.has_attr('href'):
          list24.append(link.attrs['href']) 
for i in ht_headings:
    for c in links:
        list23.append(c[title])
        
for hth in ht_headings:
    list23.append(hth.text)
#print(list23)
for news in ht_soup.find_all('div', attrs={'class': 'media-body'}):
    for c in news.find_all('p'):
        list22.append(c.text)
        
newlist=[list(x) for x in zip(list22,list24)]
newsdict=dict(zip(list23,newlist))
for i in newsdict:
     regex=re.compile(r'[\n\r\t]')
     if(i.startswith("\n\t\t\t\t")):
        i= regex.sub("",i)
        list21.append(i)
        
     else:
        pass
    
newssports=dict(zip(list21,newlist))

sport_r = requests.get("https://www.sportspundit.com/cricket/articles/?gclid=Cj0KCQjwpfHzBRCiARIsAHHzyZrKzHfccihdgUuRCL5ZtKJ_9kBeZlUgopM9oTvPtfpo6zGuTGDDyNYaAiSTEALw_wcB")
list25=[]
list27=[]
list26=[]
list28=[]
list29=[]
list30=[]
list31=[]
list32=[]
ht_soup = BeautifulSoup(sport_r.content, 'html5lib')
ht_headings = ht_soup.findAll("div", {"class": "text-holder","id":"articles"})
#ht_headings1 = ht_soup.find_all("h2")
for i in ht_headings:
    for data in i.find_all('h2'):
        list27.append((data.text))
for i in ht_headings:
    for data in i.find_all('p'):
        list26.append((data.text))
for i in ht_headings:
    for data in i.find_all('h2'):
        for link in data.find_all('a'):
            if link.has_attr('href'):
               list28.append(link.attrs['href']) 
#print(list27) 
for i in list27:
     regex=re.compile(r'[\n\r\t]')
     if(i.startswith("\n")):
        i= regex.sub("",i)
        list31.append(i)
        
     else:
        pass
#print(list31) 
for i in list26:
     regex=re.compile(r'[\n\r\t]')
     if(i.startswith("\n")):
        i= regex.sub("",i)
        list32.append(i)
        
     else:
        pass
#print(list32)    
for i in list28:
    string='https://www.sportspundit.com'
    string=string+i
    list29.append(string)
    string=""
newlist=[list(x) for x in zip(list32,list29)]
#print(newlist)
newssports1=dict(zip(list31,newlist))
#print(newssports1)
#############indianexpress sports news
list41=[]
list42=[]
list43=[]
list44=[]
list45=[]
ht_r = requests.get("https://indianexpress.com/section/sports/")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
ht_headings = ht_soup.findAll("div", {"class": "articles"})
#t_headings1=ht_soup.findALL("h2",{"class":"title"})
for i in ht_headings:
    for data in i.find_all("h2"):
        list41.append(data.text)
for i in ht_headings:
    for data in i.find_all("h2"):
         for link in data.find_all('a'):
            if link.has_attr('href'):
               list42.append(link.attrs['href'])

for i in ht_headings:
    for data in i.find_all('p'):
        list43.append(data.text)
        
for i in list41:
     regex=re.compile(r'[\n\r\t]')
     if(i.startswith("\n\t\t\t\t\t\t\t")):
        i= regex.sub("",i)
        list44.append(i)
        
     else:
        pass

for i in list43:
        regex=re.compile(r'[\n\r\t]')
 
        i= regex.sub("",i)
        list45.append(i)
        

newlist=[list(x) for x in zip(list45,list42)]

newssports2=dict(zip(list44,newlist))

items={}
items["Hindustan Times"]=newssports
items["Sportspundit"]=newssports1
items["IndianExpress"]=newssports2

# covid

list51=[]
list52=[]
list53=[]
list54=[]
ht_r = requests.get("https://www.hindustantimes.com/")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
ht_headings = ht_soup.findAll("div", {"class": "widget-inner loadable","id":"election0"})
ht_headings2 = ht_soup.findAll("div", {"class": "widget-inner loadable","id":"election1"})
ht_headings1 = ht_soup.findAll("a", {"class":"fll-covrge"})
for i in ht_headings:
    for link in i.find_all('a'):
            if link.has_attr('href'):
               list52.append(link.attrs['href'])
#print(list52)

for i in ht_headings1:
    for link in i.findAll("ul",{"id":"t2"}):
       
       for k in link.find_all("span"):
                list53.append((k.text))

for i in ht_headings1:
    for link in i.findAll("ul",{"id":"t1"}):
       
       for k in link.find_all("span"):
                list53.append((k.text))

for i in list52:
    list53.append(i)

#full dict
full_dict={}
full_dict['Times Of India']=toi_full_dict
full_dict['Hindustan TImes']=ht_full_dict
full_dict['BTC news']=crypt_full_dict

def index(req):
 return render(req, "ap1\index.html",{'ndtv_first5':ndtv_first5,'ht_top5':ht_first5,'toi_top5':toi_first5,'crypt_top5':crypt_first5})

def world(req):
  return render(req,"ap1\world.html",{'ndtv_trend':ndtv_trend,'inddict':inddict,'ndtv_dict':ndtv_dict,'world':world})

def sports(req):
  return render(req,"ap1\sports.html",{'sports':items})
def covid(req):
  return render(req,"ap1\covid.html",{'covid':list53})

def more(req):
  return render(req,"ap1\more.html",{'full_dict':full_dict})



