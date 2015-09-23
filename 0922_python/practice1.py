print"당신이 태어난 년도를 입력하세요"
year=raw_input()
nai=2015-int(year)+1
if 20<=nai<=26:
    print"대학생"
elif 17<=nai<20:
    print"고등학생"
elif 14<=nai<17:
    print"중학생"
elif 8<=nai<14:
    print"초등학생"
else: print"학생이 아닙니다"
