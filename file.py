# Write Read Create files

fo = open('text.txt', 'w')

# File Information
print('Name',fo.name)
print('Is closed?', fo.closed)
print('Opening mode', fo.mode)

# Write into a file
fo.write('I love python')
fo.write(', javascript')
fo.close()

# Add to file.txt
fo = open('text.txt', 'a')
fo.write(' and I guess php')
fo.close()

# Create File
fo = open('text2.txt', 'w+')
fo.write('This is a new file')
fo.close()

# Read File
fo = open('text.txt', 'r+')
text = fo.read()
print(text)
fo.close()