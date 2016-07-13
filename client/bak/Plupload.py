# -*- coding: utf-8 -*-
# 先做一个简单的不分片的文件上传
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2
register_openers()
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
    DONE = 5;


class Plupload:
    queue = []
    server = "http://test.yii.com/server/index.php"
    chunkSize = ''

    def __init__(self):

        pass

    def addFile(self, path):
        if os.access(path, os.F_OK) and os.access(path, os.W_OK):
            stat = os.stat(path)
            wfile = WFile()
            wfile.path = path
            wfile.size = stat.st_size
            wfile.atime = stat.st_atime
            wfile.name = os.path.basename(path)
            wfile.ext = os.path.splitext(path)[1]
            wfile.okfile = 1
            wfile.state = wfile.QUEUED
            self.queue.append(wfile)
        else:
            print('path not exists or not writeable')

    def start(self):
        self.uploadNext()

    def uploadNext(self):
        for wfile in self.queue:
            if wfile.state == wfile.QUEUED:
                wfile.state = wfile.UPLOADING
                self.uploadFile(wfile)
                break

    def uploadFile(self,wfile):
        try:
            print(wfile.name+"startd upload")
            params = {'file': open(wfile.path, "rb"),'name': wfile.name,'size':wfile.size,'lastModifiedDate':wfile.atime}
            datagen, headers = multipart_encode(params)
            request = urllib2.Request(self.server, datagen, headers)
            print wfile.size
            print request
            request.add_header('Cache-Control', 'no-cache')
            response_data = urllib2.urlopen(request)
            result = response_data.read()
            print result  # 如
            wfile.state = wfile.DONE
            if (wfile.state == wfile.DONE):
                self.uploadNext()

        except urllib2.HTTPError, e:
            #响应异常 404 500
            print e.code
            print e.read()
        except urllib2.URLError,e:
            #无网络连接（没有到目标服务器的路由,访问的目标服务器不存在
            print e.reason


    def  upload(self):


    def uploadNextChunk(self):

        pass
p = Plupload()
p.addFile("/Users/yongzi/Downloads/ceshi/examples.zip")
p.addFile("/Users/yongzi/Downloads/ceshi/架构之美.pdf")
p.start()
