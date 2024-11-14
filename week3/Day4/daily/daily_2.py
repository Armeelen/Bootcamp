word=input(str("Please write a word:"))
result=[]
for char in word: 
    if not result or char != word[-1]:
        result.append(char)
new_string = "".join(result)
print(new_string)