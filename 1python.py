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
#----------------------xlrd-----------
import xlrd
import xlwt
from datetime import date,datetime
 
def read_excel():
  # 打开文件
  workbook = xlrd.open_workbook(r'E:\python\python.xlsx')
  # 获取所有sheet
  print (workbook.sheet_names()) # [u'sheet1', u'sheet2']
  sheet2_name = workbook.sheet_names()[1]
 
  # 根据sheet索引或者名称获取sheet内容
  sheet2 = workbook.sheet_by_index(1) # sheet索引从0开始
  sheet2 = workbook.sheet_by_name('Sheet1')
 
  # sheet的名称，行数，列数
  print (sheet2.name,sheet2.nrows,sheet2.ncols)
 
  # 获取整行和整列的值（数组）
  rows = sheet2.row_values(3) # 获取第四行内容
  cols = sheet2.col_values(2) # 获取第三列内容
  print (rows)
  print (cols)
 
  # 获取单元格内容
  print (sheet2.cell(1,0).value.encode('utf-8'))
  print (sheet2.cell_value(1,0).encode('utf-8'))
  print (sheet2.row(1)[0].value.encode('utf-8'))
   
  # 获取单元格内容的数据类型
  print (sheet2.cell(1,0).ctype)
 
if __name__ == '__main__':
  read_excel()
#---------------------print-------------
#参数sep是实现分隔符，比如多个参数输出时想要输出中间的分隔字符；关键字参数end是输出结束时的字符，默认是换行符\n
print(a,b,c.sep="\n-------\n",end = "\n")
#替换字符串中的部分信息，生成一个list
urls = ['Attractions-g60763-Activities-oa{}-New_York_City_New_York'.format(str(i)) for i in range(30,930,30)]

