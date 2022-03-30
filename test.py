import requests
import shutil

url = "https://www.superherodb.com/pictures2/portraits/10/100/10060.jpg"

image = requests.get(url, stream = True)

if image.status_code == 200:
    image.raw.decode_content = True
    
    with open("./assests/test.jpg","wb") as file:
        shutil.copyfileobj(image.raw,file)