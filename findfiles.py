import os


def create_mp4(filename):
    """
    执行合并转换
    """
    DIR = os.path.dirname(os.path.abspath(__file__))
    DIR1 = DIR.replace("\\", "/")
    keyDir = "".join([DIR1, "/0.key"])

    f = open(filename, mode="r")
    old_data = f.readlines()
    f.close()

    new_data = ''
    ts_num = 0

    for index in old_data:
        if index.find(".ts") != -1:
            index = str(ts_num) + ".ts\n"
            ts_num += 1
        elif index.find("key.key") != -1:
            index = index.replace("key.key", keyDir)
        new_data = new_data + index

    f = open(filename, mode="w")
    f.write(new_data)
    f.close()

    cmd = ''.join(
        ["ffmpeg -allowed_extensions ALL -i ", filename, " -c copy ", DIR, ".MP4"])
    os.system(cmd)


if __name__ == '__main__':
    for filename in os.listdir():
        if filename.find(".m3u8") != -1:
            d = os.path.getsize(filename)
            if d > 1000:
                create_mp4(filename)
                break
