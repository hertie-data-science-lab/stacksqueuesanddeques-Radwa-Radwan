from code_file import ArrayDeque

D = ArrayDeque()

for i in range(D.DEFAULT_CAPACITY):
    D.add_last(i)
    print(len(D), D.elements)

for i in range(10):
    D.delete_first()
    print(len(D), D.elements)