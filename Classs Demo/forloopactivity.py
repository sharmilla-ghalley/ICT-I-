#forloop without use of range
tup=("John Smith", "Jane Doe", "Alice Johnson")
for x in tup:
    print(x)

set1={10,30,20}
for x in set1:
    print(x)

#iterating over dictionary
BookDetails=dict({"oython programming":"John Smith","python fundamentals":"Alice Johnson","Python Interview Quwstions":"Jane Doe"})
for keys in BookDetails:
    print(keys, BookDetails[keys])
