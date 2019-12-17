#!/usr/bin/env python3
# encoding: utf-8

dict = {'%':'%25','-':'%2D','.':'%2E','/':'%2F',':':'%3A','=':'%3D'}

def encode_url(s):
    result = []
    for i in s:
        try:
            result.append(dict[i])
        except:
            result.append(i)
    return result
def encode_sec(s):
    for i in range(len(s)):
        if '%' in s[i]:
            s[i]='%25'+s[i].replace('%','')
        print(s[i],end='')

if __name__ == '__main__':
    payload = input("Please give string to encode: ")
    encode_sec(encode_url(payload))
