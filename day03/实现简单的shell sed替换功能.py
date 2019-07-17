'''
简单实现shell seq的替换功能
'''

old_string = input("请输入你要替换的字符：")
new_string = input("输入替换后的字符：")

f = open("seq_testfile.txt", "r", encoding="utf-8")
f_new = open("seq_result.txt", "w", encoding="utf-8")

for line in f:
    if old_string in line:
        print(line)
        line = line.replace(old_string, new_string)
    f_new.write(line)
f.close()
f_new.close()
