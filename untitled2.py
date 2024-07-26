
#TATİL ÜCRETİ HESAPLAMA
kişi=input("kişi sayısını giriniz")
oda=input("oda sayısı yazınız")
lux=input("kral dairesi ister misiniz (e/h)")

if lux=="e"and oda=="1":
 print(int(kişi)*40000)
elif lux=="h" and oda=="1":
 print(int(kişi)*15000)
elif lux=="e" and oda>="1":
 print(int(kişi)*50000)
elif lux=="h"and oda>="1":
 print(int(kişi)*22500)
else:
 print("ücret hesaplanamadı")

