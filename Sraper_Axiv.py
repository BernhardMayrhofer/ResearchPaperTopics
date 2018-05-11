#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 10:52:39 2018

@author: user
"""
from bs4 import BeautifulSoup
import requests

def main():
  
  #start url
  url_ = 'https://arxiv.org/search/advanced?advanced=1&terms-0-operator=AND&terms-0-term=&terms-0-field=title&classification-eess=y&classification-physics_archives=all&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&size=100&order=&start='
  
  id_ = 0
  papers_ = []
  
  #get links to all subpages
  for id_ in range(0,1500,100): #2500
    
    print('Sprape Interval: ',str(id_))
  
    subpage_ = requests.get(url_ + str(id_))
    subsoup_ = BeautifulSoup(subpage_.content, 'html5lib')
      
    if 'Sorry, your query returned no results' in subsoup_:
      break
    
    for idx_ in range(0, len(subsoup_.find_all('p','authors'))):
            
      number_ = subsoup_.find_all('p','list-title level-left')[idx_].find('a').text
      author_ = subsoup_.find_all('p','authors')[idx_]
      author_ = author_.text.replace('\n', '').replace('Authors:', '').replace('  ', '').strip()
      dept_ = subsoup_.find_all('span','tag is-small is-link')[idx_].text
      paper_ = subsoup_.find_all('span','abstract-full has-text-grey-dark mathjax')[idx_]
      paper_ = paper_.text.replace('△ Less', '').replace('\n', '').strip()
      
      papers_.append([number_,author_,dept_,paper_])
   
  with open('papers.csv', 'w') as file_:
    for paper in papers_:
      file_.write('"'+paper[0]+'","'+paper[1]+'","'+paper[2]+'","'+paper[3]+'"\n')
     
  #return(papers_)
  
if __name__ == '__main__':
    main()