#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     :2020/9/22
# @Author   :PeterJoin
from __future__ import print_function

#11 111 010 000 0 1010 111 100 0 00 000 000 111 00 10 1 0 010 0 000 1 00 10 110

#摩斯电码转ASCII码字典
dict = {'01': 'A',
        '1000': 'B',
        '1010': 'C',
        '100':'D',
        '0':'E',
        '0010':'F',
        '110': 'G',
        '0000': 'H',
        '00': 'I',
        '0111':'J',
        '101': 'K',
        '0100': 'L',
        '11': 'M',
        '10': 'N',
        '111': 'O',
        '0110': 'P',
        '1101': 'Q',
        '010': 'R',
        '000': 'S',
        '1': 'T',
        '001': 'U',
        '0001': 'V',
        '011': 'W',
        '1001': 'X',
        '1011': 'Y',
        '1100': 'Z',
        '01111': '1',
        '00111': '2',
        '00011': '3',
        '00001': '4',
        '00000': '5',
        '10000': '6',
        '11000': '7',
        '11100': '8',
        '11110': '9',
        '11111': '0',
        '001100': '?',
        '10010': '/',
        '101101': '()',
        '100001': '-',
        '010101': '.',
        '110011':',',
        '011010':'@',
        '111000':':',
        '101010':':',
        '10001':'=',
        '011110':"'",
        '101011':'!',
        '001101':'_',
        '010010':'"',
        '10110':'(',
        '1111011':'{',
        '1111101':'}'
        };

def banner():
    print(("""%s
 __  __  ___  ____  ____  _____ 
|  \/  |/ _ \|  _ \/ ___|| ____|
| |\/| | | | | |_) \___ \|  _|  
| |  | | |_| |  _ < ___) | |___ 
|_|  |_|\___/|_| \_\____/|_____|
                                                               %s%s
        # Coded By PeterJoin -  你这个小猪怎么还不约我（´・ω・）%s
    """ % ('\033[91m', '\033[0m', '\033[93m', '\033[0m')))



if __name__ == '__main__':
    banner()
    inputString = input("input the string:")
    s = inputString.split(" ")
    for item in s:
        print (dict[item],end='')
