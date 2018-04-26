# -*- coding: utf-8 -*-    
import os
debug = 0;
insert_line = 72 - 1 # from line - 1 to insert 
last_line = 0
file_dir = "./system/fonts"
config_file_path = "./config.sh"
place_holder1 = "./system/fonts/placeholder"
place_holder2 = "./system/etc/placeholder"
files_list = []
insert_str = "data"
process_flag = "#This file has benn processed by Magisk Font Changer -- Python\n"
def file_name(file_dir):   
    for root, dirs, files in os.walk(file_dir):  
        if debug :
        	print("path:") 
        	print(root)#current dir's path
        	print("sub path :") 
        	print(dirs)#sub floders path in this path
        	print("files: " + str(type(files)))
        	print(files)#all files in current path
        files_list.append(files)
print("Start Processing")
os.remove(place_holder1)
os.remove(place_holder2)
file_name(file_dir)
if len(files_list[0]) == 0:
	print("Fonts files have NOT copy to ./system/fonts folder, please check\n")
	exit()
insert_path = []
for file in files_list[0]:
    insert_path.append("/system/fonts/" + str(file)+'\n')
insert_path.append("/system/etc/fonts.xml"+'\n')


#copy config.sh to config_file
config_file = open(config_file_path)
lines = []
for line in config_file:
    lines.append(line)
config_file.close()
if(process_flag in lines):
    print("ERROR: This file has been processed, please check ./config.sh\n Operation Abort\n")
    exit()
lines.insert(insert_line - 2, process_flag)
for i in range(len(insert_path)):
	last_line = insert_line + i
	lines.insert(insert_line + i, insert_path[i])

s = ''.join(lines)
fp = open(config_file_path, 'w+')
fp.write(s)
fp.close()
print("All done")
