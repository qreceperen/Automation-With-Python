''' Say you have a list value like spam = ['apple', 'banana','tofu','cats' ] 
1. write a function
2.return strings separated by comma and space, with and before last item
For example 'apple, bananas, tofu, and cats' 
3.Function should be able to work with any list value.'''

def ListtoString(a_list):
    if len(a_list)>=2:
        combineUntilLast = ' '.join(a_list[:-1])
        return f'{combineUntilLast} and {a_list[-1]}'
    else:
        str = ''.join(a_list)
        return f'{str}'


spam = ['apple'] # What if list is less than 2 or 1 or empty.
print(ListtoString(spam))

