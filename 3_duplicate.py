def new_list(str):
    new_lists = []
    [new_lists.append(x) for x in str if x not in new_lists]
    return new_lists

str ="It is program about remove duplicate word and print new str with has not duplicate word "
str =' '.join(new_list(str.split()))
print(str)