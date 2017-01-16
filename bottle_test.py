import json
from bottle import route, run

from burn import burn_cpu

@route('/test')
def hello():
    rsp_time = burn_cpu()

    return json.dumps({'elapse': rsp_time})

run(host='localhost', port=8080)
