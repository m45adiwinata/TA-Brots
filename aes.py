#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:04:15 2019

@author: bhaskaraby
"""

import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher(object):

    def __init__(self, key): 
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

if __name__ == '__main__':
    print('TESTING ENCRYPTION')
    msg = input('Message...: ')
    pwd = input('Password..: ')
    print('Ciphertext:', AESCipher(pwd).encrypt(msg).decode('utf-8'))

    print('\nTESTING DECRYPTION')
    cte = input('Ciphertext: ')
    #cte = AESCipher(pwd).encrypt(msg).decode('utf-8')
    pwd = input('Password..: ')
    print('Message...:', AESCipher(pwd).decrypt(cte))