'''
Created by Junho Kim
Last edit : Mar/29/2023
'''
from functools import wraps
import pandas as pd



# Used for type checking function.
type_dict = {
    str:['str', 'string'],
    list :['list', 'li'],
    int: ['int', 'integer'],
    float : ['float'],
    bool : ['bool', 'boolean'],
    pd.core.frame.DataFrame : ['dataframe', 'df']
    }

def check_type(param_name : str, param_value):
    '''
    To check one argument's data type
    '''
    type_str = param_name.split('_')[0]
    for type_, allowed_name_range in type_dict.items():
        if type_str in allowed_name_range:
            if isinstance(param_value, type_):
                return True
            else:
                return f"ERR_{param_value} is not type{type_}"

def check_type_multiple(param_dict : dict):
    '''
    To check multiple arguments data type 
    '''
    for key, value in param_dict.items():
        print(key,value)
        error_msg = check_type(key, value)
        if error_msg is not True:
            return check_type(key, value)
    return True

def param_check_deco(func):
    '''
    Docstring needed (Working on..)
    잔여 : arg_type_list가 주어지지 않았을 때 체크 없이 가능하게 할 것인가에 대한 고민
    키워드로 주어질 때 방법을 수정해야함. 
    str_a변수를 받아서 a로 만들고 이를 dictionary에 모아 func(**Purified_dict)로 전달해야함.
    '''
    @wraps(func)
    def inner(*args, arg_type_list = None, **kwargs) :
        args_length, kwargs_length = len(args), len(kwargs)
        if arg_type_list is not None and kwargs_length == 0:
            if not isinstance(arg_type_list, list) :
                return 'ERR_arg_type_list should be list type object'
            elif len(arg_type_list) != args_length :
                return 'ERR_Length of arg_type_list and count of arguments are not matched'
            else:
                for arg_type, arg in zip(arg_type_list, args):
                    print(arg_type,type(arg))
                    error_msg = check_type(arg_type, arg)
                    if error_msg is True:
                        continue
                    else:
                        return error_msg
            return func(*args)
        elif arg_type_list is None and args_length == 0 :
            error_msg  = check_type_multiple(kwargs)
            if error_msg is True:
                print('There')                
                return func(**kwargs)
            else:
                return error_msg
        elif args_length != 0 and kwargs_length != 0:
            if not isinstance(arg_type_list, list) :
                return 'ERR_arg_type_list should be list type object'
            elif len(arg_type_list) != args_length :
                return 'ERR_Length of arg_type_list and count of arguments are not matched'
            else:
                for arg_type, arg in zip(arg_type_list, args):
                    error_msg = check_type(arg_type, arg)
                    if error_msg is True:
                        continue
                    else:
                        return error_msg
            if error_msg is True:
                return func(*args, **kwargs)
            else:
                print('here')
                return error_msg
        else :
            return 'ERR'
    return inner


'''
TESTING WORDS
@param_check_deco
def foo(a=1,b=2):
    print(a,b)

foo(a=1,b=1)
foo(str_a=1, str_b='1')
'''

# def param_check_deco(func):
#     @wraps(func)
#     def pc_inner(arg_type, *args, **kwargs):
#         if arg_type is not None :
#             for arg in range(len(args)):
#                 if not isinstance(arg, arg_type):
#                     return f"ERR_{args.index(arg)} is not type{arg_type}"
#             return func(*args)
#         elif arg_type is None :
#             for key, value in kwargs:
#                 if not isinstance(value, key.split("_")[0]):
#                     return f"ERR_{value} is not type{key}"
#             return func(*kwargs)
#     return pc_inner
