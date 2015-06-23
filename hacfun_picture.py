# -*- coding: utf-8 -*-  
#---------------------------------------  
#---------------------------------------  
   
import urllib, re , time
# localpath 本地保存路径  自行更改 
localpath='F:/reptile/'

#定义函数  
def nimingban(url,begin_page,end_page):     
    for i in range(begin_page, end_page+1):  
        print i
        html = getHtml(url + str(i));
        imglist =   getImg(html)
        x = 100*i+0
        for imgurl in imglist:
            if(x%100!=0):
                print '------------------------------------------------------------------'
                print '源网址 :                              ' + imgurl
 #url 缩略图和大图
                if "thumb"  in imgurl:
                    imgurl = imgurl.replace('/thumb','/image')
                if "th"  in imgurl:
                    imgurl = imgurl.replace('/th','')
                
                #imgurl = imgurl.replace('/th','/images')
               # print imgurl
                print (time.strftime("%H:%M:%S"))
                print '第 ' + str(i) +' 页  正在下载 文件名: ' + str(x) +' '+ imgurl
                urllib.urlretrieve(imgurl,localpath+'%s.jpg' % x)
            x+=1
            
        if(i==end_page):
             print '-----------------end-------------------------'
             while(True):
                 print '\a'*7
               
     
        
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html   
    

def getImg(html):
    reg = r'data-src="(.+?\.jpg)" src='
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist         
    
    
myurl = str(raw_input(u'请输入匿名版的地址，去掉page=后面的数字：\n'))  
begin_page = int(raw_input(u'请输入开始的页数：\n'))  
end_page = int(raw_input(u'请输入终点的页数：\n'))  
num =str(raw_input(u'请输入串号：\n'))  

#num = '5739391'
#begin_page = 1
#end_page = 14

myurl = 'http://h.nimingban.com/t/'+num+'?page='

print '----------------------go---------------------------'


nimingban(myurl,begin_page,end_page)