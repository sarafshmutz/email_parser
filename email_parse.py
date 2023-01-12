#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import re
import sys

#url = 'https://www.mako.co.il/'

def email_parser(url, file_name, levels):
   links = [[url]]
   domain = url.split(".")
   domain=domain[-2:]
   print(domain)
                       

   for i in range(0,int(levels)-1):
      links_list=[]
     
      #print(links[i])
      for page in links[i]: 
         
         try:
         
            r = requests.get(page)
            soup = BeautifulSoup(r.content, 'html.parser')
            for link in soup.findAll('a'):
               url = link.get('href')
               if url not in links_list:
                  #print(url)
                  links_list.append(url)
            #print(len(links_list))
         except:
            pass 
      links.append(links_list)
     
      
               
         #         if domain in url:
          #           if url not in links_list:
           #                links_list.append(url)
            #               # url = "https://www." + domain + url
             #              links[i].append(url)
        
     # print(links[1])
          #     except:
           #       pass
     
   emails = []
   # all_links = [item for sublist in links for item in sublist]
   #counter=0        
   #print(links[1])
         
   for list in links:

     for url in list:
         
      try:
         
         r = requests.get(url)
         x = re.findall(
            r'([a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', r.text)
         for i in x:
            if "png" not in i and "jpg" not in i:
               if i not in emails:
                  print(i)
                  emails.append(i)
      except:
         pass         

   with open(file_name, 'w') as fp:
      for x in emails:
         fp.write(x)
         fp.write("\n")

# write a for loop instead of just x[0]

      
   # print(links_list)


def main():
    url = sys.argv[1]
    file_name = sys.argv[2]
    levels = sys.argv[3]
    email_parser(url, file_name, levels)


main()
