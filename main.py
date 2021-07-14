import struct
import timeit

N = 100000
FORMAT = '>qqqq'

def create_buffer():
    packed = struct.pack(FORMAT, *(41, 42, 43, 44))
    return memoryview(packed)

def plain_unpack(buf):
    struct.unpack(FORMAT, buf)

def main():
    setup = """
from __main__ import (
    create_buffer,
    plain_unpack,
)
buf = create_buffer()"""

    tests = [
        ("plain unpack()", "plain_unpack({})"),
    ]

    print("---------------------------------------------")
    print("Test Name                      Time (s)")
    print("---------------------------------------------")
    for test_name, test_snippet in tests:
        print("{:30} {:>4.3f}".format(test_name, timeit.timeit(test_snippet.format("buf"), setup=setup, number=N)))

if __name__ == '__main__':
    main()
