#!__*__coding:utf-8__*__
# pip install pygame openpyxl bs4 requests pandas
# no module
# 다른 사람이 만든것, 실행을 해보면 필요하다고 말함
# 설치를 해달라고 요청
# 명령어 : pip install 설치
# 버전이 새로 나왔으니 업데이트 해라 "" 있는분에서 복붙해서 알아서 설치를 해줌, 이런 것이 파이썬의 장점이기도 함
# 따로 환경설정을 하지 않아도 다른 사람의 모듈을 가져다 쓸 수 있다.
import os
# p.249 OS 모듈은 환경변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈이다.
import sys
# p.177 sys 모듈로 매개변수 주기, 파이썬에서는 sys 모듈을 사용하여 매개 변수를 직접 줄 수 있다.
# p.247 sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈이다.
import sub_naver_search_blog as naver_blog
import sub_naver_search_news as naver_news
# p.208 import는 현재 디렉터리에 있는 파일이나 라이브러리가 저장된 디렉터리에 있는 모듈만 불러올 수 있다.
# 1. 해석 :  import 모듈이름 as 변경이름 = sub_naver_search_blog라는 제목을 blog로 변경해줘
# 2. 해석 :  import 모듈이름 as 변경이름 = sub_naver_search_news라는 제목을 naver_news로 변경해줘

class crawler:
# p.183 class는 개체 생성을 위한 확장 가능한 프로그램 코드를 지칭
# 프로그래머 관점에서는 붕어빵을 찍어낼 수 있는 틀을 클래스(class)라고 이해할 수 있으며, 붕어빵 틀에서 찍혀 나온 붕어빵 하나하나를 객체(object)라고 이해
# crawler라는 클래스를 생성한다.
# crawler라는 클래스 안에 blog와 new라는 함수가 묶여있는 것
    def do_blog(self):
        # p.150 함수 : def 함수 이름(매개변수) :
        #                      수행할 문장 1
        #                      수행할 문장 2
        # p.152 매개변수 : 함수에 입력으로 전달된 값을 받는 변수를 의미
        # p.152 인수 : 함수를 호출할 때 전달하는 입력값을 의미
        # self란 클래스의 인스턴스를 나타내는 변수
        # p.187 인스턴스 : 클래스로 만든 객체, 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용
        
        """
        네이버 블로그에서 해당 키워드를 검색합니다.
        """
        keyword = input("검색 키워드를 입력해 주십시오:")
        naver_blog.search_blog_main(keyword)
        # 해당 함수를 가지고 지정해준 키워드로 검색을 수행하게 됨
        # 모듈 sub_블로그가 구동되어 본 함수 값을 전달

    def do_news(self):
        # do_명령어 : 
        """
        네이버 뉴스에서 해당 키워드를 검색합니다.
        """
        keyword = input("검색 키워드를 입력해 주십시오:")
        naver_news.search_news_main(keyword)

# 모듈이 아니라 자기 자신을 실행할 경우 동작 C 언어의 main 느낌
if __name__ == "__main__":
# 210 ~ 211p __name__ : 파이썬이 내부적으로 사용하는 특별한 변수 이름    

    print("모듈이지만 스스로 동작, 유닛(모듈 테스트)")
    test = crawler()
    test.do_blog()
    # (=crawler).do_blog / 크라울러 밑에 있는 do_blog를 구동한다. 
    test.do_news()
    print("종료")
