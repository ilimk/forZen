import difflib

with open('input.txt', 'r') as myfile:
  data1 = myfile.read()

with open('patterns.txt', 'r') as myfile:
  data2 = myfile.read()
print "-------------------------FirstText------------------------------------------"
print data1
print "-------------------------SecondText------------------------------------------"
print data2
print "-------------------------SplitingTexts------------------------------------------"
data11 = data1.split('\n')
data22 = data2.split('\n')
data111 = data1.split(' ')
data222 = data2.split(' ')
print "--------------------------comparisonFileByString----------------------------------"

for i in range(len(data11)):
    for j in range(len(data22)):
        if data11[i] == data22[j]:
            print data11[i]

print "--------------------------comparisonFileByWord----------------------------------"

i = 0
j = 0
for i in range(len(data11)):
    for j in range(len(data22)):
        sequence = difflib.SequenceMatcher(isjunk=None, a=data11[i], b=data22[j])
        difference = sequence.ratio() * 100
        difference = round(difference, 1)
        if difference > 50:
            print data11[i]
























