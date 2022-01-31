#count words
str = " hello world"
def count_words(str):
    words = len( str.split())
    return words
w = count_words(str)
print("number of words : ",w)

#count digits
string = "python3 programing 123"
def count_digits(string):
    count=0
    for i in string:
        if i.isdigit():
            count +=1
    return count
d = count_digits(string)
print("number of digits : ",d)

#count sentences
para ="""dywed.
u7ty7iyid.
yutu,ydw.uuwu.ygyws.
jywiud."""
def count_sentence(para):
    s = para.count('.')
    return s
c = count_sentence(para)
print("number of sentence : ",c)

#pytest
def test_count_words():
    assert count_words(str)==2

def test_count_digits():
    assert count_digits(string)==4

def test_count_sentence():
    assert count_sentence(para)==6
