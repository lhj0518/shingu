import random
guess_number=random.randint(1,100)
print"���ڸ� ���纸����(1~100)"
users_input=int(raw_input())
while(users_input<>guess_number):
    if users_input>guess_number:
        print"���ڰ� �ʹ� Ů�ϴ�"
    else:
        print"���ڰ� �ʹ� �۽��ϴ�"
    users_input=int(raw_input())
else: print"�����Դϴ�.","�Է��Ѽ��ڴ�",users_input,"�Դϴ�"
