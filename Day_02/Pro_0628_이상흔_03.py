contacts_lists = [
    {"이름": "김범준",
   "학교": "서울대학교",
   "학과": "경영학과",
   "전화번호": "010-8242-7753"},
    {"이름": "김지은",
   "학교": "이화여자대학교",
   "학과": "컴퓨터공학과",
   "전화번호": "010-8242-7753"},
    {"이름": "안주은",
   "학교": "한양대학교",
   "학과": "중정보시스템학과",
   "전화번호": "010-8242-7753"},
    {"이름": "민영기",
   "학교": "서울대학교",
   "학과": "기계항공공학부",
   "전화번호": "010-8242-7753"},
    {"이름": "이상흔",
   "학교": "서울대학교",
   "학과": "중어중문학과",
   "전화번호": "010-8242-7753"},
    {"이름": "서성욱",
   "학교": "서울대학교",
   "학과": "기계항공공학부",
   "전화번호": "010-8242-7753"},
    {"이름": "김원빈",
   "학교": "서울대학교",
   "학과": "경영학과",
   "전화번호": "010-8242-7753"},
    {"이름": "박연준",
   "학교": "서울대학교",
   "학과": "에너지자원공학부",
   "전화번호": "010-8242-7753"},
    {"이름": "이현인",
   "학교": "서울대학교",
   "학과": "기계항공공학부",
   "전화번호": "010-8242-7753"},
    {"이름": "고희원",
   "학교": "이화여자대학교",
   "학과": "컴퓨터공학",
   "전화번호": "010-8242-7753"},
    {"이름": "이경연",
   "학교": "카이스트",
   "학과": "산업디자인",
   "전화번호": "010-8242-7753"},
    {"이름": "최이준",
   "학교": "한양대학교",
   "학과": "정보시스템학과",
   "전화번호": "010-8242-7753"},
    {"이름": "김지훈",
   "학교": "한양대학교",
   "학과": "정보시스템학과",
   "전화번호": "010-8242-7753"},
    {"이름": "공현택",
   "학교": "한양대학교",
   "학과": "정보시스템학과",
   "전화번호": "010-8242-7753"},
    {"이름": "김현중",
   "학교": "한양대학교",
   "학과": "정보시스템학과",
   "전화번호": "010-8242-7753"},
    {"이름": "이혜린",
   "학교": "한양대학교",
   "학과": "정보시스템학과",
   "전화번호": "010-8242-7753"},
    {"이름": "이영은",
   "학교": "한양대학교",
   "학과": "정보시스템학과",
   "전화번호": "010-8242-7753"},
    {"이름": "오슬기",
   "학교": "서울대학교",
   "학과": "경영학과",
   "전화번호": "010-8242-7753"},
    {"이름": "김병재",
   "학교": "서울대학교",
   "학과": "산업인력개발학과",
   "전화번호": "010-8242-7753"},
    {"이름": "한민호",
   "학교": "서울대학교",
   "학과": "경제학과",
   "전화번호": "010-8242-7753"},
    {"이름": "황서영",
   "학교": "카이스트",
   "학과": "산업 및 시스템공학과",
   "전화번호": "010-8242-7753"},
   {"이름": "배주혁",
   "학교": "한양대학교",
   "학과": "정보시스템학과",
   "전화번호": "010-8242-7753"},
   {"이름": "권진환",
   "학교": "서울대학교",
   "학과": "경제학과",
   "전화번호": "010-8242-7753"},
   {"이름": "전민규",
   "학교": "서울대학교",
   "학과": "경영학과",
   "전화번호": "010-8242-7753"},
   {"이름": "김유현",
   "학교": "숙명여자대학교",
   "학과": "한국어문학",
   "전화번호": "010-8242-7753"},
   {"이름": "한효정",
   "학교": "이화여자대학교",
   "학과": "광고홍보학과",
   "전화번호": "010-8242-7753"},
   {"이름": "허수정",
   "학교": "이화여자대학교",
   "학과": "중어중문학과",
   "전화번호": "010-8242-7753"},
   {"이름": "이아영",
   "학교": "한양대학교",
   "학과": "문화콘텐츠학과",
   "전화번호": "010-8242-7753"},
]

user_input = input("이름을 입력해 주세요 : ")

for contact in contacts_lists:
    if contact["이름"] == user_input:
        print("학교: {0}\n학과: {1}\n휴대폰번호: {2}".format(
            contact["학교"], contact["학과"],
            contact["전화번호"]))