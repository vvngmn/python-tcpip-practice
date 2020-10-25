#coding:utf-8
#常量定义类

# 命令标识
class CmdB1:
	cmdDict = {
		'车辆登入':{'code':b'\x01', 'stream' : 'up'} , \
		'实时信息上报':{'code':b'\x02', 'stream' : 'up'} , \
		'补发信息上报':{'code':b'\x03', 'stream' : 'up'} , \
		'车辆登出':{'code':b'\x04', 'stream' : 'up'} , \
		'平台登入':{'code':b'\x05', 'stream' : 'up'} , \
		'平台登出':{'code':b'\x06', 'stream' : 'up'}

	}

