'''
Created by Junho Kim
Last edit : Mar/22/2023
'''
def list_length_match (input_lists : list, filling_val = False):
    '''
    Simply matching the length of lists to the longest one.
    Default is filling empty values with False. 
    The filling values will be appended to the end of the list. 
    '''
    if is_only_list(input_lists):
        print('here')
        input_lists.sort(key=len, reverse=True)
        result_lists = []
        longest_len = len(input_lists[0])
        for temp in input_lists:
            result_lists.append(temp + ([filling_val] * (longest_len - len(temp))))
        return result_lists

    return 'Err' #input Value is not list.


def list_data_check (input_li : list):
    '''
    Check all values in list and return the summary of data type information.
    The return Dictionary's Key is DataType, Value is count of it.
    '''
    dt_type_dic = {}
    for checking_value in input_li:
        if type(checking_value) in dt_type_dic:
            dt_type_dic[type(checking_value)] += 1
        else :
            dt_type_dic[type(checking_value)] = 1
    return dt_type_dic

def is_one_data_type (test_val):
    '''
    Checking Wether Data type is one or not.(Only works with List and Dict type input)
    If there are more than one types, it returns count of types.
    '''
    if isinstance(test_val, dict):
        type_list = list(test_val)
    elif isinstance(test_val, list):
        type_list = list(list_data_check(test_val))
    else:
        return 'Err' #input Value is not list or dict. Err

    if len(type_list) == 1:
        return type_list[0]
    return len(type_list)

def is_only_list(test_val):
    '''
    Check if it is double linked list.
    '''
    if is_one_data_type(test_val) == list:
        return True
    return False
