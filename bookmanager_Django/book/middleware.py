
# 中间件定义
# 中间作用 ：每次请求和相应都会调用
# 中间间的使用： 我们可以判断每次请求中是否携带cookie信息

from django.http import HttpResponse


def simple_middleware(get_response):

    # 这里是中间件第一次调用执行的地方
    print('init1111')

    def middleware(request):

        # username = request.COOKIES.get('username')
        # if username is None:
        #     print('username is None')
        #     return HttpResponse('您好，您未登录')

        # 这里是请求前
        print('before request')
        response = get_response(request)
        # 这里是请求后
        print('after request/response')
        return response

    return middleware