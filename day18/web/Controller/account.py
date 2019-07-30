import time


def handle_index():
    f = open('View/index.html', mode='rb')
    v = str(time.time())
    data = f.read()
    f.close()
    data = data.replace('@uuu'.encode('utf-8'), v.encode('utf-8'))
    return [data, ]


def handle_data():
    return ['<h1>Hello Data!</h1>'.encode('utf-8'), ]
