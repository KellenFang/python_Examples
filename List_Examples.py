#创建列表
sample_list = ['a',1,('a','b')]

#得到列表中的某一个值
value_start = sample_list[0] #[]内的值自定义sample_list的序列号
end_value = sample_list[-1]

#del删除列表的某一个值
del sample_list[0]  #[]内的值自定义sample_list的序列号
#clear清除列表中所以元素
sample_list.clear()
#pop 移除列表中的最后一个元素，默认是最后一个
sample_list.pop()
#remove 移除列表中第一个匹配的元素
sample_list.remove(2)

#在列表中插入一个值
sample_list[0:0] = ['sample value']
#append向列表末尾追加一个元素
sample_list.append(4)
#insert 将对象插入列表中
sample_list.insert(0,0)
#extend 直接向列表末尾一次性追加另一个列表
mum = [1,2,3]
sample_list.extend(mum)

#得到列表的长度
list_length = len(sample_list)

#copy 复制一个列表，并赋值num
mum = sample_list.copy()

#count统计某个元素在列表中的次数
sample_list.count('a')

#index 从列表中找出某个值第一个匹配的索引位置
sample_list.index(3)

#reverse 将列表中的元素反向存放
sample_list.reverse()

#sort 对列表排序
one = [4,2,5,1,6,8,5,9,0]
one.sort()
#根据key函数为元素产生一个键，列表的元素按照这个键值来排序
tow = ['abc','a','bc','abcd']
tow.sort(key=len)
#反向排序
one.sort(reverse=True)

# in 判断值是否存在列表，存在返回True,反之False
mums = [1,1,1,2,2,2,3,3,3,]
1 in mums
5 in mums

#将一个列表的值复制到另一个新的列表
kes = [1,2,3,4]
kos = kes.copy()#列表 copy() 函数
kcs = list(kes)#list() 转换函数
kds = kes[:]#列表分片 [:]


#列表遍历(打印列表数据)
for element in sample_list:
    print(element)
