
#coding:utf-8
# https://github.com/land-pack/jtt808/blob/master/simulate/terminal.py
# python D:\python-scripts\tcp-808client.py

from socket import *
import binascii, struct
import tongue


class TcpClient:
    HOST = '127.0.0.1'
    PORT = 8877
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    def __init__(self):
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect(self.ADDR)

        # 查询时间 '7E 00 04 40 00 01 00 00 00 00 01 55 55 55 55 55 00 24 35 7E'
        # 模拟器返回 [RECV] 7E 80 01 00 05 01 00 00 00 00 01 36 81 00 10 01 00 00 FF FF 01 02 00 21 7E
        # 服务器端log 通过模拟器=脚本 = 8001000501000000000136810010010000ffff01020021
        # 代码返回 7E 80 01 00 05 01 00 00 00 00 01 36 81 00 10 01 00 00 FF FF 01 02 00 21 7E
        self.register_data = '2323010034364637415334473136354634395344380100e6150a1010022100013839383630303233303330393730303033373236140a484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f46484a4b4c41534446485541494c48465549414f4682'
        
        self.packed_data = binascii.unhexlify(self.register_data)
        print('\n packed_data: ')
        print(type(self.packed_data))
        print(self.packed_data) 


        self.client.send(self.packed_data)
        recv_data = self.client.recv(self.BUFSIZ)
        print('\n recv_data: ')
        print(recv_data) 


        recv_decoded_data = tongue.Decode(recv_data)
        print('\n tongue decoded: ') 
        print(recv_decoded_data.dst) 
        #recv_decoded_data.dst : 十六进制用十进制表示 (126, 128, 1, 0, 5, 1, 0, 0, 0, 0, 1, 54, 129, 0, 16, 1, 0, 0, 255, 255, 1, 2, 0, 33, 126)
        l = [hex(i) for i in recv_decoded_data.dst] # 还原十六进制
        r = []
        for i in l:
            if len(i) == 3: r.append(i.replace('x','').upper())
            if len(i) == 4: r.append(i.replace('0x','').upper())
        result = ' '.join(r)
        print(result)



if __name__ == '__main__':
    client = TcpClient()