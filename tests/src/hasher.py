import hashlib
import enum

BUFF_SIZE = 100000000  # 100 MB


class Type(enum.Enum):
    MD5 = 1
    SHA1 = 2


def hash(filepath, hash_type=Type.MD5):
    """
    return md5,sha1 hash of filepath
    """
    _sha1 = hashlib.sha1()
    _md5 = hashlib.md5()
    with open(filepath, encoding="utf-8") as f:
        while True:
            data = f.read(BUFF_SIZE)
            if data is None or data == "":
                break
            _md5.update(data.encode("utf-8"))
            _sha1.update(data.encode("utf-8"))
    return _md5 if hash_type == Type.MD5 else _sha1
