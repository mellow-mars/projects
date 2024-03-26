def selection_sort(list):
    for i in range(len(list)-1):  # 리스트의 마지막 자리는 자동으로 정렬되기 때문에
        idx = i  # 첫번째 인덱스에 있는 값과 비교 해야하기 때문에 idx = i
                
        for j in range(i+1, len(list)): # 가장 작은 숫자 찾는 것을 range(i,len(list)) 한 이유가 현재 비교해야하는 인덱스 이후의 숫자만 유의미하기 때문에
            if list[idx] > list[j]:  # 리스트 i 번째에 있는 값이 리스트 뒤에 있는 값보다 작은 인덱스 j값이 있으면 j값을 idx에 저장
                idx = j
        if list[i] != list[idx]:
            list[i], list[idx] = list[idx], list[i] # 만약 두숫자가 같지 않다면 i번째와 가장 작은 숫자인 j번째를 교체

    return list


print(selection_sort([3, 3, 5, 1, 2, 4]))
# print(selection_sort([5, 4, 3, 2, 1, 4]))
# print(selection_sort([2, 2, 1, 2, 2]))
