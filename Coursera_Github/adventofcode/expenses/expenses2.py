with open('input', 'r') as a_file:
    array = []
    for line in a_file:
        array.append(int(line))

print(len(array))
#print(array)
i = 0
j = 0
k = 0
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
        for z in array:
            if k == len(array):
                k = 0
            operationcounter += 1
            #print(j)
            #print(i)
            #print(array[i])
            #print(array[j])
            if (array[i] + array[j] + array[k]) == 2020:
                print("Los arrays que sumaban 2020 son")
                print(array[i])
                print(array[j])
                print(array[k])
                print("Indexes i:", i, "j:", j, "k:", k)
                resultado = array[i] * array[j] * array[k]
                print("El resultado de la multiplicacion es", resultado)
                print("La cantidad de veces que se comprobo la suma es ", operationcounter)
                break
            k += 1
        j += 1
    i += 1
