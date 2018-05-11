#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 11:54:57 2018

@author: user
"""

import csv
from collections import Counter

def main():
  
  papers_ = []
  
  with open('papers.csv', 'r') as csvfile:
      for line in csv.reader(csvfile, delimiter=',', quotechar='"'):
          papers_.append(line)
            
  words_ = ''
  
  for line in papers_:
    words_ += line[3]
    
  words_ = words_.replace(',','').\
                replace('.','').\
                replace('(','').\
                replace(')','')
    
  #print(words_)
  dict_ = []
  
  dict_ = Counter(words_.split()).most_common()
  
  with open('dictnostops_raw.txt', 'w') as file_:
    for word in dict_:
      file_.write('"'+word[0]+'","'+str(word[1])+'"\n')
            
if __name__ == '__main__':
    main()