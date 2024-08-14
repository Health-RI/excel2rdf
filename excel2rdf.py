import requests

url = "https://xls2rdf.sparna.fr/rest/convert?url=https://skos-play.sparna.fr/play/excel_test/excel2skos-exemple-1.xlsx"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
