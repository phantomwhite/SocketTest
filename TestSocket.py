import socket
import struct
import json
import os
from os.path import join, getsize


def UploadInSocket(filename):
    HOST = '192.168.2.216'
    PORT = 54321
    ADDR = (HOST,PORT)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect(ADDR)
    except Exception as e:
        print(e)
    else:
        ver = 1
        p_type = 0

        cmd_t = 1
        pack_no = 0


        dicJson = {'access_token':'','chapterId':'', 'shareFlag':0,'fileName':'test1.bmp'
            ,'remark':''}
        dicJson['fileSize'] = getsize(filename)
        data_length = dicJson['fileSize']

        js = json.dumps(dicJson).encode('utf8')
        sub_len = len(js)

        struct_data = struct.pack('!bbHHHI%ds'%sub_len, ver,p_type,sub_len,cmd_t,pack_no,data_length,js)
        print(struct_data)

        s.send(struct_data)
        rec = s.recv(1024)
        print(rec)
        with open(filename, 'rb') as f:
            while True:
                filedata = f.read(512)
                if not filedata:
                    break

                s.send(filedata)


if __name__ == '__main__':
    UploadInSocket(r'f:\test1.bmp')