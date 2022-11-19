#11/19 수정. A에다가 넣어야할듯?아니지...어떻게하지?
#result에다가 append만 하고 자꾸 A에서만 불러오니까.... 결국 다 초기화돼서 마지막에 A를 반쪼개서 합치는거밖에 안됨...ㅎ.ㅎ
import math
global count
count = 0

#merge_sort(A[p..r]) { # A[p..r]을 오름차순 정렬한다.
def merge_sort(A):
    if len(A) <= 1: #if 0==4
        return A
    else: 
        mid = math.ceil(len(A)/2)
        #print("merge_sort",A,",",start,",",mid,",",end)
        left_array = merge_sort(A[:mid])
        right_array = merge_sort(A[mid:])
        #merge(A,start,mid,end)
        return merge(left_array, right_array)

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.

# A는 list
def merge(left_array, right_array):
    global count #함수 안,밖에다가 2번 선언해야함.
    #이걸 0으로 지정하는 바람에 계속 잘 안됐었음 ㅠㅠ
    result = [] #append로 하지 않으면 마지막에 값을 여러번 출력해야해서ㅠ
    
    left = left_array
    right = right_array 
    i = j = 0
    while (i < len(left) and j < len(right)):
        if (left[i] <= right[j]): #두 부분의 leftmost를 비교해서 작은게 병합될 list 제일 왼쪽으로.
            result.append(left[i])
            count += 1
            if count == inputCount:
                #print("left[i]<=right[j] : ",left[i], ",left: ", left, ",right: ",right,",i: ",i, ",result: ",result)
                print(left[i])
            i += 1
        else:
            result.append(right[j])
            count += 1
            if count == inputCount:
                #print("left[i]>right[j] : ",right[j],",left[i]: ", left[i] , ",left: ", left, ",right: ",right,",j: ", j, ",result: ", result)
                print(right[j])
            j += 1        

    while (i < len(left)):  # 왼쪽 배열 부분이 남은 경우
        result.append(left[i])
        count += 1
        if inputCount == count:
            #print("i < len(left) : ",left[i], ",left: ", left, ",right: ",right, ",i: ", i, ",result: ", result)
            print(left[i])
        i += 1
    while (j < len(right)):  # 오른쪽 배열 부분이 남은 경우
        result.append(right[j])
        count += 1
        if inputCount == count:
            #print("j < len(right) : ",right[j], ",left: ", left, ",right: ",right, ",result: ", result)
            print(right[j])
        j += 1
    
    if len(result) == N and count < inputCount:
        print(-1)
    return result

import sys
N,inputCount = map(int, sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
merge_sort(A)