import urllib.request
from html.parser import HTMLParser

class ExtractorTexto(HTMLParser):
    def __init__(self):
        super().__init__()
        self.texto = []
        self.ignorar = False
    
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.ignorar = True
    
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.ignorar = False
    
    def handle_data(self, data):
        if not self.ignorar:
            self.texto.append(data)
    
    def get_texto(self):
        return ' '.join(self.texto)

def contar_palabras(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    
    parser = ExtractorTexto()
    parser.feed(html)
    texto = parser.get_texto().lower()
    
    for char in '.,!?;:()[]{}"\'-<>/\\=+*&^%$#@~`|':
        texto = texto.replace(char, ' ')
    
    palabras = texto.split()
    
    contador = {}
    for palabra in palabras:
        contador[palabra] = contador.get(palabra, 0) + 1
    
    lista = []
    for palabra, frecuencia in contador.items():
        lista.append((frecuencia, palabra))
    
    lista.sort(reverse=True)
    
    print("Las 10 palabras más comunes:")
    for frecuencia, palabra in lista[:10]:
        print(f"  {palabra}: {frecuencia} veces")

url = "https://en.wikipedia.org/wiki/Investment_banking"
contar_palabras(url)