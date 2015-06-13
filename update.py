# -*- coding: UTF-8 -*-
import os
import time
import urllib2
import string


def getName():
    fSource = open('source.txt', 'r')
    names = fSource.readlines()
    name = {}
    i = 0
    while(i < len(names)):
        url_name = names[i][:names[i].find(' ')]
        caption_name = names[i][names[i].find(' '):].strip()
        name[url_name] = caption_name
        i += 1
    return name


head = open('head.txt','r').read()
tail = open('tail.txt','r').read()
#print head
time1 = time.strftime("%Y-%m-%d")
title = time1 + '.html'
fp = open(title, 'w+')
fp.write(head)



name = getName()
print name
for item in name.keys():
    fp.write('<h1><b>' + name[item].decode('GB2312').encode('utf-8') + '</br></b></h1>')
    url = 'http://chuansong.me/account/' + item
    request = urllib2.Request(url)
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36')
    con = urllib2.urlopen(request).read()
##    print con,
##    print item
##    f = open(item  + '.html','a')
##    f.write(con)

    
    href = con.find(r'question_link')
    html = con.find(r"id",href)
    target = con.find(r"target",html)
    end = con.find(r'&nbsp',target)
    timestamp = con.find('timestamp',end)
    span = con.find('span',timestamp)
    link = 'http://chuansong.me' + con[href + 21:html -2]
    caption = con[target + 16 : end - 5]
    time2 = con[timestamp + 31:span - 2]
    fp.write(r'<a href ="')
    fp.write(link)
    fp.write(r'" target="_blank">')
    fp.write(caption)
    fp.write(r'</a>&nbsp&nbsp' + time2 + '</br>')
    print link,
    print caption
    while(1):
        href = con.find('question_link',html)
        html = con.find("id",href)
        target = con.find(r"target",html)
        end = con.find(r'&nbsp',target)
        timestamp = con.find('timestamp',end)
        span = con.find('span',timestamp)
        if(href == -1):
           break
        else:
            link = 'http://chuansong.me' + con[href + 21:html -2]
            caption = con[target + 16 : end - 5]
            time2 = con[timestamp + 31:span - 2]
            fp.write(r'<a href ="')
            fp.write(link)
            fp.write(r'" target="_blank">')
            fp.write(caption)
            fp.write(r'</a>&nbsp&nbsp' + time2 + '</br>')
            print link,
            print caption
    time.sleep(3)

fp.write(tail)
fp.close()
