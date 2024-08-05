import random
import sys
import game_data
from art import logo, vs

# Kodlari optimize et 
# Ingilizce fonksiyon ve var isimleri kullanilmali
# Fonksiyonlarin islevini baslarina yazilmali
# sys nedir ona bakilabilir

score = 0


############
#random bi sayiyla A yi buluyor
#randomla B yi buluyoruz
#+

#secim yap
#input
#kiyas fonk ile like kiyasla
#+

#sonuc!=input ise yanlis
#secim yanlissa oyun bitiyor
#dogruysa puani arttir
#+
#A yi Bye esitliyor
#random B bul
#fonksiyonlar : game, compare_num, rand_find
#A=randNum.get("follower_count")
#B=game_data.data[random.randint(0, 49)].get("follower_count")

 
#harf=""
#print("Randmum:",randKey)


#value = data.values()[index]



def randomer(harf):
	"""Merabaaa"""
	randKey=game_data.data[random.randint(0, 49)]


	followers=randKey.get("follower_count")#A
	get_name=randKey.get("name")
	get_descr=randKey.get("description")
	get_country=randKey.get("country")

	print(f"Compare {harf}:",get_name,":",get_descr,"from",get_country)
	# print("Randkey in randomer:",randKey)
	return randKey
	
  

def compare_num(guess):
	# returns the A one
	# A ve B yi kiyasliyor 
	# A ve B yi kaydetme
	# Kazanani belirleme
	# Puanlari kaydetme
	# Puan artirma
 
	randKey=game_data.data[random.randint(0, 49)]
	A_follower=randKey.get("follower_count")
	randKey2=game_data.data[random.randint(0, 49)]
	B_follower=randKey2.get("follower_count")
 
	userwon =user_won(A_follower,B_follower,guess)
	return userwon
  

def user_won(A_follower,B_follower,guess):
	# Kullanici kazanip kaybetti mi onu belirliyor , puani artiriyor
	global score
	max_followerOfA_B=max(A_follower,B_follower)
	if A_follower>B_follower:
		bigger="A"
		print(bigger, max_followerOfA_B)
	else:
		bigger="B"
		print(bigger, max_followerOfA_B)
	 
	if guess!=bigger:
		print(f"Sorry, that's wrong. Final score: {score}")
		sys.exit(2)
		return False
		
	elif guess==bigger:
		print("You are right!")
		score+=1
		print(f"Your score is {score}\n")
		return True
	
def esitle():
	#print("esitleme vakti:\n")
	global B,A
	temp=A
	A=B
	#B=game_data.data[random.randint(0, 49)]
	B = randomer("B")
	# print("neu h1/A,h2/B:" ,A,"\nB:",B,"\n")
	print(vs)
	print(f"New B selected")

	A = randomer("A")
	print(vs)
	B = randomer("B")

	result = compare_num()
	if result == -1:
		return -1
	else:
		esitle()
		

 
def round():
	randomer("A")
	print(vs)
	randomer("B")
	user_input= input("A or B ? ")
	possible_user_input = ["A","B"]
	if user_input.capitalize() not in possible_user_input:
		print("YOu can only type A or B")
		exit(2)
		
	return compare_num(user_input)
	

def main():
	print(logo) 
	print("Welcome to the 'Higher vs Lower' game!\n")
	result = round()

	while result is True:
		round()
	
main()