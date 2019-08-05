# 自动将m3u8合并并转换成MP4格式
import os


DIR = os.path.dirname(os.path.abspath(__file__))
DIR1 = DIR.replace("\\", "/")
keyDir = "".join([DIR1, "/0.key"])

f = open("1.m3u8", mode="r")
old_data = f.readlines()
f.close()

new_data = ''
ts_num = 0
for index in old_data:
    # print(index)
    if index.find(".ts") != -1:
        index = str(ts_num) + ".ts\n"
        ts_num += 1
    elif index.find("key.key") != -1:
        index = index.replace("key.key", keyDir)

    new_data = new_data + index

f = open("1.m3u8", mode="w")
f.write(new_data)
f.close()

CMD = ''.join(
    ["ffmpeg -allowed_extensions ALL -i 1.m3u8 -c copy ", DIR, ".MP4"])
ver = os.system(CMD)
