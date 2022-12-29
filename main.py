from urllib.request import urlopen
import requests
import json
import time




 





post = {}
posting = []
while True:
    url = 'https://api.moresneakers.com/api/v1/offers/?status=on_sale&maxPrice=1000&minPrice=0&displayWhatsNew=1&active=1&ordering=-updatedAt&pageIndex=1&pageSize=16'
    hdr = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
    response = requests.get(url, headers = hdr)

    code_js = json.loads(response.text)

    result = code_js.get('data')
    if response.status_code != 200:
        print("ERREUR")
    def get_info():    
        a=0
        for i in range(len(result)):
            links = result[i].get('links')
            prix_f = result[i].get('price')
            prix_ff = str(prix_f)
            url_f = links[0].get('url')
            pourcent_sold = result[a].get('salePercentage')
            r = int(prix_f)*int(pourcent_sold)/100
            prixreduc_f = int(prix_f) - r
            prixreduc_ff = str(prixreduc_f)
            nom_f = result[i].get('release').get('name')
            img_f = result[i].get('release').get('mainImage')
            shop_f = result[i].get('shop').get( 'name')
            code_f = result[i].get('discountCode')
        
            post = nom_f
            if post in posting:
                time.sleep(1)
                
                continue
            else:
                if code_f == "":
                    code_f = "None"  
        
                if str(lesinfo) in nom_f:
                    pass
                lesinfo[nom_f] = {}
                lesinfo[nom_f]["image"] = img_f
                lesinfo[nom_f]["prix"] = prix_ff
                lesinfo[nom_f]["prixreduit"] = prixreduc_ff
                lesinfo[nom_f]["url"] = url_f
                lesinfo[nom_f]["shop"] = shop_f
        
                with open('dico.json', 'w') as dicojson:
                    try:
                        lesinfo[nom_f]["code"] = code_f
                    except:
                        lesinfo[nom_f]["code"] = "None"

                    json.dump(lesinfo, dicojson, indent=4)
                    posting.append(post)
                    print("nouvel item")
                    print(i)
            
            
            
                a+=1
    
    lesinfo = {}
    get_info()




