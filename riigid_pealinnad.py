print("Made by Arkadi Korotots TARpv22")

from europamodul import *
eurig1,eurig2=loe("riigid_pealinnad.txt")
while True:
    menu=input("1-Vaatama Euroopa riigid \n2-Otsige riiki või pealinna \n3-Lisa riik ja pealinn\n4-Paranda riik või pealinn\n5-Salvestama\n6-Harjutus\n")
    if menu=="1":
        print(eurig1)
    elif menu=="2":
        eurig1=otsi(eurig1,eurig2)
    elif menu=="3":
        eurig1=lisa(eurig1,eurig2)
    elif menu=="4":
        eurig1,eurig2=paranda(eurig1,eurig2)
    elif menu=="5":
        salvestama(eurig1,"riigid_pealinnad.txt")
        print("Fail salvestatud!")
    elif menu=="6":
        trenniga(eurig1)
    else:
        print("Kirjutage ainult need numbrid, mis teil on ")
