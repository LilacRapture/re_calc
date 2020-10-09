class MetaString(str):
    def __new__(cls, value, meta):
        obj = str.__new__(cls, value)
        obj.meta = meta
        return obj


class MetaFloat(float):
    def __new__(cls, value, meta):
        obj = float.__new__(cls, value)
        obj.meta = meta
        return obj


class MetaList(list):
    def __init__(self, coll=(), meta=None):
        self.meta = meta
        super().__init__(coll)


def pack(v, meta):
    if isinstance(v, str):
        return MetaString(v, meta)
    elif isinstance(v, float):
        return MetaFloat(v, meta)
    else:
        return v


def pack_list(v, meta):
    return MetaList(v, meta)


def set_meta_indices(lst):
    return [pack(x, idx) for idx, x in enumerate(lst)]
