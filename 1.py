#自动将m3u8合并并转换成MP4格式


f = open("1.m3u8", mode="r")
old_data = f.read()
f.close()
# print(old_data)
index = old_data.find("key.key")
print(index)
