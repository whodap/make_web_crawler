#!__*__coding:utf-8__*__
import requests
import re
from bs4 import BeautifulSoup

# 제목에서 HTML 태그 없애기
def get_title(title):
    bs = BeautifulSoup(title, "lxml")
    return bs.get_text()


# 빈 줄만 찾아서 제거
def remove_empty_line(a):
    j = a.splitlines()
    x = []
    for i in j:
        if len(i.strip()) > 0:
            x.append(i)
    return "\r\n".join(x)

#네이버 블로그 글 앞뒤 정리하기
def remove_extra_text(c):
    return c
    idx = c.find("번역보기")
    c = c[idx + 4:]
    idx = c.find("모바일에서 작성된 글입니다.")
    c = c[:idx]
    idx = c.find("태그저장")
    c = c[:idx]
    return c

# 네이버 블로그 본문 가져오기
def get_main_content(url):
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    c = bs.find(id="mainFrame")
    d = c["src"]
    e = "http://blog.naver.com" + d
    response2 = requests.get(e)
    bs = BeautifulSoup(response2.text, "lxml")
    bs = bs.find(id="postListBody")
    for rs in bs(["style", "script"]):
        rs.decompose()
    result = bs.get_text()
    result = remove_empty_line(result)
    return result


if __name__ == "__main__":
    result = get_main_content("http://blog.naver.com/09x43/221152682174")
    result2 = remove_empty_line(result)
    fout = open("결과.txt", "w", encoding="utf-8")
    fout.write(result2)
    fout.close()
