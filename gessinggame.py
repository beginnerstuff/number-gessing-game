import random


class game:
    print("Aklınızdan 1 den 10 e kadar bir sayı tutun!")
    sayac = 1
    while True:
        number = random.randint(1, 10)
        tahmin = int(input("tahmininizi giriniz:"))
        control = True
        while control:
            
            if tahmin == number:
                print("tebrikler doğru cevap!")
                print("tebrikler {}".format(sayac) + ".seferde bildiniz!")
                input("\nçıkmak için bir tuşa basın.")
                sayac = 1
                control = False
                
            elif tahmin >= 10 or tahmin < 1:
                print("1 ile 10 arasında bir sayı girin lütfen!!")
                tahmin = int(input("Mesela {}".format(number) + " gibi :"))
                sayac += 1
            
            elif tahmin != number:
                print("yanlış cevap")
                tahmin = int(input("tekrar deneyiniz:"))
                sayac += 1
