
def length_Calculator(text):

    count = 0

    for char in text:
        count +=1

    return count

text = input("enter a word: ")

length = length_Calculator(text)

print(length)


