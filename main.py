import struct
import sys
import timeit

N = 1000000
FORMAT = '>qqqq'

def create_buffer():
    packed = struct.pack(FORMAT, *(41, 42, 43, 44))
    return memoryview(packed)

def plain_unpack(buf):
    struct.unpack(FORMAT, buf)

def compiled_unpack(struct_obj, buf):
    struct_obj.unpack(buf)

def plain_unpack_from(buf):
    struct.unpack_from(FORMAT, buf, 0)

def main():
    setup = """
import struct

from __main__ import (
    create_buffer,
    plain_unpack,
    plain_unpack_from,
    compiled_unpack,
)
from c_unpack import (
    cython_unpack,
    cython_unpack_from,
    cython_unpack_typed,
    cython_compiled_unpack,

    get_compiled_struct_obj,
)

buf = create_buffer()
struct_obj = struct.Struct('{format}')
cython_struct_obj = get_compiled_struct_obj('{format}')""".format(format=FORMAT)

    tests = [
        ("plain unpack()", "plain_unpack({})"),

        ("plain unpack_from()", "plain_unpack_from({})"),
        ("cython unpack()", "cython_unpack('{}', {{}})".format(FORMAT)),
        ("cython unpack_from()", "cython_unpack_from('{}', {{}})".format(FORMAT)),
        ("cython typed unpack()", "cython_unpack_typed({}('{}'), {{}})".format('unicode' if sys.version_info.major == 2 else 'str', FORMAT, '')),

        ("plain compiled unpack()", "compiled_unpack(struct_obj, {})"),
        ("cython compiled unpack()", "cython_compiled_unpack(cython_struct_obj, {})"),
    ]

    print("---------------------------------------------")
    print("Test Name                      Time (s)")
    print("---------------------------------------------")
    baseline = 0
    for i, (test_name, test_snippet) in enumerate(tests):
        took = timeit.timeit(test_snippet.format("buf"), setup=setup, number=N)
        if i == 0:
            baseline = took
            print("{:30} {:>4.3f}".format(test_name, took))
        else:
            print("{:30} {:>4.3f} ({:>+.2%})".format(test_name, took, took / baseline))

if __name__ == '__main__':
    main()
