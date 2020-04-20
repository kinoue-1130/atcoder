# -*- coding: utf-8

i = list(map(int,input().split()))#N,M取得

if 1 <= i[0] and i[0] <= 1000000 and 1 <= i[1] and i[1] <+ 1000:
    i_2 = list(map(int,input().split()))#A1-AM取得

    sum = 0

    for x in range(len(i_2)):
        if 1 <= i_2[x] and i_2[x] <= 10000:
            sum = sum + i_2[x]#課題をする日数
        else:
            print('Aiは1から10000で入力してください')
            break
    
    vac = i[0] - sum#休暇（休み全日ー課題の日数）

    if 0 <= vac:
        print(vac)
    else:
        print(-1)#宿題が終わらなかった
else:
    print('Nは1から1000000、またはMは1から10000で入力してください')
