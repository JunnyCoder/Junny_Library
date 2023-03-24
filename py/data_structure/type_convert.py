'''
Created by Junho Kim
Last edit : Mar/22/2023
'''
import pandas as pd
from . import list_control as LC


def list_to_df(in_list : list, data_type = str, filling_value = False ):
    '''
    Change list to Pandas dataframe.
    The list should be double linked list.
    If there are more than one types, all datatype will be changed as string as default.
    Default filling Value is None
    '''
    temp = []
    temp = LC.list_length_match(in_list, filling_value)
    preprocessed_list = []
    for i in temp:
        if LC.is_one_data_type(i) == data_type:
            preprocessed_list.append(i)
        else:
            preprocessed_list.append(map(data_type,i))
    result = pd.DataFrame(preprocessed_list)
    return result
