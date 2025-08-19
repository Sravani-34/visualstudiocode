'''Write a Python program that takes a sentence as input from the user and performs the following operations:
Convert the sentence to uppercase.
Convert the sentence to lowercase.
Count the number of words in the sentence.
Reverse the sentence.'''
sentence=input("Enter a word:")
print("Convert a sentence to uppercase:"+sentence.upper())
print("Convert the sentence to lowercase:"+sentence.lower())
print(f"Count the number of words in the sentence",len(sentence))
print("Reverse the sentence."+sentence[::-1])

