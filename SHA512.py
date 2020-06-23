import numpy as np
import math


Key=['0100001010001010001011111001100011010111001010001010111000100010',
 '0111000100110111010001001001000100100011111011110110010111001101',
 '1011010111000000111110111100111111101100010011010011101100101111',
 '1110100110110101110110111010010110000001100010011101101110111100',
 '0011100101010110110000100101101111110011010010001011010100111000',
 '0101100111110001000100011111000110110110000001011101000000011001',
 '1001001000111111100000101010010010101111000110010100111110011011',
 '1010101100011100010111101101010111011010011011011000000100011000',
 '1101100000000111101010101001100010100011000000110000001001000010',
 '0001001010000011010110110000000101000101011100000110111110111110',
 '0010010000110001100001011011111001001110111001001011001010001100',
 '0101010100001100011111011100001111010101111111111011010011100010',
 '0111001010111110010111010111010011110010011110111000100101101111',
 '1000000011011110101100011111111000111011000101101001011010110001',
 '1001101111011100000001101010011100100101110001110001001000110101',
 '1100000110011011111100010111010011001111011010010010011010010100',
 '1110010010011011011010011100000110011110111100010100101011010010',
 '1110111110111110010001111000011000111000010011110010010111100011',
 '0000111111000001100111011100011010001011100011001101010110110101',
 '0010010000001100101000011100110001110111101011001001110001100101',
 '0010110111101001001011000110111101011001001010110000001001110101',
 '0100101001110100100001001010101001101110101001101110010010000011',
 '0101110010110000101010011101110010111101010000011111101111010100',
 '0111011011111001100010001101101010000011000100010101001110110101',
 '1001100000111110010100010101001011101110011001101101111110101011',
 '1010100000110001110001100110110100101101101101000011001000010000',
 '1011000000000011001001111100100010011000111110110010000100111111',
 '1011111101011001011111111100011110111110111011110000111011100100',
 '1100011011100000000010111111001100111101101010001000111111000010',
 '1101010110100111100100010100011110010011000010101010011100100101',
 '0000011011001010011000110101000111100000000000111000001001101111',
 '0001010000101001001010010110011100001010000011100110111001110000',
 '0010011110110111000010101000010101000110110100100010111111111100',
 '0010111000011011001000010011100001011100001001101100100100100110',
 '0100110100101100011011011111110001011010110001000010101011101101',
 '0101001100111000000011010001001110011101100101011011001111011111',
 '0110010100001010011100110101010010001011101011110110001111011110',
 '0111011001101010000010101011101100111100011101111011001010101000',
 '1000000111000010110010010010111001000111111011011010111011100110',
 '1001001001110010001011001000010100010100100000100011010100111011',
 '1010001010111111111010001010000101001100111100010000001101100100',
 '1010100000011010011001100100101110111100010000100011000000000001',
 '1100001001001011100010110111000011010000111110001001011110010001',
 '1100011101101100010100011010001100000110010101001011111000110000',
 '1101000110010010111010000001100111010110111011110101001000011000',
 '1101011010011001000001100010010001010101011001011010100100010000',
 '1111010000001110001101011000010101010111011100010010000000101010',
 '0001000001101010101000000111000000110010101110111101000110111000',
 '0001100110100100110000010001011010111000110100101101000011001000',
 '0001111000110111011011000000100001010001010000011010101101010011',
 '0010011101001000011101110100110011011111100011101110101110011001',
 '0011010010110000101111001011010111100001100110110100100010101000',
 '0011100100011100000011001011001111000101110010010101101001100011',
 '0100111011011000101010100100101011100011010000011000101011001011',
 '0101101110011100110010100100111101110111011000111110001101110011',
 '0110100000101110011011111111001111010110101100101011100010100011',
 '0111010010001111100000101110111001011101111011111011001011111100',
 '0111100010100101011000110110111101000011000101110010111101100000',
 '1000010011001000011110000001010010100001111100001010101101110010',
 '1000110011000111000000100000100000011010011001000011100111101100',
 '1001000010111110111111111111101000100011011000110001111000101000',
 '1010010001010000011011001110101111011110100000101011110111101001',
 '1011111011111001101000111111011110110010110001100111100100010101',
 '1100011001110001011110001111001011100011011100100101001100101011',
 '1100101000100111001111101100111011101010001001100110000110011100',
 '1101000110000110101110001100011100100001110000001100001000000111',
 '1110101011011010011111011101011011001101111000001110101100011110',
 '1111010101111101010011110111111111101110011011101101000101111000',
 '0000011011110000011001111010101001110010000101110110111110111010',
 '0000101001100011011111011100010110100010110010001001100010100110',
 '0001000100111111100110000000010010111110111110010000110110101110',
 '0001101101110001000010110011010100010011000111000100011100011011',
 '0010100011011011011101111111010100100011000001000111110110000100',
 '0011001011001010101010110111101101000000110001110010010010010011',
 '0011110010011110101111100000101000010101110010011011111010111100',
 '0100001100011101011001111100010010011100000100000000110101001100',
 '0100110011000101110101001011111011001011001111100100001010110110',
 '0101100101111111001010011001110011111100011001010111111000101010',
 '0101111111001011011011111010101100111010110101101111101011101100',
 '0110110001000100000110011000110001001010010001110101100000010111']

