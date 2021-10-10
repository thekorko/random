with open('input', 'r') as a_file:
    array = []
    for line in a_file:
        array.append(str(line))

#print(array)
#print(array)
i = 0
j = 0
k = 0
min = 0
max = 0
valid = 0
policy = ''
list_of_my_line = []
count = 0
list_of_valid = []
list_of_invalid = []
password = []
min_is_found = False
max_is_found = False
number_concat = ''
for line in array:
    currently = line

    #print(line)
    list_of_my_line = list(str(line))
    #min = int(list_of_my_line[0])
    #max = int(list_of_my_line[2])
    #policy = str(list_of_my_line[4])
    #while True:
    #    list_of_my_line.pop(i)
    #    i += 1
    #    if i == 7:
    #        i = 0
    #        break
    for caracter in list_of_my_line:
        if caracter == ('-'):
            print(number_concat,"HOLA1")
            list_of_my_line.pop(i)
            min = int(number_concat)
            number_concat = ''
            #min_is_found = True
        elif caracter == ':':
            print(number_concat,"HOLA2")
            max = int(number_concat)
            number_concat = ''
            list_of_my_line.pop(i)
            i += i
            list_of_my_line.pop(i)
            i += i
            break
        elif caracter.isdigit():
            number_concat += caracter
            #print(caracter)
            #print(list_of_my_line)
            list_of_my_line.pop(i)
        elif caracter.isalpha():
            policy = caracter
            list_of_my_line.pop(i)
        else:
            list_of_my_line.pop(i)
    #print(min, "-", max, "Line ", str(line), "Policy ", policy)
    for caracter in list_of_my_line:
        if caracter == policy:
            count += 1
    if (count < min) or (count > max):
        print("password", print(currently), "is not valid the line is:", j, "policy min-max:", min, "-", max, "letter:", policy)
        list_of_invalid.append((currently, j))
    else:
        print("password", print(currently), "is valid the line is:", j, "policy min-max:", min, "-", max, "letter:", policy)
        list_of_valid.append((currently, j))
        valid += 1
    count = 0
    j += 1
print(list_of_valid)
print(valid)
#print(list_of_invalid)
