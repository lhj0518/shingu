
print"������ ����� ����ұ��(1~9)?"
x=1
while(x<>0):
    x=int(raw_input())
    if x==0: break
    if not(1<=x<=9):
        print"�߸� �Է��ϼ̽��ϴ�","1���� 9���� ���ڸ� �Է����ּ���"
        continue
    else:
        print"������"+str(x)+"���� ����մϴ�."
        for i in range(1,10):
            print str(x)+"X"+str(i)+"="+str(x*i)
        print"������ ����� ����ұ��(1~9)?"
print"������ ������ �����մϴ�"
