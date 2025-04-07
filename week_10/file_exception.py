"""
print the story, only to the user
count the number of words in the story 

1) Make two files cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs 
in the second file. Write a program that tries to read these files and print the contents of the file to the screen. 
Wrap your code in a try-except block to catch the FileNotFoundError, and print a friendly message if a file is missing. 
Move one of the files to a different location on your system, and make sure that the code in the except block executes 
properly. 

2) Modify your previous code to fail silently if either file is missing 

3) One common problem when prompting for numerical input occurs when providing text instead of numbers. 
In such a case, when trying to convert the input to int, a ValueError occurs. Write a program that prompts 
the user for two numbers, add them together and print the result. Catch the ValueError if either input value 
is not a number, and print a friendly error message. Test your program by entering two number and then by entering 
some text instead of a number
"""

file_name = "week_10/book.txt"
output_file = open(file_name, "r+", encoding="utf-8")
lst = output_file.readlines()

word_count = 0
word_dict = {}
for line in lst:
    for word in line.split():
        word = word.lower()
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

for item in lst:
    line = item.rstrip().split()
    word_count += len(line)

#sort by appearance
for word in word_dict.keys():
    for key in word_dict:
        for key2 in word_dict:
            if word_dict[key] > word_dict[key2]:
                word_dict[key], word_dict[key2] = word_dict[key2], word_dict[key]

print(f"Word count: {word_count}")
print(word_dict)