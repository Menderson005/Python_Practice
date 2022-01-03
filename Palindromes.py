#N is number of letters 
#K is length of word 
#ab c ba
#ab ba
#python 3.8.6   Last Update:2022/01/02
import random 

def solution(N,K):
	Letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	P = K/2
	Even = K%2
	Word_Letters = list(random.sample(Letters,N))
	Front_Word = list(random.choices(Word_Letters,k=K))
	Part_One = ''.join(Front_Word)
	def flip(x):
		return x[::-1]
	Part_Two = flip(Part_One)
	Part_Three = Part_Two[1::]
	if Even == 0:
		Pal = Part_One + Part_Two
	else:
		Pal = Part_One + Part_Three
	print(Pal)
