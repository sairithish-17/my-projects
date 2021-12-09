p=0
def run():
    global p
    a=input()
    if a==ans:
        print('correct')
        p=p+1
    elif a=='pass':
        pass
    else:
        print('no')
        print(f'{ans}')
print('movies or gk')
c=input()
if c=='movies':
    for i in range(1,6):
        if i==1:
            print("venkatesh's last movie")
            ans='venkymama'
            run()
        elif i==2:
            print("nagarjuna's last movie")
            ans='manmadhudu2'
            run()
        elif i==3:
            print("VD's next film")
            ans='fighter'
            run()
        elif i==4:
            print("rana's next movie")
            ans='aranya'
            run()
        elif i==5:
            print('prabhas,om rout movie')
            ans='adipurush'
            run()
        else:
            print('no')
elif c=='gk':
    for i in range(1,6):
        if i==1:
            print("1st pm")
            ans='nehru'
            run()
        elif i==2:
            print("1st president")
            ans="rajendra prasad"
            run()
        elif i==3:
            print("1st cm of ts")
            ans='kcr'
            run()
        elif i==4:
            print("1st cm of andhra") 
            ans='neelam'
            run()
        elif i==5:
            print('who established TDP')
            ans='ntr'
            run()
        else:
            print('no')
else:
    print('are you blind?') 
    print('there are only 2 options ')           
print(f'your score is {p}')                            