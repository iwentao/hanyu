# /usr/bin/python
# coding: utf-8
# 
# Utility to convert chinese pinyin map dictionary
# 
# Wentao Sun (sunwt5@lenovo.com)
# 2023-8-31

import os, sys

def conv_to_pinyin_map(dict_file_name, dict_out_name, ignore_file_name):
  print(dict_file_name)
  f = open(dict_file_name, 'r', encoding = 'utf-8')
  o = open(dict_out_name, 'w', encoding = 'utf-8')
  
  ig = open(ignore_file_name, 'r', encoding = 'utf-8')
  ig_ls = ig.readlines()
  ig_lt = []
  for ig_line in ig_ls:
    ig_sline = ig_line.strip()
    ig_lt.append(ig_sline)
  
  print(len(ig_lt))
  lines = f.readlines()
  dict = {}
  for line in lines:
    s_line = line.strip()
    if s_line.startswith('#') or len(s_line) == 0:
      continue
    words = s_line.split('\t')
    chinese_word = words[0].strip()
    pinyin = words[1].strip()
    frequency = words[2].strip()
    
    if chinese_word in ig_lt:
      continue
    
    #print(words[0].strip())
    if pinyin not in dict.keys():
      dict[pinyin] = []
    
    dict[pinyin].append('%s/%s'%(chinese_word, frequency))
  
  ks = list(dict.keys())
  ks.sort()
  sorted_dict = {i : dict[i] for i in ks}
  
  dict_len = len(sorted_dict.items())
  print(dict_len)
  idx = 0
  for k, v in sorted_dict.items():
    #print(k, v)
    v_dict = {}
    for v_i in v:
      vv = v_i.split('/')
      v_chinese = vv[0].strip()
      v_frequency = int(vv[1].strip())
      if v_frequency not in v_dict.keys():
        v_dict[v_frequency] = []
      
      v_dict[v_frequency].append(v_chinese)
    
    #print(v_dict.keys())
    v_ks = list(v_dict.keys())
    v_ks.sort(reverse = True)
    v_sorted_dict = {j : v_dict[j] for j in v_ks}
    
    v_values = v_sorted_dict.values()
    v_value_list = []
    for v_value in v_values:
      v_value_list.append(''.join(v_value))
    str_values = ''.join(v_value_list)
    if idx < (dict_len - 1):
      o.write('{"%s"\t:"%s"},\n'%(k, str_values))
    else:
      o.write('{"%s"\t:"%s"}'%(k, str_values))
    idx = idx + 1
  f.close()
  o.close()
  

if __name__ == '__main__':
  print(sys.argv[0])
  dict_file_name = sys.argv[1]
  ignore_file_name = sys.argv[2]
  dict_out_name = 'pinyin_map.txt'
  conv_to_pinyin_map(dict_file_name, dict_out_name, ignore_file_name)