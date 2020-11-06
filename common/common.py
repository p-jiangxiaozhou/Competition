import os
import uuid
from datetime import datetime
import hashlib


def get_file_path(instance, filename):
    folder = datetime.now().strftime("%Y/%m/%d")
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(folder, filename)


def md5hex(word):
    """ MD5加密算法，返回32位小写16进制符号 """
    if isinstance(word, str):
        word = word.encode("utf-8")
    elif not isinstance(word, str):
        word = str(word)
    m = hashlib.md5()
    m.update(word)
    return m.hexdigest()
