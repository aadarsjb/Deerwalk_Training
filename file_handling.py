# f = open('file.txt', 'w')


# f.write('\n Python is awesome')

# g = open('file.txt', 'r')

# g_output = (g.readlines())
# for line in g_output:
#     print(line.strip())

# closing the file
# g.close()
    
with open('file.txt', 'r') as f:
    print(f.closed)
    print(f.read())

print(f.closed)