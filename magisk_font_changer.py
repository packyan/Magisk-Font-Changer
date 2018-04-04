# -*- coding: utf-8 -*-    
import os
debug = 0;
insert_line = 76 - 1 # from line - 1 to insert 
file_dir = "./system/fonts"
config_file_path = "./config.sh"
files_list = []
insert_str = "data"
process_flag = "#This file has benn processed by Magisk Fonts Changer -- Python\n"
def file_name(file_dir):   
    for root, dirs, files in os.walk(file_dir):  
        if debug :
        	print("path:") 
        	print(root)#当前目录路径  
        	print("sub path :") 
        	print(dirs)#当前路径下所有子目录  
        	print("files: " + str(type(files)))
        	print(files)#当前路径下所有非目录子文件  
        files_list.append(files)
file_name(file_dir)
insert_path = []
print("Processing")
insert_path.append(process_flag)
insert_path.append("REPLACE=\"\n")
for file in files_list[0]:
    insert_path.append("/system/fonts/" + str(file)+'\n')
insert_path.append("/system/etc/fonts.xml"+'\n')
insert_path.append("\"\n")

#copy config.sh to config_file
config_file = open(config_file_path)
lines = []
for line in config_file:
    lines.append(line)
config_file.close()
if(process_flag in lines):
    print("ERROR: This file has been processed, please chuck ./config.sh\n Operation Abort\n")
    exit()
for i in range(len(insert_path)):
    lines.insert(insert_line + i, insert_path[i])
s = ''.join(lines)
fp = open(config_file_path, 'w+')
fp.write(s)
fp.close()
print("All done")
