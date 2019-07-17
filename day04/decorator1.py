'''
语法糖
'''
user, passwd = "abc", "123"


def auth(auth_type):
    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            
            if auth_type == "local":
                username = input("username:").strip()
                password = input("passwd:").strip()
                if user == username and passwd == password:
                    print("user has passed authentication.") 
                    res = "---------" + func(*args, **kwargs)
                    return res
                else:
                    exit("用户名或密码错误。")
            elif auth_type == "ldap":
                print("搞毛线ldap,不会。。。。")
        return wrapper
    return out_wrapper

def index():
   print("wellcome to index page.")


@auth(auth_type = "local")
def home(name):
    print("wellcome to %s's home page." % name)
    return "%s's home page." % name

@auth(auth_type = "ldap")
def bbs():
    print("wellcome to bbs page.")


index()
home("yzn")
bbs()
