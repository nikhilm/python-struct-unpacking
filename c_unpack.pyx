import struct

def cython_unpack(format, buf):
    struct.unpack(format, buf)

def cython_unpack_from(format, buf):
    struct.unpack_from(format, buf, 0)

def cython_unpack_typed(str format, const unsigned char[:] buf):
    struct.unpack(format, buf)

def get_compiled_struct_obj(format):
    return struct.Struct(format)

def cython_compiled_unpack(struct_obj, buf):
    struct_obj.unpack(buf)
