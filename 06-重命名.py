import os
files = input('请输入文件的名字:')

os.listdir(files)

#files = name.find('.')
'''
os.chdir(dic_name)
print(os.getcwd())
for file in files:
	position = file.rfind('.')
	new_nmae = file[:position]+'必属精品'+file[position:]
	os.rename(file,new_name)
'''


for file in files:
	position = file.rfind('.')
	new_name = file[:position]+'必输'+file[position:]
	old_name = files+'/'+file
	new_name = files+'/'+file
	os.rename(old_name,new_name)
