#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:47:44 2019

@author: aishee
"""
def isvalid(s):
    arr=[0]*26
    for i in range(len(s)):
        arr[ord(s[i])-ord('a')]+=1
    f1=f2=count1=count2=0
    for i in range(26):
        if(arr[i]!=0):
            f1=arr[i]
            count1=1
            break
    for j in range(i+1,26):
        if(arr[j]!=0):
            if(arr[j]==f1):
                count1+=1
            else:
                f2=arr[j]
                count2=1
                break;
    for k in range(j+1,26):
        if(arr[k]!=0):
            if(arr[k]==f1):
                count1+=1
            elif(arr[k]==f2):
                count2+=1
            else:
                print("NO")
    print(count1)
    print(count2)
    if(count1==1 or count2==1):
        print("YES")
    elif((count1>1 and count2>1) or abs(arr[j]-arr[i])>1):
        print("NO")
#    else:
#        print("YES")
#    for i in range(26):
#        if(arr[i]!=0):
#            f1=arr[i]
#            break
#    for j in range(i+1,26):
#        if(arr[j]!=0 and arr[j]!=f1):
#            f2=arr[j]
#            break
#    for k in range(j+1,26):
#        if(arr[k]!=0 and arr[k]!=f1 and arr[k]!=f2):
#            print("NO")
#    if(abs(f2-f1)>1):
#        print("NO")
#    else:
#        print("YES")
#s='abcdefghhgfedecba'
#s='aabbcd'
s='aaaabc'
#s='ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'
isvalid(s)