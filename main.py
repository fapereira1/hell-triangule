#!/usr/bin/python
from hell_triangule import HellTriangule
import time

def main():
    table = [map(int, s.split()) for s in open('test_case2.in').readlines()]

    hell_triangule = HellTriangule(table)
    sum = hell_triangule.hell_triangule()
    print sum
if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))