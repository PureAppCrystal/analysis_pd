# json_request.py

import sys
from urllib.request import Request, urlopen
from datetime import *
import json


def json_request(url='',
                 encoding='utf-8',
                 success=None,
                 error=lambda e: print("%s : %s" % (datetime.now(), e), file=sys.stderr)):
    try:
        request = Request(url)
        resp = urlopen(request)

        resp_body = resp.read().decode(encoding)
        json_result = json.loads(resp_body)

        print('%s : success for request [%s]' % (datetime.now(), url))

        # success 함수인지 체크하고 아니면 결과를 리턴, 맞으면 함수를 호출
        if callable(success) is False:
            return json_result

        success(json_result)
    except Exception as e:
        callable(error) and error(e)
