import time
inputs =[
'1,1,9',
'1,3,4',
'1,8,6',
'2,2,7',
'3,2,5',
'3,5,7',
'3,8,4',
'4,1,6',
'4,3,5',
'4,5,4',
'4,8,9',
'5,3,8',
'5,8,3',
'6,2,3',
'6,4,7',
'6,5,9',
'7,2,4',
'7,5,1',
'7,6,8',
'7,7,6',
'7,9,3',
'9,2,6',
'9,4,9',
'9,6,5',
'9,8,8',
'9,9,1',
]





class Point:
    def __init__(self,y,x):
        y = int(y)
        x = int(x)
        self.y = int(y)
        self.x = int(x)
        self.box = None
        if 0<=x<=2 and 0<=y<=2: self.box = 0
        if 3<=x<=5 and 0<=y<=2: self.box = 1
        if 6<=x<=8 and 0<=y<=2: self.box = 2
        if 0<=x<=2 and 3<=y<=5: self.box = 3
        if 3<=x<=5 and 3<=y<=5: self.box = 4
        if 6<=x<=8 and 3<=y<=5: self.box = 5
        if 0<=x<=2 and 6<=y<=8: self.box = 6
        if 3<=x<=5 and 6<=y<=8: self.box = 7
        if 6<=x<=8 and 6<=y<=8: self.box = 8

        self.possible = [1,2,3,4,5,6,7,8,9]
        self.actual = 0

    def remove_pos(self, integer):
        self.possible.remove(integer)



def set_certain(y,x,integer):
    points[y*9 + x].actual = int(integer)
    points[y*9 + x].possible = [int(integer)]



def check_done():
    done = True
    for i in points:
        if i.actual == 0: done = False
    return done




def print_grid():
    for i in grid:
        print(i[0].actual, i[1].actual, i[2].actual, i[3].actual, i[4].actual, i[5].actual, i[6].actual, i[7].actual, i[8].actual)

def print_list():
    for i in range(9):
        print((points[i*9+0].actual, points[i*9+1].actual, points[i*9+2].actual, points[i*9+3].actual, points[i*9+4].actual, points[i*9+5].actual, points[i*9+6].actual, points[i*9+7].actual, points[i*9+8].actual))


def check_certain():
    for p1 in points:
        for p2 in points:
            if p1.actual != 0 and p2.actual != 0:
                continue
            if p1.actual == 0 and p2.actual == 0:
                continue
            else:
                try:
                    if p1.box == p2.box :
                        if p1.actual != 0: p2.remove_pos(p1.actual)
                        if p2.actual != 0: p1.remove_pos(p2.actual)
                    if p1.x == p2.x:
                        if p1.actual != 0: p2.remove_pos(p1.actual)
                        if p2.actual != 0: p1.remove_pos(p2.actual)
                    elif p1.y == p2.y:
                        if p1.actual != 0: p2.remove_pos(p1.actual)
                        if p2.actual != 0: p1.remove_pos(p2.actual)

                except: continue



def check_box():
    all_numbers = [1,2,3,4,5,6,7,8,9]
    for box_n in range(9):
        box = list()
        box_remaining = all_numbers.copy()

        for point in points:
            if point.box == box_n: box.append(point)
        for point in box:
            if point.actual == 0:continue
            else:box_remaining.remove(point.actual)
            point_prev = point
        count_of_numbers = dict()
        for point in box:
            for number in point.possible:
                count_of_numbers[number]=count_of_numbers.get(number,0)+1
        for number in all_numbers:
            if count_of_numbers.get(number,0)==1:
                for point in box:
                    if point.possible.count(number) == 1: set_certain(point.y,point.x,number)

def check_row():
    all_numbers = [1,2,3,4,5,6,7,8,9]
    for row_n in range(9):
        row = list()
        row_remaining = all_numbers.copy()

        for point in points:
            if point.y == row_n: row.append(point)
        for point in row:
            if point.actual == 0:continue
            else:row_remaining.remove(point.actual)
            point_prev = point
        count_of_numbers = dict()
        for point in row:
            for number in point.possible:
                count_of_numbers[number]=count_of_numbers.get(number,0)+1
        for number in all_numbers:
            if count_of_numbers.get(number,0)==1:
                for point in row:
                    if point.possible.count(number) == 1: set_certain(point.y,point.x,number)


