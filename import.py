import random
from guess import tbkangka

jawaban = random.randint(1,10)
tebakan = int(input("tebak angka  : "))

if tbkangka(tebakan , jawaban):
	print("jawaban kamu benar")
else:
	print("jawaban kamu salah")