import hashlib

class crypt:
    def hashFile(self, path):
        f = ""
        err = False
        md5Str = ""
        try:
            f = open(path, 'rb')
            m = hashlib.md5()
            while True:
                bytes = f.read(2048)
                if not bytes:
                    break
                m.update(bytes)
            md5Str = m.hexdigest()
        except  Exception as err:
            print(err)
            err = True
        finally:
            if f:
                f.close()
        return err, md5Str

    def hashBlob(self, bytes):
        m = hashlib.md5()
        m.update(bytes)
        return m.hexdigest()
