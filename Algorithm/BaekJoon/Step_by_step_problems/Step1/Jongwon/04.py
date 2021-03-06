# # 강아지 출력하기 
# |\_/|
# |q p|   /}
# ( 0 )"""\
# |"^"`    |
# ||_/=\\__|

# my sol
print(r'''|\_/|
|q p|   /}
( 0 )"""\
|"^"`    |
||_/=\\__|''')

# 만약 escape char가 너무 많은 string을 바로 출력하고 싶다면 raw string을 사용하는 방법이 있다.
# raw string은 말 그대로 날 것의 문자열로 escape char를 무시하고 출력이 가능하다. 하지만 ' " '''등을 생략하는 것은 아니기에 적절한 quotes를 선택해서 string을 만들어야 한다.
# 위의 문제도 string 속에 ' "등이 있다. 이를 그대로 출력하기 위해서는 ''' string ''' 을 사용해야 한다.
