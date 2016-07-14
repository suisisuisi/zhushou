# -*- coding: utf-8 -*-
#!/usr/local/bin/python3
# 先做一个简单的不分片的文件上传
import sys
import os
import struct
import time
from sck import sck


sck = sck()
sck.connect("test.mm.com",5800)

for i in range(1,100):
    print (i)
    buffer = "BBBB"+str(i)+" are moments in life when you miss someone so much that you just want to pick them from your dreams and hug them for real! Dream what you want to dream;go where you want to go;be what you want to be,because you have only one life and one chance to do all the things you want to do."
    sendBufferLen = len(buffer)

    head = ""
    head += "filehash:dfasjfkjaskdfjksajdfkasjfkasj;"
    head += "chunkhash:dfasjfkjaskdfjksajdfkasjfkasj;"
    head += "size:20160714;"
    head += "authorizeToken:dfasjfkjaskdfjksajdfkasjfkasj;"
    head += "name:c语言入门.pdf;"
    head = head.encode(encoding="utf-8")

    data = struct.pack('!14s300s1I',
                       b'www.redocn.com',
                       head,
                       sendBufferLen)
    data += buffer.encode(encoding="utf-8")
    sck.send(data)
time.sleep(5)  # 休眠0.1秒