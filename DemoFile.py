# DemoFile.py

print("---정렬방식---")
for x in range(1,6):
    print(x,"*",x,"=",x*x)



print("---오른쪽정렬---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3))
    
print("---0으로 채우기---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).zfill(3))

print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(15000000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))


# 문자열과 숫자를 합하려고 숫자를 문자화(str)사용
url = "http://www.credu.com/?page=" + str(1)
print(url)

#파일을 생성
f = open("demo.txt", "wt")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#파일을 읽어서 처리
f = open("demo.txt", "rt")
result = f.read()
print(result)
# f.close()

print(f.tell())
f.seek(0)
lst=f.readlines()
print(lst)
for item in lst:
   # print(item)  -> 글자들 사이에 빈캄이 생김
   print(item, end="")

#처음으로 리셋
f.seek(0)
print(f.readline(), end="")
print(f.readline(), end="")
f.close()

#with 구문을 같이 사용하는 경우
with open("demo.txt", "rt") as f:
    for item in f.readlines():
        print(item, end="")
        
