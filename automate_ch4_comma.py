def convert(list):
    output=''
    for i in range(0,len(spam)):
        if i == len(spam)-1:
            output+='and '+spam[-1]
        else:
            output += spam[i] + ', '
    return output

spam =['apples','bananas','tofu','cats','horses']

convert(spam)
