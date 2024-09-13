# Python Program to Remove Punctuation from a String

punctuations="!@#$%^&*()_+};':,. "

string="Khushnood Bilal , . !@#$. How are you"

no_punctuation=""

for char in string :
    if char not in punctuations :
        no_punctuation=no_punctuation + char

print(no_punctuation)