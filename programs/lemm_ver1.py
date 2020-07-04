"""
Lemmatizating essay text file
Version 1
Read only Middle 200 ~ 250 words
if total is greater than 200
input => input.txt
output => output_ver1.txt 
"""
input_file = "text-files\input.txt"

def read_input(input_file):
    with open (input_file,"r+", encoding="utf-8") as fin:
        return fin.read()

get_text = read_input(input_file)
#print(get_text)
#print("\n")

get_text = get_text.split(" ")
if len(get_text) > 200:
    start = (len(get_text)-200)//2
    end = len(get_text) - start
    #print(start)
    #print(end)
    middle = get_text[start:end]

else:
    middle = get_text

text_list = middle
#print(text_list)
text = " "
text = text.join(text_list)

with open('text-files\output_ver1.txt', 'w') as f:
    for item in lemm:
        f.write("%s" % item)