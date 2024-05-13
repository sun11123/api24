import requests
class login():
    def login(self,user,ps):

        url="http://192.168.55.1:8000/api/user/login"
        data={"userName":user,"password":ps,"remember":False}
        r=requests.post(url,json=data)
        return r
if __name__=='__main__':
    l=login()
