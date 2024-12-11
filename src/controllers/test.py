from flask import request
# from swagger_server.models.test import Test

# params，query都根据文档定义可以在controller函数参数里直接获取参数值，参数的顺序不影响取值
# body参数只可以根据文档定义的body对象的name从controller函数参数里直接获取整个body的dict数据，且数据类型保持不变
# 文档里定义的接口参数，写在controller函数参数里的直接用，非string类型的数据会保持原有类型，query和body都是
# request对象获取的接口参数，body数据会保持参数原有类型，query则不会，全部为字符串类型
# 文档对query和body中的参数的require，数据类型做了保护，在以controller函数参数获取接口参数的情况下，controller函数内部不必对这些保护做校验
# path中的变量数据不受文档保护，类型和require都不保护
# 总结：query参数使用controller函数参数获取，body参数使用文档定义的body别名name属性获取整个body的dict数据


# 通过request获得的body数据，是数据原来的类型，不会转化为字符串
def test_result_post(id, keyword, body):
    # body = request.get_json()
    print('=====================body:', body, body['has'], type(body['has']))
    print('=====================params:', id, type(id), keyword, type(keyword))
    # return HTTP.test_to_device_post(333, 'lhf', body)
    # return Test.paginate(page=1, per_page=10)


# 通过request对象获取和在函数参数中获取query的区别，request对象获取的所有数据均是字符串，函数参数中获取的会根据文档定义的数据类型自动转化为number，boolean等
def test_result_get(id, keyword, page, enable):
    query = request.args
    print('=====================query:', query)
    print(
        '=====================params:',
        id, type(id), keyword, type(keyword), page, type(page),
        enable, type(enable),
        query['enable'], type(query['enable'])
    )
    # print('========================= get start ========================')
    # ss = HTTP.test_to_device_get(id, keyword, query)
    # print(ss)
    # print('========================= get end ========================')
    # return Test.find_many()
