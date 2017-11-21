dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
 
print ("字典值 : %s" %  dict.items())
 
# 遍历字典列表
for key,values in  dict.items():
    print (key,values)

#----------------------time----------------------    
import time

# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) )


#----------------------time----------------------    
dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
 
print ("字典值 : %s" %  dict.items())
 
# 遍历字典列表
for key,values in  dict.items():
    print (key,values)

#--------------------i/o--------------------
fo = open("foo.txt", "wb")
print ("文件名: ", fo.name)
print ("是否已关闭 : ", fo.closed)
print ("访问模式 : ", fo.mode)

fo.write( "www.runoob.com!\nVery good site!\n");

#--------------------i/o--------------------
# 打开一个文件
fo = open("foo.txt", "w+")
fo.write('abcdefg')
#把指针再次重新定位到文件开头
position = fo.seek(0, 0);
str = fo.read(10);
print ("读取的字符串是 : ", str)
 
# 查找当前位置
position = fo.tell();
print ("当前文件位置 : ", position)
 
# 把指针再次重新定位到文件开头
position = fo.seek(0, 0);
str = fo.read(10);
print ("重新读取字符串 : ", str)
#查看变量

print('tell' ,fo.tell())
print('seek' ,fo.seek(0, 0))
# 关闭打开的文件
fo.close()