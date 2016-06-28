contacts_lists = [
    {"이름": "이상흔",
   "학교": "서울대학교",
   "학과": "중어중문학과",
   "전화번호": "010-8242-7753"},
]

user_input = input("이름을 입력해 주세요 : ")

for contact in contacts_lists:
    if contact["이름"] == user_input:
        print("학교: {0}\n학과: {1}\n휴대폰번호: {2}".format(
            contact["학교"], contact["학과"],
            contact["전화번호"]))
