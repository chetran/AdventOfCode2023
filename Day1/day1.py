import re

# Solution 1
sum = 0 
with open("input.txt", "r") as input:
    for line in input:
        nums = re.findall("\d", line)
        sum += int(nums[0] + nums[-1])

print(sum)
# Solution 2 
nums = {
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7', 
    'eight' : '8',
    'nine' : '9'
}

class matchObj:
    def __init__(self, group, a, b):
        self.group = group
        self.span = (a, b)

def sortWords(arr):
    newList = []
    i = 0 
    j = -1
    for k in range(len(arr)):
        if (arr[i].span[0] > arr[k].span[0]):
            i = k
        if (arr[j].span[0] < arr[k].span[0]):
            j = k
    newList.append(arr[i])
    newList.append(arr[j])
    return newList

sum = 0
with open("input.txt", "r") as input:
    for line in input:
        list_of_words = []
        for num in nums:
            for i in range(0, len(line)):
                if (line[i: i+len(num)] == num):
                    x = matchObj(num, i, i+len(num))
                    list_of_words.append(x)
        numbers = re.findall("\d", line)
        if list_of_words and numbers:
            list_of_words = sortWords(list_of_words)
            index_num1 = line.index(numbers[0]) # index of the first number
            index_num2 = len(line) -  line[::-1].index(numbers[-1]) - 1 # index of the second number 
            # Deciding if i should use the number or the word by comparing the index of the number and the span of the word
            a = nums.get(list_of_words[0].group) if (list_of_words[0].span[0] < index_num1) else line[index_num1] # che
            b = nums.get(list_of_words[-1].group) if (list_of_words[-1].span[0] > index_num2) else line[index_num2]
            sum += int(a+b)
        elif (numbers):
            sum += int(numbers[0] + numbers[-1])
        elif (list_of_words):
            list_of_words = sortWords(list_of_words)
            sum += int(nums.get(list_of_words[0].group()) + nums.get(list_of_words[-1].group()))

print(sum) 