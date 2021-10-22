hour=int(input('enter the hour\n'))
minute=int(input("enter minutes\n"))
mode=input('am or pm?\n')
if minute<=60:
    if hour==12:
        if mode=="am":
            print("00",":",minute,mode)
        elif mode=="pm":
            print(12,":",minute,mode)
        else:
                print("your enter something wrong")
    elif hour==24 or hour==00:
        if mode=="am":
            print(12,":",minute,mode)
        else:
                print("your enter something wrong")
    elif mode=="am":    
        if hour<12:
            print(hour,":",minute,mode)
        else:
            print("your enter something wrong")
    elif mode=="pm":
        if hour<=23:
            if hour==1:
                print(13,":",minute,mode)
            elif hour==2:
                print(14,":",minute,mode)
            elif hour==3:
                print(15,":",minute,mode)
            elif hour==4:
                print(16,":",minute,mode)
            elif hour==5:
                print(17,":",minute,mode)
            elif hour==6:
                print(18,":",minute,mode)
            elif hour==7:
                print(19,":",minute,mode)
            elif hour==8:
                print(20,":",minute,mode)
            elif hour==9:
                print(21,":",minute,mode)
            elif hour==10:
                print(22,":",minute,mode)
            elif hour==11:
                print(23,":",minute,mode)
            elif hour==13:
                print(1,":",minute,mode)
            elif hour==14:
                print(2,":",minute,mode)
            elif hour==15:
                print(3,":",minute,mode)
            elif hour==16:
                print(4,":",minute,mode)
            elif hour==17:
                print(5,":",minute,mode)
            elif hour==18:
                print(6,":",minute,mode)
            elif hour==19:
                print(7,":",minute,mode)
            elif hour==20:
                print(8,":",minute,mode)
            elif hour==21:
                print(9,":",minute,mode)
            elif hour==22:
                print(10,":",minute,mode)
            elif hour==23:
                print(11,":",minute,mode)
            else:
                print("your")
        else:
                print("your enter ")
    else:
                print("your enter something ")
else:
                print("your enter something wrong")


        
