def insert_sort(list):
    length=len(list)
    for i in range(1,length):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
list=[1,3,5,8,2]

print(insert_sort(list))

#array = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]
array =[3,2,1]
# insert_sort
for i in range(1, len(array)):
    if array[i - 1] > array[i]:
        temp = array[i]     # 当前需要排序的元素12345
        #123fghfgh
        index = i           # 用来记录排序元素需要插入的位置dsdsddsds
        while index > 0 and array[index - 1] > temp:
            array[index] = array[index - 1]     # 把已经排序好的元素后移一位，留下需要插入的位置
            index -= 1
        array[index] = temp # 把需要排序的元素，插入到指定位置ddsdsddssdd
        print (array)
# print sort result.
print(array)

def bubble_sort(list):
    length=len(list)
    for i in range(length-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list

def bubbleSort(nums):
    for i in range(len(nums)-1): # 这个循环负责设置冒泡排序进行的次数
        print("#")
        for j in range(len(nums)-i-1):  # ｊ为列表下标
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                print(nums)
    return nums

print(bubble_sort(list))
print(bubbleSort([8,2,1]))

for i in range(1):
    print (i)
