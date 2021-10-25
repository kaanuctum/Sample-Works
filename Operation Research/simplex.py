#the simplex algorithm to find the optimal solution of a linear programm
#its only the primal simplex --> I'm lazy

#getting the objective function
while True:
    OF_coefs = input('input the coefficients of the objective function \nwithout the variables, separeated by a comma: ')

    OF = OF_coefs.split(',')
    try:
        for i in range(len(OF)):
            OF[i] = int(OF[i])
        break
    except:
        print('not a valid input')
#getting the constraints
print('\nenter done or nothing to end inputing constraints \n')
constraints = list()
while True:
    const_coefs = input('enter the coefficients of the constraint,\nseperated by a comma, with the limit as the last coeefficient')
    if const_coefs == 'done' or len(const_coefs)==0:break
    const_coefs = const_coefs.split(',')
    try:
        current_const = list()
        for i in range(len(const_coefs)):
            current_const.append(int(const_coefs[i]))
        constraints.append(current_const)
    except:
        print('not a valid input')



BV = list()
values = list()


#remove the limit from the input
for i in range(len(constraints)):
    values.append(constraints[i][-1])
    constraints[i] = constraints[i][:-1]
values.append(0)



#achieving the conanical form
for i in range(len(constraints)):
    for j in range(len(constraints)):
        if i == j: constraints[j].append(1)
        else: constraints[j].append(0)

for i in range(len(constraints)):
    OF.append(0)
    BV.append(len(OF))
initial_OF = OF.copy()



print('\ninitial tableau form:')

for i in range(len(constraints)):
    print('|{}|{}|{}'.format(BV[i],values[i], constraints[i]))
print('|{}|{}|{}'.format('-Z',values[-1], OF))

x = ''
while True:
    if x != 'cont' : x = input("enter for the next iteration, write 'cont' for the final solution ")

    #check if the algorithm is done
    done = True
    for i in range(len(OF)):
        if OF[i] > 0 : done = False

    if done == True : break


    pivot_col = -1
    for i in range(len(OF)):
        if OF[i] >= 0:
            if pivot_col == -1 : pivot_col = i
            if OF[i] > OF[pivot_col] : pivot_col = i

    pivot_row = -1
    smallest = int()
    for i in range(len(constraints)):
        if constraints[i][pivot_col] > 0:
            if pivot_row == -1 :
                smallest = values[i]/constraints[i][pivot_col]
                pivot_row = i

            if values[i]/constraints[i][pivot_col] < smallest:
                smallest = values[i]/constraints[i][pivot_col]
                pivot_row = i



    #swap the base
    BV[pivot_row] = (pivot_col+1)
    pivot_element = constraints[pivot_row][pivot_col]
    #perform the gausian eliminitaion procces

    #transform the pivot row
    for i in range(len(constraints[pivot_row])):
        constraints[pivot_row][i] *= (1/pivot_element)
    values[pivot_row] *= (1/pivot_element)




    #transform the other rows
    for i in range(len(constraints)):
        if i != pivot_row:
            divisor = constraints[i][pivot_col]
            for j in range(len(constraints[i])):
                constraints[i][j] -= divisor * constraints[pivot_row][j]
            values[i] -= divisor * values[pivot_row]

    #transform the OF
    divisor = OF[pivot_col]
    for i in range(len(OF)):
        OF[i] -= divisor* constraints[pivot_row][i]
    values[-1] -= divisor * values[pivot_row]




    if x != 'cont':
        #print the current tableau
        for i in range(len(constraints)):
            print('|{}|{}|{}'.format(BV[i],values[i], constraints[i]))
        print(values[-1], OF)




for i in range(len(constraints)):
    print('|{}|{}|{}'.format(BV[i],values[i], constraints[i]))
print(values[-1], OF)

for i in range(len(BV)):
    print('X{} = {}'.format(BV[i], values[i]))


z=0
for i in range(len(BV)):
    z  += (values[i]* initial_OF[BV[i]-1])

print('Z = ',z)
