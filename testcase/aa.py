import threadpool


def hello(m, n, o):
    print("m = %s, n = %s, o = %s" % (m, n, o))



if __name__ == '__main__':
    # 方法1
    lst_vars_1 = ['1', '2', '3']
    func_var = [(lst_vars_1, None)]
    pool = threadpool.ThreadPool(2)
    requests = threadpool.makeRequests(hello, func_var)
    print(requests)
    for req in requests:
        print(req)
        pool.putRequest(req)
    pool.wait()
