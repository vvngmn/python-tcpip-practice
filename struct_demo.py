# 基础知识十、Python解析网络报文之IP首部报文解析:
# https://blog.csdn.net/wang_xiaowang/article/details/105939251
# FORMAT	C TYPE	PYTHON TYPE	STANDARD SIZE
# B	unsigned char	integer	1字节
# H	unsigned short	integer	2字节
# L	unsigned long	integer	4字节
# s	char[]	string	~

import struct

mystr = 'ABCDEFGH'
bin_str = mystr.encode()
print(bin_str)
print(bin_str.decode())

print('>8B')
res = struct.unpack('>8B', bin_str)
print(res)
# (65, 66, 67, 68, 69, 70, 71, 72)

print('>4H')
res2 = struct.unpack('>4H', bin_str)
print(res2)
# (16706, 17220, 17734, 18248)

print('>2L')
res3 = struct.unpack('>2L', bin_str)
print(res3)
# (1094861636, 1162233672)

print('>8s')
res4 = struct.unpack('>8s', bin_str)
print(res4)
# (b'ABCDEFGH',)

