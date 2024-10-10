# Barışcan Çeken - Tek Kişilik Amiral Battı
# Nakahtumu = Umuthakan 

import random

kordinatlar = {"a1": 1, "a2": 9, "a3": 17, "a4": 25, "a5": 33, "a6": 41, "a7": 49, "a8": 57,"b1": 2, "b2": 10, "b3": 18, "b4": 26, "b5": 34, "b6": 42, "b7": 50, "b8": 58,"c1": 3, "c2": 11, "c3": 19, "c4": 27, "c5": 35, "c6": 43, "c7": 51, "c8": 59,"d1": 4, "d2": 12, "d3": 20, "d4": 28, "d5": 36, "d6": 44, "d7": 52, "d8": 60,"e1": 5, "e2": 13, "e3": 21, "e4": 29, "e5": 37, "e6": 45, "e7": 53, "e8": 61,"f1": 6, "f2": 14, "f3": 22, "f4": 30, "f5": 38, "f6": 46, "f7": 54, "f8": 62,"g1": 7, "g2": 15, "g3": 23, "g4": 31, "g5": 39, "g6": 47, "g7": 55, "g8": 63,"h1": 8, "h2": 16, "h3": 24, "h4": 32, "h5": 40, "h6": 48, "h7": 56, "h8": 64}
print("Oyuna Hoş Geldin!")

kacgemi = int(input("Kaç Gemi İle Oyun Oynamak İstiyorsun?"))
while kacgemi < 1 or kacgemi > 63 :
       print("Hatalı Değer Girdiniz!")
       exit()
kalan = kacgemi
geminolari2 = random.sample(range(1,64 ), kacgemi)
geminolari = random.sample(range(1,64 ), kacgemi)
gemiler = geminolari 
gemiler2 = geminolari2

d = 0
y = 0
b = 0
sayi = 0
deneme = 0

nakahtumuliste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64]
for x in range(64, 0, -1):
    a = x
    if a in  geminolari2 :
        d = d + 1
        geminolari2.remove(a)
        nakahtumuliste.remove(a)
        if d == kacgemi :
            sonbasarili = 64 - x
    elif a not in geminolari2 and a in nakahtumuliste:
        nakahtumuliste.remove(a)
        y = y + 1
    elif a not in geminolari2 and a not in nakahtumuliste:
        y = y + 1
        pass

    if d == kacgemi :
        print(f"Nakahtumu senin {kacgemi} tane gemini, {sonbasarili} atışta buldu.")
        print(f"Eğer Nakahtumu'nın gemilerini {sonbasarili} atıştan önce vurabilirsen maçı kazanacaksın başarılar! ")
        break

rakamlar = [1,2,3,4,5,6,7,8,9]

