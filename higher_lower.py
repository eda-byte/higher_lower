import random
import game_data
from art import logo, vs
def main(): 
    print("hey there") 
 print(logo)
print("Welcome to the 'Higher vs Lower' game!\n")
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

score=0
result=0
#value = data.values()[index]
def game( ):
  guess=0
  bigger=0
  #score=0
  #kaydet=[]

  def randomer(harf):
    randKey=game_data.data[random.randint(0, 49)]
  
  
    followers=randKey.get("follower_count")#A
    get_name=randKey.get("name")
    get_descr=randKey.get("description")
    get_country=randKey.get("country")
   
    print(f"Compare {harf}:",get_name,":",get_descr,"from",get_country)
   # print("Randkey in randomer:",randKey)
    return randKey
  
  global A,B

  A=randomer("A")
  print(vs)
  B=randomer("B")

  def compare_num():#returns the A one
    global score
    randKey=game_data.data[random.randint(0, 49)]
    A_follower=randKey.get("follower_count")
    randKey2=game_data.data[random.randint(0, 49)]
    B_follower=randKey2.get("follower_count")
    
  
    max_followerOfA_B=max(A_follower,B_follower)
    if A_follower>B_follower:
      bigger="A"
      print(bigger, max_followerOfA_B)
     # print("Randkeey:",randKey)
     # return randKey
    else:
      bigger="B"
      
      print(bigger, max_followerOfA_B)
   # print("bigger max:",bigger)
    guess= input("Who has more followers? Type 'A' or 'B'\n") 
    if guess!=bigger:
      print(f"Sorry, that's wrong. Final score: {score}")
      return -1
       
    elif guess==bigger:
      print("You are right!")
      score+=1
      print(f"Your score is {score}\n")
    #print("RRRandkeey in compareNum:",randKey)
    return randKey
    
 
  
  
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
    
while True: 
  result = game() 
  if result == -1: 
      break  # Exit the loop if the desired value is reached 