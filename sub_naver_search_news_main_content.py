#!__*__coding:utf-8__*__
import requests
import re
from bs4 import BeautifulSoup
import chardet

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
    # p.151  return : 함수의 결과값을 돌려주는 명령어


# 네이버 뉴스 본문 가져오기
def get_main_content_from_news(url):
    try:
        print(url)
        response = requests.get(url)
        bs = BeautifulSoup(response.text, "lxml")
        for rs in bs(["style", "script"]):
            rs.decompose()
        result = bs.get_text()
    except:
        result = ""
    return result


if __name__ == "__main__":
    result = get_main_content_from_news("http://blog.naver.com/09x43/221152682174")
    result2 = remove_empty_line(result)
    fout = open("결과.txt", "w", encoding="utf-8")
    fout.write(result2)
    fout.close()
