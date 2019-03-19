from bs4 import BeautifulSoup
import requests
import re

url = "https://www.tagindex.com/html5/elements/"

page = requests.get(url)
html = page.text

soup = BeautifulSoup(html, "html.parser")

code_objs = soup.select("code")
tags = [code.text.replace("<", "").replace(">", "") for code in code_objs]

print(tags)
