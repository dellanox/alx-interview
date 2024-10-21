#!/usr/bin/env python3
""" reads stdin line by line and computes metrics
"""

import sys


def main():
    """ Entry point
    """
    var = {}
    file_size = 0
    try:
        for i, line in enumerate(sys.stdin):
            *parse, = line.split(" ")
            ip, _, date, time, method, directory, protocol, s_code, f_size, *r = parse

            if len(r) > 0 or len(s_code) < 3 or not s_code:
                try:
                    int(s_code)
                except ValueError:
                    continue
                continue
            if not var.get(s_code, None):
                var[s_code] = 1
            else:
                var[s_code] += 1
            file_size += int(f_size)
            
            if (i + 1) % 10 == 0:
                print(f"File size: {file_size}")
                for x in sorted(var):
                    print(f"{x}: {var[x]}")

    except KeyboardInterrupt:
        print(var)

main()
