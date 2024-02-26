import hashlib


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        hash_object = hashlib.sha256(password.encode())
        hex_dig = hash_object.hexdigest()
        self.password = hex_dig

    def display(self):
        print(self.name)
        print(self.username)


class Post:
    def __init__(self, title, content, username):
        self.title = title
        self.content = content
        self.author = username


# 빈 리스트 생성
members = []
posts = []

# 멤버 생성
members.append(Member('김범중', 'kbeom0124', '123456789'))
members.append(Member('스파르타', 'sparta', 'asdfqwer'))
members.append(Member('스파르탄', 'spartan', 'qwe123'))
# 포스트 생성
posts.append(Post('과일', '사과, 배, 딸기', 'kbeom0124'))
posts.append(Post('맛있는 과일', '사과, 토마토, 키위', 'kbeom0124'))
posts.append(Post('토마토는 과일인가?', '토마토는 과일이 아니다', 'kbeom0124'))
posts.append(Post('계절', '봄, 여름, 가을, 겨울', 'sparta'))
posts.append(Post('좋아하는 날씨', '가을이 제일 좋아', 'sparta'))
posts.append(Post('일기 예보', '오늘은 비가 올 예정입니다', 'sparta'))
posts.append(Post('AI 웹개발', '스파르타 내일배움 캠프', 'spartan'))
posts.append(Post('스파르타 코딩클럽', 'AI 웹개발', 'spartan'))
posts.append(Post('내일배움캠프', '내일배움캠프 TIL', 'spartan'))


# 작성자 필터
for post in posts:
    if post.author == 'sparta':
        print(post.title)

# 단어 필터
for post in posts:
    if '캠프' in post.content:
        print(post.title)

# 사용자 추가
name = input('이름: ')
username = input('사용자 id: ')
password = input('비밀번호: ')
members.append(Member(name, username, password))

for member in members:
    Member.display(member)

# 개시글 추가
title = input('제목: ')
content = input('내용: ')
author = input('작성자: ')
posts.append(Post(title, content, author))

# 개시글 전부 출력 제목/내용/작성자 순
for post in posts:
    print(post.title, post.content, post.author)