def oyuncu1(): 
      global sayi
      global deneme
      konumsec = input("Konum belirlemek için bir konum girin(a1 - h8 e kadar) : ")
      
      if  konumsec in kordinatlar and kordinatlar[konumsec] in gemiler :
                  sayi += 1
                  deneme += 1
                  print("Hedefi Vurdunuz!")
                  if kordinatlar[konumsec] in rakamlar :
                         kordinatlar[konumsec] = "X"
                  else :
                         kordinatlar[konumsec] = "X."
                         
                  

      elif konumsec in kordinatlar and kordinatlar[konumsec] not in gemiler :
                  print("Boşa Atış Yaptınız!")
                  deneme += 1
                  if kordinatlar[konumsec] in rakamlar :
                         kordinatlar[konumsec] = "O"
                  else :
                         kordinatlar[konumsec] = "O"



      elif konumsec not in kordinatlar :
                  print("Doğrı bir şekilde kordinat girdiğinize emin olun.")           


      a1, a2, a3, a4, a5, a6, a7, a8 = kordinatlar["a1"], kordinatlar["a2"], kordinatlar["a3"], kordinatlar["a4"], kordinatlar["a5"], kordinatlar["a6"], kordinatlar["a7"], kordinatlar["a8"]
      b1, b2, b3, b4, b5, b6, b7, b8 = kordinatlar["b1"], kordinatlar["b2"], kordinatlar["b3"], kordinatlar["b4"], kordinatlar["b5"], kordinatlar["b6"], kordinatlar["b7"], kordinatlar["b8"]
      c1, c2, c3, c4, c5, c6, c7, c8 = kordinatlar["c1"], kordinatlar["c2"], kordinatlar["c3"], kordinatlar["c4"], kordinatlar["c5"], kordinatlar["c6"], kordinatlar["c7"], kordinatlar["c8"]
      d1, d2, d3, d4, d5, d6, d7, d8 = kordinatlar["d1"], kordinatlar["d2"], kordinatlar["d3"], kordinatlar["d4"], kordinatlar["d5"], kordinatlar["d6"], kordinatlar["d7"], kordinatlar["d8"]
      e1, e2, e3, e4, e5, e6, e7, e8 = kordinatlar["e1"], kordinatlar["e2"], kordinatlar["e3"], kordinatlar["e4"], kordinatlar["e5"], kordinatlar["e6"], kordinatlar["e7"], kordinatlar["e8"]
      f1, f2, f3, f4, f5, f6, f7, f8 = kordinatlar["f1"], kordinatlar["f2"], kordinatlar["f3"], kordinatlar["f4"], kordinatlar["f5"], kordinatlar["f6"], kordinatlar["f7"], kordinatlar["f8"]
      g1, g2, g3, g4, g5, g6, g7, g8 = kordinatlar["g1"], kordinatlar["g2"], kordinatlar["g3"], kordinatlar["g4"], kordinatlar["g5"], kordinatlar["g6"], kordinatlar["g7"], kordinatlar["g8"]
      h1, h2, h3, h4, h5, h6, h7, h8 = kordinatlar["h1"], kordinatlar["h2"], kordinatlar["h3"], kordinatlar["h4"], kordinatlar["h5"], kordinatlar["h6"], kordinatlar["h7"], kordinatlar["h8"]
      bccd = (f"+-----+-----+-----+-----+-----+-----+-----+-----+\n| {a8}  | {b8}  | {c8}  | {d8}  | {e8}  | {f8}  | {g8}  | {h8}  | 8 \n+-----+-----+-----+-----+-----+-----+-----+-----+\n| {a7}  | {b7}  | {c7}  | {d7}  | {e7}  | {f7}  | {g7}  | {h7}  | 7 \n+-----+-----+-----+-----+-----+-----+-----+-----+\n| {a6}  | {b6}  | {c6}  | {d6}  | {e6}  | {f6}  | {g6}  | {h6}  | 6 \n+-----+-----+-----+-----+-----+-----+-----+-----+\n| {a5}  | {b5}  | {c5}  | {d5}  | {e5}  | {f5}  | {g5}  | {h5}  | 5 \n+-----+-----+-----+-----+-----+-----+-----+-----+\n| {a4}  | {b4}  | {c4}  | {d4}  | {e4}  | {f4}  | {g4}  | {h4}  | 4 \n+-----+-----+-----+-----+-----+-----+-----+-----+\n| {a3}  | {b3}  | {c3}  | {d3}  | {e3}  | {f3}  | {g3}  | {h3}  | 3 \n+-----+-----+-----+-----+-----+-----+-----+-----+\n|  {a2}  | {b2}  | {c2}  | {d2}  | {e2}  | {f2}  | {g2}  | {h2}  | 2\n+-----+-----+-----+-----+-----+-----+-----+-----+\n|  {a1}  |  {b1}  |  {c1}  |  {d1}  |  {e1}  |  {f1}  |  {g1}  |  {h1}  | 1 \n+-----+-----+-----+-----+-----+-----+-----+-----+\n")
      

      print(bccd)


for i in range (sonbasarili) :
        if sayi != kacgemi :
               oyuncu1()
        elif sayi == kacgemi :
               if deneme > sonbasarili :
                      print("Nakahtumu oyunu kazandı! (her zamanki gibi) ")     
                      exit()  
               elif deneme == sonbasarili :
                      print("Nakahtumu'yla berabere kaldın !")
                      exit()
               elif deneme < sonbasarili :
                      print("Tebrikler Oyunu Kazandınız. Hamle Sayınız : ",deneme)
                      exit()


