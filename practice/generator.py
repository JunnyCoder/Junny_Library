test_list=[1,2,3]

def test_gen(num_list):
    for i in num_list:
        yield i + 5

my_test = test_gen(test_list)
# for i in my_test:
#     test_list[0] = i
#     print(test_list)
print(next(my_test),next(my_test),next(my_test))


# from __future__ import division
# import os
# import psutil
# import random
# import time

# names = ['최용호', '지길정', '진영욱', '김세훈', '오세훈', '김민우']
# majors = ['컴퓨터 공학', '국문학', '영문학', '수학', '정치']

# process = psutil.Process(os.getpid())
# mem_before = process.memory_info().rss / 1024 / 1024


# def people_list(num_people):
#     result = []
#     for i in range(num_people):
#         person = {
#             'id': i,
#             'name': random.choice(names),
#             'major': random.choice(majors)
#         }
#         result.append(person)
#     return result


# def people_generator(num_people):
#     for i in range(num_people):
#         person = {
#             'id': i,
#             'name': random.choice(names),
#             'major': random.choice(majors)
#         }
#         yield person

# t1 = time.time()

# people = people_generator(1000000)  # 1 people_generator를 호출


# # 제너레이터를 사용하여 for loop 실행
# for p in people:
#     print(p)
    
# t2 = time.time()
# mem_after = process.memory_info().rss / 1024 / 1024
# total_time = t2 - t1

# print('시작 전 메모리 사용량: {.f} MB'.format(mem_before))
# print('종료 후 메모리 사용량: {.f} MB'.format(mem_after))
# print('총 소요된 시간: {:.6f} 초'.format(total_time))