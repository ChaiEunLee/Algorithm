
my_set = set([])

for i in range(10):
    a = int(input())
    nums = a%42
    my_set.add(nums) #set은 unordered. append 대신 add.
print(len(my_set))