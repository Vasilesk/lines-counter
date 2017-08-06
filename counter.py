#!/usr/bin/python3
# -*- coding: utf8 -*-

import io, sys
from functools import reduce

buffer_size = io.DEFAULT_BUFFER_SIZE * 1024
code_newline = 10

def count_lines(bytes_iter):
    return reduce(
            lambda buf_counter, elem: buf_counter if elem != code_newline else buf_counter + 1,
            bytes_iter,
            0
        )

if __name__ == "__main__":
    if len(sys.argv) == 1:
        count = count_lines(sys.stdin.buffer.read())
        print(count)
    else:
        many_files = len(sys.argv) > 2
        total_count = 0
        for filename in sys.argv[1:]:
            with open(filename, 'rb') as f:
                counter = 0

                buffered = f.read(buffer_size)
                while buffered != b'':
                    counter += count_lines(buffered)
                    buffered = f.read(buffer_size)

                if many_files:
                    print("% 7d %s" % (counter, sys.argv[1]))
                    total_count += counter
                else:
                    print(counter, sys.argv[1])

        if many_files:
            print("% 7d %s" % (total_count, 'итого'))
