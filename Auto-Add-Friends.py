# -*- coding: utf-8 -*-

#API FACEBOOK MUA LIÊN HỆ : FB.COM/NgxHieeus !!!

import ApiFacebook
import re, requests, os, time
from ApiFacebook import printf

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    os.system('title TOOL AUTO FRIENDS - NGXHIEEUS')
    banner = '''
                - Copyright © NgxHieeus -
          
    [          COPYRIGHT LICENSE: Ngx Hieeus        ]   
    [          FB: facebook.com/NgxHieeus           ]              
    [       TOOL AUTO ADD FRIENDS - By NgxHieeus    ]
    '''
    print(banner)

if __name__ == "__main__":
    banner()
    cookie = input("Nhap cookie: ")
    ApiFB = ApiFacebook.ApiFacebook(cookie)
    username, userid = ApiFB.GetUserName()
    if "Đăng nhập Facebook | Facebook" in username:
        printf("Vui lòng kiểm tra lại cookie !")
        exit()
    print(f"[ USERNAME : {username} | USERID : {userid} | STATUS : 200 ]")
    file_uid = open('UID_List.txt', 'w')
    delay = int(input("Nhập delay ( Khuyến khích trên 60s ) : "))
    full_uid_list = []
    for i in range(1): #Thích để bao nhiêu thì để ( >= 1 )
        uid_list = ApiFB.GetListAddFriend()
        print('=' * 80)
        printf(f"Đã tìm thấy {len(uid_list)} người có thể kết bạn ! Tiến hành kết bạn")
        for uid in uid_list:
            kb = ApiFB.FriendRequest(uid)
            if kb == "success":
                printf(f"[ UID : {uid} | Kết Bạn : Đã Gửi Lời Mời | Status : success ]")
                file_uid.write(str(uid) + '\n')
                full_uid_list.append(uid)
            time.sleep(delay)
        time.sleep(1)
