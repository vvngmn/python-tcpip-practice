#coding:utf-8
# Python Version:3.5.1
import socket
import time
import struct
import json

# # 32960
# host = "10.170.58.224"
# port = 8877

# JT808
# host = "10.170.58.100"
# port = 8866

# ADDR = (host, port)

if __name__ == '__main__':
  # client = socket.socket()
  # client.connect(ADDR)

  # 32960 车辆登入
  data = '2323010034364637415334473136354634395344380100e6150a1010022100013839383630303233303330393730303033373236140a484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f4682'
  
  # # JT808 数据
  # body = '80 01 00 05 01 00 00 00 00 01 36 81 00 10 01 00 00 FF FF 01 02 00 21'
  l = []
  for i in body.split(' '): l.append((r"\x"+i).replace(u"\\x", u"\\\x"))
  # hex_data = ''.join(l)
  print(l)

  # id = '0100'.encode()
  # bodyProp = '0022'.encode()
  # prototypeVersion = '01'.encode()
  # phone = '35000000040001000B04'.encode()
  # msgNum = '4D31'.encode()
  # provinceId = '3233'.encode()
  # cityId = '3435'.encode()
  # manufactor = '4142313233343536413131'.encode()
  # terminalClient = '3232333300E7B2A4423131313135'.encode()

  # message = ['7E', id, bodyProp, prototypeVersion, phone, msgNum, provinceId, cityId, manufactor, terminalClient,'7E']
  # print(*message)
  # data = struct.pack("!11", *message)

  # 
  # while True:
  #   client.send( body.encode())
  #   print ('sent')
  #   res = client.recv(1)
  #   print(res)
  #   time.sleep(1)


  # sendData1 = data.encode()
  # res = client.recv(1024)
  # print(res)

#   # 分包数据定义
#   ver = 2
#   body = json.dumps(dict(hello="world2"))
#   print(body)
#   cmd = 102
#   header = [ver, body.__len__(), cmd]
#   headPack = struct.pack("!3I", *header)
#   sendData2_1 = headPack+body[:2].encode()
#   sendData2_2 = body[2:].encode()

#   # 粘包数据定义
#   ver = 3
#   body1 = json.dumps(dict(hello="world3"))
#   print(body1)
#   cmd = 103
#   header = [ver, body1.__len__(), cmd]
#   headPack1 = struct.pack("!3I", *header)

#   ver = 4
#   body2 = json.dumps(dict(hello="world4"))
#   print(body2)
#   cmd = 104
#   header = [ver, body2.__len__(), cmd]
#   headPack2 = struct.pack("!3I", *header)

#   sendData3 = headPack1+body1.encode()+headPack2+body2.encode()


#   # 正常数据包
#   client.send(sendData1)
#   time.sleep(3)

#   # 分包测试
#   client.send(sendData2_1)
#   time.sleep(0.2)
#   client.send(sendData2_2)
#   time.sleep(3)

#   # 粘包测试
#   client.send(sendData3)
#   time.sleep(3)
#   client.close()

# struct.unpact('H','/0x232302014C413945434343343647534E5344303031010001004F')
