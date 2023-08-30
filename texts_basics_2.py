"""Task 1
Create a variable called text to store the data: Berlin is a world city of culture, politics, media and science. . 
Your task is to print the length of the text variable on the screen.
"""

# text = "Berlin is a world city of culture, politics, media and science."

# print(len(text))


"""Task 2

Reuse the variable called text and print the first and the last characters on the screen.
"""

# text = "Berlin is a world city of culture, politics, media and science."


# print(text[0], text[62])


"""Task 3

Reuse the variable called text and print the first three characters in upper case.
"""

# text = "Berlin is a world city of culture, politics, media and science."

# upper_three = text[:3]

# print('First three characters:',upper_three.upper())

# print('First three characters:',text[:3].upper())


"""Task 4

Create the variable called text with the following content:  
Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, 
Brandenburg's capital , then count how many times the letter B  appears in the text.
"""

# text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

# print('B appears:',text.count('B'),"times")


"""Task 5

Create a variable called text to store the data: Berlin straddles the banks of the Spree, 
which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau. . 
Your task is to print the last 10 characters of the text variable on screen.
"""

# text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."

# print(text[-10:])

"""Task 6

Create a variable called text to store the data: ---Python programming--- .
Your task is to remove the hyphen (-) character from the string.

"""

# text = "---Python programming---"

# print(text.replace('-',''))

# new_text= ''.join([char for char in text if char != "-"])
# print(new_text)

# new_text= ""
# for char in text:
#     if char != "-":
#         text += new_text

# print(text)

"""Task 7

Create two variables to store your first and your last name. 
Your task is to concatenate the two variables using the appropriate labels.
"""

firstName = "SangDoo"

lastName = "Nam"

print(f"Firstname: {firstName}\nLastname: {lastName}")


