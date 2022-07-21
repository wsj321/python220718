# web1.py

from bs4 import BeautifulSoup

#페이지 로딩
page = open("test01.html", "rt", encoding="utf-8").read()

#검색이 용이한 객체
soup = BeautifulSoup(page, "thml.parser")
print(soup.prettify())

