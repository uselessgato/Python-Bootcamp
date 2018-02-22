spam =['apples','bananas','tofu','cats','horses']

output=''
for i in range(0,len(spam)):
    if i == len(spam)-1:
        output += 'and '+spam[-1]
    else:
        output += spam[i]+', '

print(output)
