# /usr/bin/python
# coding: utf-8
# 
# Utility to convert chinese pinyin map dictionary
# 
# Wentao Sun (sunwt5@lenovo.com)
# 
# 2023-9-1
# 2023-9-4 add chinese character encoding to check its length
#          for normal chinese, its length is 3
#          for those special chinese, its length is 4

import os, sys

def conv_to_hanzi(dict_file_name, dict_out_name, dict_out_dup_remove_name, dict_out_ignore_name, dict_out_remove_ignore_name):
  f = open(dict_file_name, 'r', encoding = 'utf-8')
  o = open(dict_out_name, 'w', encoding = 'utf-8')
  odp = open(dict_out_dup_remove_name, 'w', encoding = 'utf-8')
  oi = open(dict_out_ignore_name, 'w', encoding = 'utf-8')
  ori = open(dict_out_remove_ignore_name, 'w', encoding = 'utf-8')
  
  lines = f.readlines()
  
  dict = set() # work as set, remove duplication automatically
  ig_set = set()
  ori_set = set()
  idx = 0
  line_len = len(lines)
  print(line_len)
  for line in lines:
    s_line = line.strip()
    idx = idx + 1
    if s_line.startswith('#') or len(s_line) == 0:
      continue
    words = s_line.split('\t')
    chinese_word = words[0].strip()
    o.write('%s%s'%(chinese_word, len(chinese_word.encode('utf8'))))
    if len(chinese_word.encode('utf8')) > 3:
      ig_set.add(chinese_word)
    else:
      ori_set.add(chinese_word)
    
    dict.add(chinese_word)
    
    if idx < line_len:
      o.write('\n')
  
  odp.writelines('\n'.join(list(dict)))
  oi.writelines('\n'.join(list(ig_set)))
  ori.writelines('\n'.join(list(ori_set)))
  
  f.close()
  o.close()
  odp.close()
  oi.close()
  ori.close()
  
if __name__ == '__main__':
  print(sys.argv[0])
  dict_file_name = sys.argv[1]
  dict_out_name = 'hanzi_spec.txt'
  dict_out_dup_remove_name = 'hanzi_dup_remove.txt'
  dict_out_ignore_name = 'hanzi_to_ignore.txt'
  dict_out_remove_ignore_name = 'hanzi_remove_ignore.txt'
  conv_to_hanzi(dict_file_name, dict_out_name, dict_out_dup_remove_name, dict_out_ignore_name, dict_out_remove_ignore_name)