def stringToBinary(s):
    return ' '.join('{0:08b}'.format(ord(x), 'b') for x in s)

def intToBinary(x, y):
    if y == 128:
        return "{0:0128b}".format(x)
    if y == 64:
        return "{0:064b}".format(x)

def xor(a, b):
    s = ''

    for i in range(len(b)):
        if a[i] == b[i]:
            s += '0'
        else:
            s += '1'
    return s

def RS187(s):
    x = xor(ROTR(s, 1), ROTR(s, 8))
    return xor(x, SHR(s, 7))

def ROTR(s, x):
    return s[len(s) - x:] + s[:len(s) - x]


def SHR(s, x):
    st = '0000000'
    return st[:x] + s[:len(s) - x]  # s[x:] + st[:x]

def RS19616(s):
    x = xor(ROTR(s, 19), ROTR(s, 61))
    return xor(x, SHR(s, 6))

def additionModulo(s1, s2):
    x = 0
    l1=len(s1)
    for i in range(l1):
        if s1[i] == '1':
            x += int(math.pow(2, len(s1) - 1 - i))

    y = 0
    l2=len(s2)
    for i in range(l2):
        if s2[i] == '1':
            y += int(math.pow(2, len(s2) - 1 - i))

    return intToBinary(int((x + y) % (2 ** 64)), 64)

def RA(m):
    x = xor(ROTR(m, 28), ROTR(m, 34))
    return xor(x, ROTR(m, 39))    

def maj(m, n, o):
    s = ''
    l=len(m)
    for i in range(l):
        s += str((int(m[i]) & int(n[i])) ^ (int(m[i]) & int(o[i])) ^ (int(n[i]) & int(o[i])))

    return s    

def conditional(m, n, o):
    s = ''
    l=len(m)
    for i in range(l):
        if m[i] == '1':
            s += n[i]
        else:
            s += o[i]

    return s

def RE(m):
    x = xor(ROTR(m, 14), ROTR(m, 18))
    return xor(x, ROTR(m, 41))        

def hexToBin(s):
    qw = bin(int(s, 16)).zfill(64)
    a, b = qw.split('b')

    l = len(b)

    for i in range(64 - l):
        b = '0' + b

    return b

def SHA512(message):
  bin_data = stringToBinary(message)

  #Padding
  bin_data=bin_data.replace(" ", "")
  length_message="{0:0128b}".format(len(bin_data))
  n = int((len(bin_data) + len(length_message)) % 1024)
  final_message=""
  if n == 0:
      final_message= bin_data + length_message
  else:
      final_message += bin_data+'1' + format(0, 'b').zfill(1024-1 - n) + length_message

  #So khoi tin
  N = int(len(final_message) / 1024)
  #Dau vao ban dau
  a = "0110101000001001111001100110011111110011101111001100100100001000"
  b = "1011101101100111101011101000010110000100110010101010011100111011"
  c = "0011110001101110111100110111001011111110100101001111100000101011"
  d = "1010010101001111111101010011101001011111000111010011011011110001"
  e = "0101000100001110010100100111111110101101111001101000001011010001"
  f = "1001101100000101011010001000110000101011001111100110110000011111"
  g = "0001111110000011110110011010101111111011010000011011110101101011"
  h = "0101101111100000110011010001100100010011011111100010000101111001"
  prea=a; preb=b; prec=c; pred=d; pree=e; pref=f; preg=g; preh=h
  
  for i in range(N):
    M = ''
    M += final_message[i * 1024:(i + 1) * 1024]

    #Word Expansion
    W=[]
    for j in range(16):
      W.append(M[j*64 : (j + 1)*64])
    for j in range(16, 80):
      st = ''
      st += additionModulo(RS19616(W[j - 2]), RS187(W[j - 15]))
      st = additionModulo(st, W[j - 7])
      st = additionModulo(st, W[j - 16])
      W.append(st)


    #80 Round
    for j in range(80):
      tron1 = additionModulo(RA(a), maj(a, b, c))

      tron2 = additionModulo(h, conditional(e, f, g))
      tron2 = additionModulo(tron2, RE(e))
      tron2 = additionModulo(tron2, W[j])    
      tron2 = additionModulo(tron2, Key[j])    
      
      h = g
      g = f
      f = e
      e = additionModulo(d, tron2)
      d = c
      c = b
      b = a
      a = additionModulo(tron1, tron2)

    #Cong modulo voi H truoc do  
    a= additionModulo(prea, a)
    b= additionModulo(preb, b)
    c= additionModulo(prec, c)
    d= additionModulo(pred, d)
    e= additionModulo(pree, e)
    f= additionModulo(pref, f)
    g= additionModulo(preg, g)
    h= additionModulo(preh, h)
    prea=a; preb=b; prec=c; pred=d; pree=e; pref=f; preg=g; preh=h;
  
  H = a + b + c + d + e + f + g + h
  result = ''
  for i in range(128):
    p, qw = hex(int(H[i * 4:(i + 1) * 4], 2)).split('x')
    result += qw
  return result