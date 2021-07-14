import struct

def cython_unpack(format, buf):
    struct.unpack(format, buf)

def cython_unpack_typed(str format, const unsigned char[:] buf):
    struct.unpack(format, buf)
