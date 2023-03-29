'''
데코레이터 테스트
'''
from functools import wraps
# import datetime
import time

def logger ():
    '''로그 펑션'''
    print(time.time())

def arg_check_type(func):
    '''
    주어진 파라미터의 타입을 체크
    딕셔너리 타입이용 시 list_, str_ 등의 정확한 형식 요구사항을 가장 앞에 작성해야함 
    '''
    @wraps(func)
    def pct_inner(arg_type, *args, **kwargs):
        if arg_type is not None :
            for arg in range(len(args)):
                if not isinstance(arg, arg_type):
                    return f"ERR_{args.index(arg)} is not type{arg_type}"
            return func(*args)
        elif arg_type is None :
            for key, value in kwargs:
                if not isinstance(value, key.split("_")[0]):
                    return f"ERR_{value} is not type{key}"
            return func(*kwargs)
    return pct_inner

def parm_check_match(func):
    '''주어진 파라미터의 일치여부를 체크'''
    @wraps(func)
    def pcm_inner(*args, **kwargs):
        return func(*args, **kwargs)
    return pcm_inner

def deco_log(func):
    '''로그 데코레이터'''
    @wraps(func)
    def innerfunc(*args, **kwargs):
        logger()
        return func(*args, **kwargs)
    return innerfunc

# @deco_log
# def accesser (a):
#     '''접근하는 펑션'''
#     print('Accessed', a)
#     return a

# a = accesser('a')
# b = accesser
# print(b)

# b('')
# print(b)

# b('w')
# print(b)

# b(a)

# print(a)



# from functools import wraps
# import datetime
# import time


# def my_logger(original_function):
#     import logging
#     filename = '{}.log'.format(original_function.__name__)
#     logging.basicConfig(handlers=[logging.FileHandler(filename, 'a', 'utf-8')],
#                         level=logging.INFO)

#     @wraps(original_function)  # 1
#     def wrapper(*args, **kwargs):
#         timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
#         logging.info(
#             '[{}] 실행결과 args - {}, kwargs - {}'.format(timestamp, args, kwargs))
#         return original_function(*args, **kwargs)

#     return wrapper


# def my_timer(original_function):
#     import time

#     @wraps(original_function)  # 2
#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = original_function(*args, **kwargs)
#         t2 = time.time() - t1
#         print('{} 함수가 실행된 총 시간: {} 초'.format(original_function.__name__, t2))
#         return result

#     return wrapper


# @my_timer
# @my_logger
# def display_info(name, age):
#     time.sleep(1)
#     print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))


# display_info('Jimmy', 30)  # 3
