
import requests
#>>https://api.telegram.org/bot5428603065:AAFFKL2Wjh4dLvnQ5pgJbebqSj0s4WkYelk/sendMessage?chat_id=-5367598877&text=ÜYE NOTU YOK
a=353
while True:
    try:
        while True:
            try:
                url = "https://www.zurihbet"+str(a)+".com"
                response = requests.head(url, timeout=5)

            
                print("Site Aktif") 
            except requests.exceptions.Timeout:
                mesajgndr="https://api.telegram.org/bot5428603065:AAFFKL2Wjh4dLvnQ5pgJbebqSj0s4WkYelk/sendMessage?chat_id=-768053785&text=Domain kapandı "+url+""
                msj=requests.get(mesajgndr) 
                print("Site kapalı")
                a=a+1
    except:
        print("Bağlantı kesildi")
