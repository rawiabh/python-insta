
# coding: utf-8

# In[106]:


import json
import urllib.request as ur
import requests
from bs4 import BeautifulSoup
tag='tunisia'
URL = ('http://www.instagram.com/explore/tags/'+tag+'/?-a=1')
oururl= ur.urlopen(URL).read()
soup = BeautifulSoup(oururl,'lxml')
script = soup.select('script')
print(script[2])


# In[116]:


from lxml import html

r = requests.get(URL, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36"})
tree = html.fromstring(r.content)
script = tree.xpath('//script[contains(., "swc_market_lists")]/text()')
print(script)
import re

data = re.search(r"var swc_market_lists = (.*?);$", script).group(1)
print(data)


# In[103]:


print(data)

