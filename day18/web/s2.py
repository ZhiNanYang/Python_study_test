from wsgiref.simple_server import make_server
from Controller import account

URL_DICT = {
    "/index": account.handle_index,
    "/data": account.handle_data,
}


def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    current_url = environ['PATH_INFO']
    func = None
    if current_url in URL_DICT:
        func = URL_DICT[current_url]
    if func:
        return func()
    else:
        return ['<h1>404!</h1>'.encode('utf-8'), ]


if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()
