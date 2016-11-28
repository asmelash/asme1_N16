#7. Write a function that counts the number of vowels 
# (both, lower and upper case) used in a given string

def count_vowels(string):
    """Count the number of vowels given a string as an argument
    """
    count = 0
    for char in string.lower():
        if char in 'aeiou':
            count += 1
    return count

def example():
    #string = 'Sphinx of black quartz, judge my vow'
    #string = 'Asmelash Haftu is a student of Prof Prabhu Ramachandran'
    string = 'pneumonoultramicroscopicsilicovolcanoconiosis'
    #string = 'the quick brown fox jumps over a lazy dog'
    print('The number of vowels in the string is', count_vowels(string))
    

def test_count_vowels():
    assert count_vowels('asdfx') == 1
    assert count_vowels('aeiou') == 5
    assert count_vowels('AEIOU') == 5
    
if __name__ == '__main__':
    test_count_vowels()
    example() 
    #unittest.main()
##########################################################################