def check_collom():
    all_numbers = [1,2,3,4,5,6,7,8,9]
    for collom_n in range(9):
        collom = list()
        collom_remaining = all_numbers.copy()

        for point in points:
            if point.x == collom_n: collom.append(point)
        for point in collom:
            if point.actual == 0:continue
            else:collom_remaining.remove(point.actual)
            point_prev = point
        count_of_numbers = dict()
        for point in collom:
            for number in point.possible:
                count_of_numbers[number]=count_of_numbers.get(number,0)+1
        for number in all_numbers:
            if count_of_numbers.get(number,0)==1:
                for point in collom:
                    if point.possible.count(number) == 1: set_certain(point.y,point.x,number)






def print_used_number():
    numbers = dict()
    for point in points:
        numbers[point.actual]=numbers.get(point.actual,0)+1
    for i in range(9):
        j=i+1
        print(numbers[j])






def make_final():
    for point in points:
        if len(point.possible) == 1:
            set_certain(point.y, point.x, point.possible[0])

def starting_validity_check():
    valid = True
    for p1 in points:
        for p2 in points:
            if p1 == p2: continue
            if p1.actual == 0 or p2.actual == 0: continue
            if p1.x == p2.x     and p1.actual == p2.actual: valid = False
            if p1.y == p2.y     and p1.actual == p2.actual: valid = False
            if p1.box == p2.box and p1.actual == p2.actual: valid = False
    return valid




def validity_check():
    valid = True
    for p1 in points:
        for p2 in points:
            if p1 == p2: continue
            if p1.x == p2.x     and p1.actual == p2.actual: valid = False
            if p1.y == p2.y     and p1.actual == p2.actual: valid = False
            if p1.box == p2.box and p1.actual == p2.actual: valid = False
    return valid

def check_progress():
    total = 81
    tot = 0
    for p in points:
        if p.actual == 0: tot +=1
    percentage = ((total-tot)/total)*100
    return percentage


#create an empty sudoku grid
grid = list()
points = list()
for y in range(9):
    row = list()
    for x in range(9):
       row.append(Point(y, x))
       points.append(Point(y, x))
    grid.append(row)



for inp in inputs:
#while True:
#    inp = input('enter the y, x, and integer: ')
#    if len(inp) == 0 or inp =='done': break
    y,x,integer = inp.split(',')
    y = int(y) -1
    x = int(x)-1
    set_certain(int(y),int(x),int(integer))
print_list()
print('Starting validity check: ',starting_validity_check())
print('Starting at {} percentage completion'.format(check_progress()))
guesses = 0
multiple_solutions = False
print('\n')
iteration = 0
beg_time = time.time()
while check_done() == False:
    print(iteration, check_progress())
    iteration +=1
#    disposible = input()
    if iteration ==1001:
        print('Prev')
        print_list()
        print('Time elapsed for {} iteration'.format(iteration), time.time()-beg_time)
        print('Time per iteration in ms: ',(time.time()-beg_time)/iteration*1000)
        print('Current validity of the board: ',starting_validity_check() )
        print('Currently at {} percentage completion'.format(check_progress()))
        print('\n')
    if iteration >15:
        check_box()
        check_row()
        check_collom()
    if iteration > 1000 and iteration % 500 == 0 :
        print_list()
        print('time elapsed for {} iteration'.format(iteration), time.time()-beg_time)
        print('time per iteration in ms: ',(time.time()-beg_time)/iteration*1000)
        print('current validity of the board: ',starting_validity_check() )
        print('currently at {} percentage completion'.format(check_progress()))
        print('\n')
#    if iteration > 30 and (iteration -20) % 10 == 0 :
#        guesses += 1
#        save_points = points.copy()
#        save_iter = iteration
#        for point in points:
#            if len(point.possible) == 2:
#                other_option = point.possible[1]
#                set_certain(point.y,point.x,point.possible[0])
#                while check_done() == False and starting_validity_check() == True :
#                     iteration +=1
#                     check_box()
#                     check_row()
#                     check_collom()
#                     check_certain()
#                     make_final()
#                if starting_validity_check() == False:
#                    points = save_points.copy()
#                    iteration = save_iter + 1
#                    set_certain(point.y,point.x,other_option)
#                if starting_validity_check() == True:
#                    multiple_solutions = True
#                break
#
    check_certain()
    make_final()
print_list()
print('multiple solutions: ',multiple_solutions)
print('guesses: ',guesses)
print('time elapsed for {} iteration'.format(iteration), time.time()-beg_time)
print('time per iteration in ms: ',(time.time()-beg_time)/iteration*1000)
print('current validity of the board: ',validity_check() )
