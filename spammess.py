import requests
from time import sleep

class SpamMsgFacebook:
    def __init__(self,Cookies_FB) -> None:
        cookie = Cookies_FB.split(';')
        title = []
        value = []
        for i in range(len(cookie) - 1):
            title.append(cookie[i].split('=')[0].strip())
            value.append(cookie[i].split('=')[1].strip())
        self.cookies = dict(zip(title, value))
        
        self.headers = {
        'authority': 'm.facebook.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'dpr': '1',
        'origin': 'https://m.facebook.com',
        'referer': 'https://m.facebook.com/messages/read/?fbid=100076657214923&entrypoint=profile_message_button&eav=Afb8tLpjRFk8Ig2JtCGB9VNOg2pBifM6y4i0N45WdL71saQQXHuWwXVkoqeEMtfBezM&paipv=0&_rdr',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.188", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.188"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"7.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'viewport-width': '641',
        'x-asbd-id': '129477',
        'x-fb-lsd': 'L-lxaNu6GShbW3_8stzPsJ',
        'x-msgr-region': 'PNB',
        'x-requested-with': 'XMLHttpRequest',
        'x-response-format': 'JSONStream',
    }
        self.uid = self.cookies['c_user']
    def GetUserName(self):
        facebook = requests.get(f"https://mbasic.facebook.com/{self.uid}/", headers=self.headers, cookies=self.cookies).text
        self.UserName = facebook.split('<title>')[1].split('</')[0]
        print(self.UserName)
    def run(self, id,nd,so_lan_spam,delay):
        profile = requests.get(f"https://mbasic.facebook.com/{id}/",headers=self.headers,cookies=self.cookies).text
        NodeMess = "https://m.facebook.com/messages/thread/"+profile.split("/messages/thread/")[1].split('"')[0].replace("amp;", "")
        Mess = requests.get(NodeMess,headers=self.headers,cookies=self.cookies).text
        tids = Mess.split('name="tids" value="')[1].split('"')[0]
        wwwupp = Mess.split('name="wwwupp" value="')[1].split('"')[0]
        ids = Mess.split(f'name="ids[{id}]" value="')[1].split('"')[0]
        fb_dtsg = Mess.split('name="fb_dtsg" value="')[1].split('"')[0]
        jazoest = Mess.split('name="jazoest" value="')[1].split('"')[0]
        data = {
            "tids": tids,
            "wwwupp": wwwupp,
            f"ids[{id}]": ids,
            "body": nd,
            "waterfall_source" : "message",
            "fb_dtsg": fb_dtsg,
            "jazoest": jazoest,
            "__user": id,
        }
        url_post = "https://m.facebook.com/messages/send/?"+Mess.split('action="/messages/send/?')[1].split('"')[0].replace("amp;", "")
        for i in range(so_lan_spam):
            requests.post(url_post,headers=self.headers,cookies=self.cookies,data=data)
            print(f"/ Spam Nofication [{i}] / UID : {id} / Nội Dung Spam : {nd} / Đã Thực Hiện Spam !")
            sleep(delay)
        print("Done !")

cookies = input("Cookies : ")
uid_target = input("Nhap uid can spam : ")
nd = input("Nhap noi dung ban muon spam : ")
so_lan_spam = int(input("Nhap so lan muon spam : "))
delay = int(input("Nhap delay : "))
ApiFB = SpamMsgFacebook(cookies)
ApiFB.run(uid_target,nd,so_lan_spam,delay)
