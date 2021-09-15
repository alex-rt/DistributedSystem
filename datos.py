import requests

dlurl = 'http://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip'

req = requests.get(dlurl)

filename = req.url[dlurl.rfind('/')+1:]

with open(filename, 'wb') as f:
    for chunk in req.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)


from zipfile import ZipFile

with ZipFile('datos_abiertos_covid19.zip', 'r') as zipObj:

   zipObj.extractall()