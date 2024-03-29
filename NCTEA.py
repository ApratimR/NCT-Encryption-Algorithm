#@name : NECTA (No Cipher Text Encryption Algorithm)

import numpy as np
from FNNH import FNNH
import base64

def NECTA(data="",key="",mode=1,stress=1):
	"""
	data = (str) the main data which you want to encrypt or decrypt

	key = (str) the main key

	mode = (int) determines the mode of operation(1 = encrypt, 2 = decrypt)
	Default mode is set to 1(encryption mode)

	stress = (int) the amount of Instruction cycles required to do the
	whole operation(Default = 1)
	"""

	encryption_array=np.array([
		[34, 60, 38, 1, 55, 63, 33, 40, 46, 42, 52, 18, 39, 10, 30, 47, 6, 50, 25, 3, 14, 26, 2, 13, 53, 54, 58, 35, 17, 61, 27, 15, 23, 44, 21, 59, 37, 36, 45, 41, 62, 16, 5, 9, 4, 29, 12, 51, 48, 8, 32, 57, 7, 49, 11, 22, 43, 0, 28, 19, 31, 20, 56, 24],
		[43, 59, 29, 36, 41, 17, 19, 53, 57, 32, 8, 42, 26, 60, 30, 55, 23, 58, 39, 1, 12, 31, 52, 3, 62, 16, 5, 49, 47, 33, 51, 22, 6, 13, 38, 11, 50, 37, 20, 4, 2, 40, 48, 34, 25, 45, 15, 0, 54, 14, 56, 44, 7, 21, 9, 10, 24, 46, 18, 63, 27, 35, 28, 61],
		[10, 8, 0, 39, 41, 53, 45, 17, 56, 37, 4, 25, 35, 20, 47, 58, 30, 12, 1, 19, 51, 32, 63, 13, 57, 29, 50, 11, 61, 31, 3, 24, 55, 6, 22, 46, 2, 36, 44, 15, 27, 9, 21, 40, 18, 62, 5, 49, 52, 34, 28, 7, 60, 33, 48, 16, 42, 14, 23, 38, 54, 26, 59, 43],
		[31, 9, 30, 54, 33, 23, 47, 7, 59, 49, 15, 3, 11, 34, 10, 21, 44, 32, 37, 62, 4, 39, 63, 14, 43, 17, 35, 20, 42, 24, 27, 38, 1, 61, 19, 29, 36, 26, 57, 55, 8, 41, 0, 40, 51, 6, 13, 53, 12, 46, 52, 48, 2, 16, 25, 22, 18, 50, 60, 58, 5, 56, 45, 28],
		[41, 63, 23, 18, 44, 30, 10, 5, 0, 19, 40, 11, 28, 45, 34, 13, 20, 9, 51, 37, 38, 33, 47, 56, 31, 1, 58, 53, 60, 29, 26, 59, 15, 4, 36, 21, 49, 14, 35, 17, 61, 6, 7, 8, 2, 3, 54, 52, 46, 16, 39, 57, 25, 24, 62, 55, 42, 12, 22, 32, 43, 48, 27, 50],
		[37, 33, 53, 60, 54, 18, 50, 55, 34, 4, 19, 63, 6, 7, 30, 26, 51, 48, 17, 45, 5, 23, 25, 57, 47, 28, 62, 41, 58, 21, 43, 49, 3, 0, 40, 9, 1, 42, 24, 29, 14, 10, 20, 35, 56, 52, 32, 13, 59, 8, 15, 61, 27, 39, 12, 38, 31, 11, 46, 2, 22, 44, 36, 16],
		[40, 44, 21, 53, 8, 60, 50, 49, 33, 51, 28, 9, 58, 11, 1, 18, 55, 2, 4, 46, 3, 38, 14, 42, 37, 34, 12, 47, 41, 57, 13, 22, 26, 19, 45, 48, 36, 43, 0, 29, 15, 16, 30, 7, 24, 6, 10, 31, 59, 62, 61, 20, 39, 27, 56, 52, 17, 23, 5, 35, 54, 25, 63, 32],
		[31, 24, 49, 23, 16, 63, 20, 47, 59, 12, 55, 2, 57, 54, 28, 35, 27, 19, 39, 50, 11, 4, 33, 52, 37, 38, 17, 43, 36, 53, 46, 10, 34, 3, 30, 14, 7, 22, 42, 8, 1, 61, 26, 9, 62, 45, 15, 51, 48, 40, 18, 25, 21, 29, 0, 5, 41, 32, 58, 6, 44, 56, 13, 60],
		[37, 52, 27, 2, 51, 61, 49, 17, 58, 20, 16, 54, 60, 45, 0, 29, 43, 55, 62, 21, 30, 6, 53, 18, 28, 46, 12, 32, 25, 36, 40, 8, 23, 57, 35, 42, 63, 38, 13, 14, 15, 9, 10, 26, 22, 50, 4, 24, 11, 1, 56, 44, 19, 33, 39, 59, 31, 47, 5, 41, 3, 34, 48, 7],
		[51, 33, 19, 25, 43, 37, 7, 29, 54, 57, 24, 16, 30, 45, 49, 18, 53, 1, 63, 26, 56, 0, 20, 38, 59, 58, 17, 34, 32, 47, 14, 12, 40, 3, 61, 60, 41, 23, 42, 5, 39, 6, 13, 28, 9, 11, 21, 31, 55, 62, 27, 4, 44, 22, 52, 15, 8, 36, 48, 2, 50, 46, 35, 10],
		[62, 43, 30, 49, 24, 60, 5, 9, 18, 51, 16, 13, 20, 17, 25, 54, 12, 35, 15, 59, 14, 21, 19, 38, 32, 55, 44, 28, 45, 27, 34, 1, 53, 56, 31, 8, 3, 50, 23, 33, 63, 46, 39, 0, 29, 42, 40, 47, 36, 6, 37, 10, 26, 58, 2, 52, 61, 48, 41, 11, 22, 57, 7, 4],
		[24, 45, 41, 57, 26, 13, 40, 20, 21, 32, 53, 33, 7, 59, 49, 9, 51, 38, 56, 52, 1, 25, 12, 30, 42, 35, 0, 37, 48, 3, 11, 4, 29, 10, 16, 17, 62, 18, 19, 34, 63, 6, 47, 50, 58, 43, 54, 8, 36, 2, 15, 22, 14, 39, 28, 27, 46, 23, 55, 31, 61, 44, 60, 5],
		[52, 46, 1, 26, 62, 8, 34, 22, 58, 12, 5, 54, 28, 57, 21, 61, 20, 55, 10, 15, 31, 19, 56, 24, 35, 48, 30, 27, 13, 59, 43, 38, 0, 44, 50, 17, 11, 37, 45, 3, 33, 14, 7, 49, 18, 4, 39, 41, 63, 23, 36, 6, 25, 9, 42, 40, 32, 51, 29, 47, 53, 2, 60, 16],
		[13, 14, 56, 25, 19, 57, 34, 48, 5, 43, 31, 28, 60, 6, 1, 59, 63, 7, 47, 9, 22, 21, 54, 40, 32, 8, 3, 58, 0, 45, 17, 2, 24, 44, 26, 37, 29, 12, 42, 41, 16, 46, 18, 15, 36, 50, 4, 55, 62, 23, 53, 51, 10, 39, 27, 49, 11, 35, 33, 20, 38, 30, 61, 52],
		[48, 34, 55, 22, 27, 23, 26, 42, 4, 39, 57, 37, 59, 8, 18, 21, 35, 29, 9, 63, 62, 13, 31, 20, 44, 16, 19, 6, 24, 41, 25, 61, 38, 10, 33, 28, 45, 51, 3, 2, 1, 12, 50, 43, 60, 47, 30, 7, 15, 52, 40, 49, 53, 56, 46, 17, 11, 5, 0, 54, 58, 32, 36, 14],
		[54, 21, 56, 36, 32, 6, 49, 14, 24, 34, 31, 27, 60, 8, 17, 7, 45, 12, 39, 44, 29, 47, 43, 16, 19, 50, 53, 0, 1, 52, 37, 26, 18, 5, 4, 35, 48, 55, 25, 41, 40, 30, 3, 59, 15, 28, 42, 20, 33, 2, 11, 38, 51, 61, 10, 23, 13, 58, 63, 46, 22, 62, 57, 9],
		[2, 13, 36, 54, 53, 58, 63, 61, 40, 45, 47, 8, 41, 34, 30, 57, 20, 21, 10, 55, 49, 38, 16, 48, 12, 27, 23, 1, 7, 26, 60, 33, 46, 39, 22, 56, 4, 24, 35, 14, 28, 3, 18, 43, 0, 6, 51, 17, 50, 25, 44, 37, 32, 9, 31, 11, 19, 5, 59, 15, 52, 62, 42, 29],
		[37, 27, 6, 48, 39, 19, 43, 59, 62, 13, 22, 42, 7, 30, 32, 49, 54, 53, 57, 61, 5, 60, 3, 14, 12, 2, 17, 63, 56, 11, 31, 50, 28, 35, 46, 44, 26, 58, 29, 51, 40, 33, 4, 10, 36, 47, 21, 15, 18, 16, 0, 52, 45, 41, 1, 23, 25, 20, 38, 55, 8, 24, 34, 9],
		[27, 4, 17, 41, 14, 13, 47, 59, 7, 18, 62, 1, 34, 16, 57, 21, 22, 48, 32, 11, 60, 9, 52, 49, 43, 0, 31, 37, 44, 45, 55, 51, 20, 8, 15, 29, 33, 39, 25, 3, 28, 40, 5, 38, 58, 30, 54, 10, 63, 12, 2, 6, 26, 61, 24, 23, 50, 36, 35, 53, 19, 46, 42, 56],
		[38, 61, 39, 11, 40, 5, 26, 60, 50, 54, 27, 14, 59, 33, 48, 44, 17, 35, 7, 43, 34, 62, 18, 51, 20, 30, 46, 8, 24, 47, 41, 21, 53, 16, 22, 12, 31, 63, 3, 25, 52, 1, 58, 13, 36, 9, 49, 56, 2, 23, 6, 0, 10, 45, 55, 4, 29, 19, 28, 42, 57, 15, 37, 32],
		[37, 54, 27, 18, 30, 25, 23, 10, 12, 61, 20, 7, 55, 34, 49, 40, 33, 42, 46, 48, 19, 24, 26, 63, 5, 47, 53, 58, 0, 28, 17, 31, 62, 9, 2, 56, 36, 11, 51, 44, 3, 60, 21, 16, 4, 57, 29, 39, 32, 15, 50, 1, 6, 52, 45, 41, 22, 43, 38, 59, 35, 13, 8, 14],
		[61, 31, 60, 8, 19, 50, 51, 6, 55, 26, 18, 4, 22, 11, 53, 59, 20, 34, 43, 5, 48, 2, 47, 37, 12, 40, 21, 15, 44, 1, 29, 42, 28, 25, 63, 24, 52, 9, 54, 62, 7, 0, 39, 17, 57, 3, 16, 49, 14, 46, 41, 56, 33, 58, 27, 23, 30, 32, 35, 36, 13, 10, 38, 45],
		[59, 35, 32, 21, 12, 27, 29, 37, 17, 28, 38, 56, 63, 44, 61, 9, 25, 36, 40, 4, 5, 45, 51, 8, 39, 16, 30, 42, 55, 48, 33, 62, 26, 60, 43, 23, 0, 41, 52, 20, 57, 49, 34, 10, 18, 1, 47, 6, 11, 14, 31, 54, 22, 50, 2, 53, 46, 13, 15, 19, 7, 58, 24, 3],
		[15, 12, 4, 0, 30, 56, 10, 27, 46, 24, 62, 2, 9, 37, 28, 51, 26, 16, 25, 6, 11, 32, 49, 17, 45, 42, 22, 44, 31, 8, 41, 38, 14, 33, 1, 55, 13, 35, 20, 63, 52, 43, 60, 21, 57, 61, 7, 18, 39, 58, 29, 48, 19, 36, 54, 5, 34, 47, 53, 23, 40, 59, 3, 50],
		[23, 17, 41, 42, 12, 47, 24, 52, 15, 51, 14, 36, 61, 58, 50, 45, 55, 7, 37, 9, 34, 57, 43, 3, 31, 32, 16, 53, 28, 59, 0, 54, 1, 22, 11, 44, 40, 49, 13, 25, 8, 35, 63, 19, 20, 6, 2, 48, 33, 5, 29, 60, 38, 27, 26, 18, 30, 4, 21, 46, 39, 10, 62, 56],
		[53, 36, 32, 48, 19, 58, 8, 28, 25, 56, 27, 42, 40, 51, 54, 41, 49, 16, 50, 21, 7, 1, 18, 30, 62, 17, 4, 55, 24, 20, 34, 2, 13, 38, 43, 63, 46, 29, 52, 31, 47, 22, 33, 0, 10, 6, 45, 59, 35, 60, 3, 39, 26, 5, 61, 37, 15, 11, 44, 23, 14, 9, 12, 57],
		[34, 41, 6, 31, 40, 16, 18, 47, 15, 27, 13, 49, 59, 51, 3, 58, 53, 2, 48, 54, 1, 9, 26, 32, 55, 33, 7, 56, 62, 22, 60, 11, 0, 30, 45, 24, 52, 19, 23, 37, 46, 17, 35, 42, 28, 21, 57, 38, 10, 20, 25, 4, 43, 29, 50, 8, 61, 39, 5, 12, 63, 36, 44, 14],
		[58, 48, 2, 23, 9, 59, 45, 44, 10, 55, 47, 37, 12, 30, 29, 54, 61, 35, 8, 31, 32, 4, 63, 5, 6, 15, 18, 1, 14, 25, 41, 3, 57, 51, 50, 11, 56, 43, 49, 28, 19, 52, 16, 46, 27, 24, 60, 39, 22, 26, 36, 40, 53, 42, 33, 38, 7, 17, 13, 21, 34, 20, 0, 62],
		[5, 13, 35, 36, 22, 56, 29, 16, 2, 27, 59, 31, 57, 33, 53, 18, 52, 46, 40, 14, 23, 7, 55, 24, 32, 42, 30, 38, 25, 54, 58, 47, 10, 45, 60, 3, 17, 12, 44, 37, 28, 51, 26, 48, 49, 8, 41, 19, 50, 9, 1, 63, 6, 34, 4, 11, 20, 39, 0, 43, 21, 15, 62, 61],
		[21, 39, 5, 43, 45, 34, 61, 4, 13, 52, 59, 33, 24, 16, 26, 56, 3, 35, 58, 23, 57, 40, 11, 36, 51, 62, 31, 63, 14, 44, 49, 10, 18, 12, 42, 20, 27, 54, 7, 47, 50, 29, 6, 17, 32, 1, 38, 8, 0, 19, 30, 2, 37, 48, 46, 41, 55, 25, 15, 53, 9, 22, 28, 60],
		[12, 2, 21, 3, 46, 61, 20, 15, 0, 32, 13, 56, 43, 41, 1, 28, 38, 26, 53, 8, 10, 52, 42, 19, 18, 30, 58, 35, 50, 49, 25, 11, 57, 34, 47, 29, 59, 62, 44, 17, 16, 60, 36, 51, 23, 14, 31, 24, 54, 55, 45, 5, 63, 7, 22, 6, 39, 27, 9, 40, 4, 48, 33, 37],
		[3, 55, 63, 54, 35, 6, 31, 11, 57, 41, 9, 1, 51, 36, 49, 24, 17, 25, 0, 53, 45, 21, 16, 10, 15, 20, 19, 23, 7, 47, 43, 32, 34, 29, 26, 48, 40, 37, 14, 50, 13, 56, 28, 4, 58, 27, 12, 60, 52, 2, 8, 61, 62, 59, 22, 33, 30, 18, 38, 44, 39, 5, 42, 46],
		[26, 4, 28, 9, 63, 6, 39, 43, 47, 60, 52, 34, 31, 2, 13, 30, 40, 17, 10, 37, 18, 32, 1, 36, 20, 12, 0, 54, 62, 29, 11, 56, 51, 53, 16, 55, 19, 21, 7, 61, 27, 38, 3, 24, 35, 15, 44, 45, 49, 48, 33, 58, 25, 22, 5, 8, 41, 57, 42, 46, 50, 23, 59, 14],
		[14, 52, 49, 61, 63, 8, 46, 28, 20, 27, 10, 23, 37, 62, 12, 59, 43, 30, 41, 60, 39, 7, 34, 56, 26, 13, 22, 2, 50, 53, 35, 29, 51, 47, 54, 44, 57, 25, 45, 55, 16, 11, 19, 42, 17, 36, 18, 6, 1, 0, 3, 32, 48, 58, 15, 24, 21, 5, 38, 31, 40, 4, 9, 33],
		[41, 42, 40, 48, 7, 13, 25, 34, 18, 28, 8, 14, 33, 61, 19, 21, 11, 43, 32, 49, 46, 52, 62, 59, 16, 31, 23, 47, 22, 44, 29, 51, 9, 56, 55, 60, 20, 50, 37, 36, 4, 35, 17, 12, 5, 38, 30, 6, 24, 26, 45, 58, 0, 15, 63, 53, 54, 39, 2, 1, 10, 27, 57, 3],
		[25, 61, 21, 56, 24, 14, 44, 10, 22, 30, 1, 18, 15, 4, 63, 27, 35, 42, 48, 43, 9, 7, 26, 12, 34, 41, 54, 40, 39, 2, 62, 53, 13, 5, 46, 28, 38, 19, 55, 50, 49, 47, 37, 57, 3, 29, 36, 16, 60, 23, 20, 51, 58, 32, 0, 8, 6, 59, 52, 11, 31, 17, 33, 45],
		[29, 17, 27, 15, 40, 6, 1, 46, 31, 61, 5, 8, 48, 62, 28, 60, 3, 52, 43, 26, 32, 4, 23, 44, 25, 53, 54, 56, 51, 41, 11, 19, 30, 16, 9, 13, 57, 0, 34, 18, 49, 58, 63, 20, 45, 38, 24, 2, 42, 47, 33, 14, 7, 22, 37, 36, 50, 21, 55, 59, 39, 12, 10, 35],
		[21, 11, 58, 16, 9, 28, 47, 3, 44, 1, 20, 29, 18, 6, 50, 55, 19, 33, 52, 57, 15, 32, 41, 5, 38, 22, 63, 53, 0, 7, 59, 49, 48, 24, 43, 61, 23, 2, 42, 14, 10, 27, 30, 62, 25, 39, 54, 31, 40, 26, 45, 12, 60, 8, 51, 56, 36, 34, 13, 35, 17, 46, 37, 4],
		[43, 59, 14, 39, 56, 16, 11, 12, 47, 26, 36, 4, 51, 35, 2, 8, 57, 61, 3, 6, 19, 40, 44, 7, 37, 54, 29, 48, 0, 30, 1, 32, 33, 50, 52, 24, 46, 13, 15, 31, 10, 20, 55, 21, 28, 23, 17, 60, 63, 5, 18, 38, 45, 22, 9, 62, 25, 58, 34, 42, 27, 49, 53, 41],
		[31, 0, 18, 38, 47, 29, 50, 32, 3, 59, 14, 27, 7, 28, 63, 9, 39, 56, 44, 52, 43, 4, 42, 37, 48, 19, 10, 24, 8, 53, 40, 54, 11, 12, 57, 45, 62, 46, 6, 20, 25, 16, 61, 35, 49, 17, 41, 30, 21, 33, 60, 51, 36, 5, 26, 22, 34, 55, 2, 13, 15, 58, 1, 23],
		[36, 33, 16, 13, 18, 46, 15, 40, 61, 4, 34, 23, 51, 27, 12, 37, 50, 56, 19, 47, 38, 49, 55, 2, 35, 45, 29, 8, 25, 54, 21, 17, 63, 24, 0, 7, 20, 52, 62, 42, 60, 30, 22, 10, 6, 39, 53, 32, 41, 57, 5, 44, 26, 48, 1, 14, 58, 3, 11, 43, 59, 31, 28, 9],
		[12, 14, 32, 9, 52, 5, 25, 27, 49, 45, 13, 0, 57, 28, 26, 42, 55, 23, 38, 34, 24, 51, 39, 19, 31, 63, 17, 50, 53, 59, 41, 48, 7, 37, 2, 10, 46, 54, 43, 47, 22, 16, 1, 61, 21, 33, 29, 30, 11, 36, 58, 15, 56, 44, 62, 60, 8, 4, 35, 3, 20, 6, 18, 40],
		[49, 0, 8, 29, 47, 11, 7, 9, 18, 34, 44, 33, 16, 2, 12, 27, 10, 30, 25, 36, 50, 42, 59, 28, 40, 22, 38, 58, 62, 20, 14, 55, 39, 35, 1, 13, 45, 4, 21, 17, 23, 6, 26, 31, 43, 5, 3, 41, 53, 54, 48, 37, 51, 19, 56, 63, 52, 61, 32, 57, 60, 24, 15, 46],
		[25, 20, 52, 63, 1, 43, 9, 5, 35, 11, 6, 45, 3, 62, 51, 31, 21, 37, 56, 7, 17, 54, 22, 32, 58, 2, 60, 53, 40, 47, 39, 57, 27, 36, 44, 0, 38, 34, 10, 13, 42, 15, 8, 18, 26, 50, 48, 59, 12, 24, 55, 28, 23, 61, 46, 41, 33, 19, 49, 14, 29, 16, 30, 4],
		[10, 8, 43, 44, 18, 42, 26, 60, 16, 5, 58, 39, 57, 4, 23, 61, 37, 27, 36, 24, 3, 34, 7, 55, 14, 19, 35, 29, 53, 13, 0, 33, 32, 9, 25, 54, 30, 47, 49, 52, 50, 62, 46, 2, 51, 21, 48, 1, 38, 40, 31, 20, 15, 41, 12, 11, 6, 28, 45, 59, 22, 17, 63, 56],
		[36, 1, 32, 37, 43, 44, 25, 61, 27, 50, 39, 11, 52, 55, 21, 41, 31, 13, 59, 28, 4, 46, 10, 34, 22, 48, 20, 5, 42, 7, 47, 0, 51, 38, 53, 63, 35, 57, 8, 16, 19, 62, 49, 15, 14, 29, 2, 30, 18, 54, 23, 33, 17, 40, 9, 24, 45, 6, 26, 12, 3, 60, 58, 56],
		[26, 32, 52, 43, 61, 53, 58, 51, 45, 6, 3, 18, 19, 56, 37, 41, 42, 10, 44, 12, 31, 35, 23, 8, 27, 17, 16, 39, 49, 34, 38, 57, 59, 24, 5, 54, 15, 55, 47, 60, 11, 46, 1, 33, 48, 13, 0, 63, 28, 36, 20, 4, 21, 7, 14, 29, 25, 40, 30, 2, 22, 9, 50, 62],
		[57, 31, 41, 60, 15, 33, 10, 25, 2, 28, 51, 14, 17, 44, 56, 8, 53, 5, 24, 18, 12, 32, 27, 39, 45, 40, 19, 42, 62, 1, 58, 38, 13, 37, 52, 49, 26, 22, 63, 43, 3, 0, 47, 36, 61, 9, 46, 30, 34, 6, 21, 11, 59, 35, 16, 7, 20, 54, 55, 29, 50, 23, 48, 4],
		[46, 59, 37, 28, 52, 12, 4, 8, 50, 34, 30, 27, 47, 13, 41, 45, 25, 62, 32, 43, 44, 48, 42, 18, 9, 24, 6, 7, 29, 1, 15, 36, 21, 38, 53, 16, 5, 3, 26, 63, 58, 11, 14, 56, 51, 61, 35, 20, 10, 0, 39, 33, 40, 55, 60, 19, 31, 17, 57, 22, 49, 2, 23, 54],
		[61, 41, 59, 12, 48, 31, 18, 37, 8, 45, 58, 28, 7, 20, 50, 33, 57, 26, 40, 53, 39, 54, 22, 51, 60, 9, 24, 16, 23, 36, 44, 63, 27, 52, 2, 3, 30, 19, 21, 11, 6, 49, 55, 38, 10, 32, 4, 35, 15, 5, 47, 56, 29, 62, 0, 43, 14, 46, 34, 1, 42, 13, 17, 25],
		[28, 10, 33, 58, 15, 30, 27, 40, 45, 49, 51, 11, 24, 25, 55, 31, 61, 60, 38, 23, 7, 22, 18, 56, 17, 36, 50, 62, 9, 34, 37, 20, 2, 42, 41, 43, 0, 8, 54, 57, 16, 1, 4, 59, 48, 47, 19, 63, 14, 35, 32, 3, 21, 26, 53, 46, 29, 5, 39, 6, 52, 13, 44, 12],
		[42, 0, 38, 25, 35, 20, 46, 16, 24, 2, 40, 21, 30, 27, 6, 56, 9, 28, 48, 54, 53, 18, 13, 15, 1, 11, 61, 19, 51, 50, 55, 62, 5, 10, 45, 41, 23, 14, 36, 22, 34, 49, 59, 4, 52, 8, 17, 60, 26, 12, 29, 31, 47, 43, 63, 37, 32, 7, 57, 44, 33, 58, 39, 3],
		[9, 25, 52, 17, 6, 54, 58, 21, 3, 53, 47, 13, 44, 36, 59, 35, 56, 51, 37, 30, 38, 63, 39, 12, 1, 19, 26, 55, 33, 41, 29, 0, 27, 49, 42, 46, 20, 23, 10, 14, 16, 8, 15, 50, 32, 11, 40, 43, 45, 62, 4, 34, 18, 28, 22, 5, 61, 2, 57, 60, 24, 7, 48, 31],
		[39, 15, 17, 56, 45, 47, 25, 37, 40, 36, 29, 53, 6, 14, 34, 58, 1, 57, 49, 26, 9, 52, 59, 13, 2, 62, 51, 4, 5, 18, 19, 50, 31, 12, 0, 48, 8, 43, 41, 27, 11, 63, 55, 10, 16, 24, 35, 32, 60, 22, 20, 28, 46, 44, 33, 61, 38, 42, 3, 21, 54, 30, 23, 7],
		[33, 59, 39, 5, 50, 45, 57, 61, 9, 6, 22, 23, 20, 10, 63, 54, 35, 2, 14, 53, 60, 55, 13, 43, 32, 37, 42, 36, 26, 7, 52, 48, 38, 46, 51, 56, 40, 24, 47, 11, 3, 1, 0, 49, 19, 31, 12, 28, 58, 8, 41, 4, 15, 25, 34, 16, 44, 21, 29, 27, 30, 18, 17, 62],
		[56, 7, 23, 46, 59, 50, 16, 43, 18, 51, 58, 22, 19, 35, 49, 27, 57, 61, 17, 11, 47, 15, 13, 55, 6, 42, 24, 45, 44, 33, 8, 2, 54, 48, 60, 31, 52, 53, 26, 14, 9, 0, 62, 40, 5, 30, 41, 34, 3, 28, 1, 63, 25, 38, 32, 20, 21, 12, 39, 29, 36, 37, 4, 10],
		[6, 5, 36, 17, 26, 4, 35, 18, 14, 27, 2, 33, 21, 25, 28, 0, 16, 46, 63, 56, 20, 32, 30, 60, 7, 11, 54, 15, 50, 34, 24, 31, 55, 10, 13, 48, 41, 43, 22, 12, 8, 37, 51, 40, 38, 19, 49, 53, 9, 62, 44, 59, 29, 58, 47, 42, 61, 3, 23, 39, 52, 1, 57, 45],
		[54, 32, 52, 31, 23, 29, 47, 8, 44, 51, 39, 22, 33, 40, 62, 49, 21, 1, 63, 18, 9, 56, 42, 35, 16, 11, 36, 38, 57, 15, 24, 60, 58, 46, 27, 61, 13, 17, 30, 4, 43, 12, 25, 7, 41, 37, 20, 48, 26, 50, 55, 6, 2, 34, 45, 14, 10, 19, 5, 59, 53, 28, 3, 0],
		[21, 11, 28, 52, 16, 26, 40, 14, 55, 30, 23, 7, 10, 5, 31, 25, 46, 19, 42, 57, 2, 38, 41, 37, 43, 4, 18, 17, 35, 13, 15, 51, 59, 33, 0, 6, 58, 60, 48, 45, 29, 22, 50, 62, 12, 3, 36, 47, 8, 61, 20, 56, 39, 54, 32, 34, 27, 53, 24, 63, 1, 9, 49, 44],
		[58, 47, 40, 2, 46, 29, 17, 60, 39, 54, 0, 19, 6, 56, 18, 43, 10, 7, 12, 1, 53, 51, 35, 49, 21, 33, 30, 55, 20, 28, 24, 25, 59, 41, 50, 22, 14, 63, 3, 57, 38, 37, 23, 27, 16, 34, 42, 44, 5, 26, 8, 13, 11, 45, 52, 4, 62, 32, 15, 9, 36, 31, 48, 61],
		[34, 57, 20, 5, 40, 52, 26, 24, 22, 61, 33, 2, 10, 32, 19, 6, 55, 4, 11, 23, 9, 46, 42, 59, 14, 13, 50, 29, 30, 1, 3, 16, 53, 51, 21, 56, 38, 39, 8, 0, 41, 27, 35, 7, 48, 17, 28, 54, 25, 12, 37, 18, 60, 36, 15, 45, 47, 49, 58, 44, 63, 43, 31, 62],
		[17, 60, 41, 21, 50, 6, 18, 55, 14, 29, 43, 53, 61, 62, 36, 32, 37, 25, 12, 23, 26, 5, 48, 33, 7, 59, 56, 27, 19, 30, 45, 0, 22, 52, 3, 44, 35, 31, 9, 20, 54, 58, 51, 38, 2, 28, 10, 16, 8, 13, 42, 46, 24, 34, 47, 1, 11, 49, 4, 39, 40, 15, 57, 63],
		[52, 20, 4, 28, 55, 37, 49, 63, 41, 14, 12, 51, 60, 61, 57, 47, 59, 23, 6, 53, 11, 24, 46, 16, 50, 34, 31, 13, 32, 8, 38, 39, 18, 54, 9, 0, 21, 29, 44, 43, 26, 15, 5, 40, 7, 42, 3, 17, 30, 22, 19, 35, 58, 45, 2, 36, 48, 33, 56, 1, 27, 10, 62, 25],
		[37, 63, 43, 49, 20, 11, 27, 58, 46, 62, 1, 31, 42, 9, 51, 15, 35, 56, 39, 14, 3, 7, 8, 24, 40, 0, 44, 33, 48, 13, 32, 41, 36, 4, 38, 60, 2, 29, 17, 47, 53, 55, 10, 45, 6, 5, 50, 34, 18, 52, 19, 30, 59, 26, 22, 16, 61, 57, 23, 21, 28, 12, 54, 25],
		],dtype=np.uint8)

	refstr=list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_")

	def encodedata(data):
		data = str(data)
		data = data.encode(encoding="UTF-8")
		data = base64.urlsafe_b64encode(data)
		data = data.decode(encoding="UTF-8")

		if "=" in data:
			pos = data.index("=")

			data = data[:pos]
		return data


	def decodedata(data):
		data = str(data)
		paddingLenght = 4-(len(data) % 4)
		padding = "="*paddingLenght
		data += padding
		data = data.encode(encoding="UTF-8")
		data = base64.urlsafe_b64decode(data)
		data = data.decode(encoding="UTF-8")
		return data


	def str_to_int(data):
		emplist = list()
		for temp1 in data:
			emplist.append(refstr.index(temp1))
		return emplist


	def int_to_str(data):
		emplist = str()
		for temp1 in data:
			emplist+=refstr[temp1]
		return emplist


	def main_array_messup(key,thearray):
		"""
		key = 1D list of int with each element under 64

		thearray = 2D array of size 64*64
		"""
		for temp in range(64):
			thearray[temp]=np.roll(thearray[temp],key[temp])
		return thearray

	if isinstance(stress,int)==True:
		if stress<=0 :
			raise Exception("enter a valid stress amount")
	else:
		raise Exception("enter a valid stress data type")


	hashed_key = FNNH(data=key,hash_size=128,rounds=16*stress)
	hashed_key = str_to_int(hashed_key)

	if mode == 1:
		#encrypt
		data = str_to_int(encodedata(data))
		round_encryption_array = main_array_messup(key=hashed_key[0:64],thearray=encryption_array)
		counter=0
		data = np.roll(data,hashed_key[hashed_key[127]+64])

		for temp in range(len(data)):
			data[temp] = round_encryption_array[counter].tolist().index(data[temp])
			counter+=1
			if counter == 64:
				hashed_key=FNNH(data=key,hash_size=128,rounds=4*stress)
				hashed_key = str_to_int(hashed_key)
				round_encryption_array = main_array_messup(key=hashed_key[0:64],thearray=round_encryption_array)
				counter=0

		data = int_to_str(data)
		return data



	if mode == 2:
		data = str_to_int(data)
		round_encryption_array = main_array_messup(key=hashed_key[0:64],thearray=encryption_array)
		tempkeyroll = hashed_key[hashed_key[127]+64]
		counter=0

		for temp in range(len(data)):


			data[temp] = round_encryption_array[counter][data[temp]]

			counter+=1
			if counter == 64:
				hashed_key=FNNH(data=key,hash_size=128,rounds=4*stress)
				hashed_key = str_to_int(hashed_key)
				round_encryption_array = main_array_messup(key=hashed_key[0:64],thearray=round_encryption_array)
				counter=0
		#TODO this needs to be tested
		data = np.reshape(data,len(data))
		data = np.roll(data,-tempkeyroll)
		data = int_to_str(data)
		return decodedata(data)

	else:
		raise Exception("invalid option entered")
