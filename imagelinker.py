import urllib
import re
print "enter the url of the website"

url=raw_input(">>>")
website=urllib.urlopen(url)
html=website.read()
pattern=r'<imgsrc=\"(.*?)\"'
pattern=re.compile(pattern)
links=re.findall(pattern,str(html))
print "enter the name of the file"
file=raw_input(">>>")
newfile=open(file,"w")
print "here u go! the link of the images"
for links in links:
		print url,links
		i=url+links
		newfile.write(str(i))
print "all the links are copied" +str(file)
newfile.close()




