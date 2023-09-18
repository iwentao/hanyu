# /usr/bin/python
# coding: utf-8
# 
# Utility to convert chinese pinyin map dictionary
# 
# Wentao Sun (sunwt5@lenovo.com)
# 2023-9-1

import os, sys

def conv_to_hanzi(dict_file_name, dict_out_name):
  f = open(dict_file_name, 'r', encoding = 'utf-8')
  o = open(dict_out_name, 'w', encoding = 'utf-8')
  lines = f.readlines()
  dict = {}
  for line in lines:
    s_line = line.strip()
    if s_line.startswith('#') or len(s_line) == 0:
      continue
    words = s_line.split('\t')
    chinese_word = words[0].strip()
    o.write('%s\n'%chinese_word)
  
  f.close()
  o.close()
  
if __name__ == '__main__':
  print(sys.argv[0])
  dict_file_name = sys.argv[1]
  dict_out_name = 'hanzi.txt'
  conv_to_hanzi(dict_file_name, dict_out_name)