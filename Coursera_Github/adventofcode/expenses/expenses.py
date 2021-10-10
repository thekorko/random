with open('input', 'r') as a_file:
    array = []
    for line in a_file:
        array.append(int(line))

print(len(array))
print(array)
i = 0
j = 0
resultado = 0
operationcounter = 0
#while ((array[i]+array[j] != 2020) or ((i or j) != 200)
print(array[1])
for x in array:
    if i == len(array):
        print("errror")
        break
    for y in array:
        if j == len(array):
            j = 0
        operationcounter += 1
        #print(j)
        #print(i)
        #print(array[i])
        #print(array[j])
        if (array[i] + array[j]) == 2020:
            print("Los arrays que sumaban 2020 son")
            print(array[i])
            print(array[j])
            print("Indexes i:", i, "j:", j)
            resultado = array[i] * array[j]
            print("El resultado de la multiplicacion es",resultado)
            print("La cantidad de veces que se comprobo la suma es ", operationcounter)
            break
        j += 1
    i += 1
