# -*- coding: utf-8 -*-
#!/usr/local/bin/python3
# 先做一个简单的不分片的文件上传
import sys

import os
import struct
from crypt import crypt
from sck import sck
import ConfigParser

class WFile:
    size = 0
    path = ''
    name = ''
    ext = ''
    guid = ''
    state = 0  # 0 等待上传 1准备上传计算md5 1上传中 2上传完成 3上传失败
    atime = 0
    okfile = 0
    percent = 0

    QUEUED = 1
    UPLOADING = 2
    FAILED = 4
    DONE = 5

# http://www.open-open.com/lib/view/open1398169869203.html python 读取配置文件
class plupload:
    queue = []
    cfg = ''
    sck = ''
    crypt = ''

    #程序的初始化
    def init(self):
        self.cfg = ConfigParser.ConfigParser()
        self.cfg.read("conf.ini")
        self.crypt = crypt()

    # some callback func well use later
    def fileAddedCallback(self, wfile):
        print(wfile.name + " added in queue")

    def beforeUploadCallback(self, wfile):
        print(wfile.name + " before upload")

    def __init__(self):
        self.init()
        self.initSck()


    def initSck(self):
        self.sck = sck()
        self.sck.connect(self.cfg.get('Server','addr'),int(self.cfg.get('Server','port')))



    # 发送文件 每次发送包含一个请求头(认证信息，文件描述，附加信息) + 文件流(具体文件内容)
    # token  token
    # filesize 文件大小
    # atime   创建时间
    # blk  块名称
    # chunk  片名称
    # chunkoffset  片偏移
    def _upload(self,wfile):
        f = ""
        sendBufferLen = 0
        try:
            messageLength = (wfile.size) # another 2 byte is '/r/n
            chunksize = int(self.cfg.get('Upload','chunksize'))
            f = open(wfile.path, 'rb')
            while True:

                if((messageLength - chunksize) > chunksize ):
                    sendBufferLen = chunksize
                else:
                    messageLength = messageLength - chunksize
                    sendBufferLen = messageLength
                bytes = f.read(sendBufferLen)
                if not bytes:
                    break
                else:
                    chunkhash = self.crypt.hashBlob(bytes)
                    fhead = ""
                    fhead += "filehash:"+wfile.hash+";"
                    fhead += "chunkhash:"+chunkhash+";"
                    fhead += "size:" + str(wfile.size) + ";"
                    fhead += "authorizeToken:" + wfile.hash + ";"
                    fhead += "name:"+wfile.name+";"

                    fhead = fhead.encode(encoding="utf-8")
                    data = struct.pack('!14s300s1I',
                                       b'www.redocn.com',
                                       fhead,
                                       sendBufferLen)
                    data += bytes
                    self.sck.send(data)

            wfile.state = WFile.DONE
            print('文件传输完毕')
        except  Exception as err:
            print(err)
        finally:
            if f:
                f.close()

    def onError(self, errCode, errMsg):
        print("[ERROR]"+str(errCode) + " "+errMsg)
        os._exit(0)


    # 添加文件
    def addFile(self, path):
        if os.access(path, os.F_OK) and os.access(path, os.W_OK):
            stat = os.stat(path)
            w = WFile()
            w.path = path
            w.size = stat.st_size
            w.atime = stat.st_atime
            w.name = os.path.basename(path)
            w.ext = os.path.splitext(path)[1]
            w.okfile = 1
            w.state = WFile.QUEUED
            self.queue.append(w)
            self.fileAddedCallback(w)
        else:
            print('path not exists or not writeable')

    # 开始上传
    def start(self):
        self.uploadNext()

    # 上传队列中下个文件
    def uploadNext(self):
        for wfile in self.queue:
            if wfile.state == WFile.QUEUED:
                wfile.state = WFile.UPLOADING
                self.uploadFile(wfile)
                break

    # before uplaod we will can Calculation the file MD5
    # or other things
    def beforeUpload(self, wfile):
        err,md5Str = self.crypt.hashFile(wfile.path)
        if not err:
            wfile.hash = md5Str
        self.beforeUploadCallback(wfile)
        pass

    # 上传文件
    def uploadFile(self, wfile):
        self.beforeUpload(wfile)
        self.uploadNextChunk(wfile)

        # if (file.state == file.DONE):
        #     self.uploadNext()

    # 上传下个分片
    def uploadNextChunk(self,wfile):
        # 我们先不考虑别的情况 直接实现socket发送文件
        self._upload(wfile)

        pass


p = plupload()
# p.addFile("E:/ceshi/5555.JPG")
# p.addFile("E:/ceshi/自然银 (2).JPG")
# p.addFile("/Users/yongzi/Downloads/ceshi/examples.zip")
p.addFile("/Users/yongzi/Downloads/架构之美.pdf")
p.start()
