# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 17:40:07 2018

@author: Dv00
"""

class Des:
    
    __sBoxes = [
    	[
    		[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    		[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    		[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    		[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    	],
    	[
    		[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    		[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    		[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    		[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    	],
    	[
    		[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    		[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    		[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    		[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    	],
    	[
    		[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    		[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    		[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    		[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    	],
    	[
    		[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    		[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    		[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    		[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    	],
    	[
    		[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    		[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    		[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    		[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    	],
    	[
    		[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    		[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    		[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    		[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    	],
    	[
    		[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    		[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    		[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    		[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    	]
    ]
    
    
    __IP = [
    	57, 49, 41, 33, 25, 17, 9,  1,
		59, 51, 43, 35, 27, 19, 11, 3,
		61, 53, 45, 37, 29, 21, 13, 5,
		63, 55, 47, 39, 31, 23, 15, 7,
		56, 48, 40, 32, 24, 16, 8,  0,
		58, 50, 42, 34, 26, 18, 10, 2,
		60, 52, 44, 36, 28, 20, 12, 4,
		62, 54, 46, 38, 30, 22, 14, 6
	]
    
    
    __inverseIP = [
		39,  7, 47, 15, 55, 23, 63, 31,
		38,  6, 46, 14, 54, 22, 62, 30,
		37,  5, 45, 13, 53, 21, 61, 29,
		36,  4, 44, 12, 52, 20, 60, 28,
		35,  3, 43, 11, 51, 19, 59, 27,
		34,  2, 42, 10, 50, 18, 58, 26,
		33,  1, 41,  9, 49, 17, 57, 25,
		32,  0, 40,  8, 48, 16, 56, 24
	]
    
    
    __EExpansion = [
        31,  0,  1,  2,  3,  4,
        3,  4,  5,  6,  7,  8,
        7,  8,  9, 10, 11, 12,
        11, 12, 13, 14, 15, 16,
        15, 16, 17, 18, 19, 20,
        19, 20, 21, 22, 23, 24,
        23, 24, 25, 26, 27, 28,
        27, 28, 29, 30, 31,  0
    ]
    
    __PSubstitute = [
        15, 6, 19, 20,
        28, 11, 27, 16,
        0, 14, 22, 25,
        4, 17, 30, 9,
        1, 7, 23, 13,
        31, 26, 2, 8,
        18, 12, 29, 5,
        21, 10, 3, 24
    ]
    
    __PC1 = [
        56, 48, 40, 32, 24, 16,  8,
        0, 57, 49, 41, 33, 25, 17,
		  9,  1, 58, 50, 42, 34, 26,
        18, 10,  2, 59, 51, 43, 35,
        62, 54, 46, 38, 30, 22, 14,
        6, 61, 53, 45, 37, 29, 21,
        13,  5, 60, 52, 44, 36, 28,
        20, 12,  4, 27, 19, 11,  3
    ]
    
    __PC2 = [
		13, 16, 10, 23,  0,  4,
		 2, 27, 14,  5, 20,  9,
		22, 18, 11,  3, 25,  7,
		15,  6, 26, 19, 12,  1,
		40, 51, 30, 36, 46, 54,
		29, 39, 50, 44, 32, 47,
		43, 48, 38, 55, 33, 52,
		45, 41, 49, 35, 28, 31
	]

    __leftRotation = [
        1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
    ]


    ENCRYPT = True
    DECRYPT = False


    def __init__(self, key):
        if len(key) != 8:
            raise ValueError("The key should be 8 bytes")
        self.K = [[0] * 48 ] * 16
        self.final = []
        self.__key = key
        self.__createSubKeys()


    def __permutate(self, table, block):
        return list(map(lambda x: block[x], table))


    def __str2BitList(self, data):
        resultLen = len(data) * 8
        result = [0] * resultLen
        pos = 0
        for ch in data:
            i = 7
            while i >= 0:
                if ch & (1 << i) != 0:
                    result[pos] = 1
                else:
                    result[pos] = 0
                pos += 1
                i -= 1

        return result


    def __bitList2Str(self, data):
        result = []
        pos = 0
        c = 0
        while pos < len(data):
            c += data[pos] << (7 - (pos % 8))
            if (pos % 8) == 7:
                result.append(c)
                c = 0
            pos += 1

        return bytes(result)


    def __createSubKeys(self):
        try:
            self.__key = self.__key.encode()
        except UnicodeEncodeError:
            raise ValueError("Encode error")
        key = self.__permutate(Des.__PC1, self.__str2BitList(self.__key))
        left = key[:28]
        right = key[28:]
        i = 0
        while i < 16:
            j = 0
            while j < Des.__leftRotation[i]:
                left = left[1:] + [left[0]]
                right = right[1:] + [right[0]]
                j += 1
            self.K[i] = self.__permutate(Des.__PC2, left + right)
            i += 1
            
            
    def __padData(self, data):
        padLen = 8 - (len(data) % 8)
        data += bytes([padLen] * padLen)
        return data
        
    def __unpadData(self, data):
        padLen = data[-1]
        data = data[:-padLen]
        return data
        
    def crypt(self, data, cryptType):
        result = []
        
        block = self.__str2BitList(data[:])
        block = self.__permutate(Des.__IP, block)
        
        left = block[:32]
        right = block[32:]
        
        if cryptType == Des.ENCRYPT:
            start = 0
            add = 1
        else:
            start = 15
            add = -1
        
        j = 0
        while j < 16:
            tempRight = right[:]
            right = self.__permutate(Des.__EExpansion, right)
            
            right = list(map(lambda x, y: x ^ y, right, self.K[start]))
            B = [right[6 * i:6 * (i + 1)] for i in range(8)]
            
            k = 0
            Bn = [0] * 32
            pos = 0
            while k < 8:
                m = (B[k][0] << 1) + B[k][5]
                n = (B[k][1] << 3) + (B[k][2] << 2) + (B[k][3] << 1) + B[k][4]
                v = Des.__sBoxes[k][m][n]
                
                Bn[pos] = (v & 8) >> 3
                Bn[pos + 1] = (v & 4) >> 2
                Bn[pos + 2] = (v & 2) >> 1
                Bn[pos + 3] = v & 1
                
                pos += 4
                k += 1
                
            right = self.__permutate(Des.__PSubstitute, Bn)
            right = list(map(lambda x, y: x ^ y, left, right))
            left = tempRight
            
            j += 1
            start += add
            
        block = self.__permutate(Des.__inverseIP, right + left)
        result.append(self.__bitList2Str(block))
            
        return bytes.fromhex('').join(result)
        

    def encrypt(self, data):
        try:
            data = data.encode()
        except UnicodeEncodeError:
            raise ValueError("Encode error")
        result = b''
        j = 0
        for i in range(len(data) // 8):
            result += self.crypt(data[8 * i: 8 * (i + 1)], Des.ENCRYPT)
            j = i
        result += self.crypt(self.__padData(data[8 * (j + 1):]), Des.ENCRYPT)
        return result


    def decrypt(self, data):
        result = ""
        for i in range(len(data) // 8 - 1):
            result += self.crypt(data[8 * i: 8 * (i + 1)], Des.DECRYPT).decode()
        result += self.__unpadData(self.crypt(data[-8:], Des.DECRYPT)).decode()
        return result