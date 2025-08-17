Registration_dic = {}
#注册
while True:
    R_name = input("用户名:",)
    if R_name not in Registration_dic:
        Registration_dic[R_name] = {}
        print("取名成功")
        print(Registration_dic)
        break
    else:
        print(f"名称{R_name}已存在,请重试")

while True:
        R_password = input("密码:", )
        if 8<= len(R_password) <=16:
            while True:
                R_password2 = input("请再次输入密码:", )
                if R_password2 == R_password:
                    print('注册成功！')
                    R_hash_pw =hash(R_password)
                    Registration_dic[R_name]['hash_pw'] = R_hash_pw
                    break
            break
        else:
            print("密码格式错误，请重试")

print("请尝试登录吧")
#登录
while True:
    name = input("用户名:",)
    if name not in Registration_dic:
        print("用户名不存在,请重试")
    else:
        while True:
            password = input("请输入密码:",)
            hash_pw = hash(password)
            if hash_pw == Registration_dic[name]['hash_pw']:
                print("登陆成功")
                break
            else:
                print("密码错误,请重试")
        break









