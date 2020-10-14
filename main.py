#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from fifo import *
from lru import *


def main():
    # Quadros que podem ser usados na memória RAM
    quad_vlr = int(sys.stdin.readline())

    referencias = map(int, sys.stdin.readlines())
 
    fifo = FIFO()
    fifoResul = fifo.execute(quad_vlr, referencias)


    lru = LRU()
    lruResul = lru.execute(quad_vlr, referencias)

    saida = 'Resultado por algoritmo:\nFIFO {0}\nLRU {1}'

    print(saida.format(fifoResul, lruResul))


if __name__ == "__main__":
    main()
