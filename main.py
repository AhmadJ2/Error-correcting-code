# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from sympy import *
import numpy
import random

debug = False
# inputs:
encode = "1234567890abc"
print("Sending: ", encode)
# we sent 16 points, k is 4, error = 2,
# t = n - e -> n = t + e
print('Number of errors that will occur when sending the message:')
error = int(input())


# maximum error: if |field| is 28

def ord2(char):
    if ord(char) - ord('0') > 10:
        return ord(char) - ord('a') + 10
    return ord(char) - ord('0')


def encode_one_letter(word, val):
    start_ = 0
    sum = 0
    for i in range(0, len(word)):
        sum += val ** start_ * ord2(word[i])
        start_ += 1
    return sum


def make_noise(X_arr, Y_arr, num_of_noise):
    num_of_curr_noise = 0
    history = []
    if num_of_noise == 0:
        return
    while true:
        curr = random.randint(0, len(X_arr) - 1)
        if history.count(curr) == 0:
            history.append(curr)
            X_arr[curr] = random.randint(0, 100)
            Y_arr[curr] = random.randint(0, 100)
        if len(history) == num_of_noise:
            break


x_arr = []
y_arr = []
# Change the 28 to change the field size!
for i in range(0, 28):
    y_arr.append(encode_one_letter(encode, i))
    x_arr.append(i)
make_noise(x_arr, y_arr, error)
n = len(x_arr)
k = len(encode) - 1
t = int(sqrt(2 * k * n)) - 3
print('n is: ', n, '\nD is:', t, '\nt is: ', t + 1, '\ne is ', error, '\nk is: ', k)

for i in range(0, list.__len__(x_arr)):
    x_arr[i] = x_arr[i]


def double_sigma_algo1(D, k, X, Y, Z_arr):  # FOR BUILDING THE (1,k) DEGREE POLY
    for x in range(0, list.__len__(x_arr)):  # fix with +1
        for y in range(0, list.__len__(x_arr)):
            if x + k * y <= D:
                list.append(Z_arr, ((pow(X, x)) * (pow(Y, y))))


def double_sigma_algo1_last_step(D, k, co_acc, Z_arr):  # FOR BUILDING THE (1,k) DEGREE POLY WITH FEW ADDITIONS
    i = 0
    for x in range(0, list.__len__(x_arr)):  # fix with +1
        for y in range(0, list.__len__(x_arr)):
            if x + k * y <= D:
                list.append(Z_arr, ((co_acc[i]) * Symbol('x') ** (x) * Symbol('y') ** y))
                i = i + 1


def can_be_poly(poly):  # TESTING IF THE MULTIVARIATE POLYNOMIAL IS IN THE FORM OF (Y-P(X))
    if poly.count(Symbol('y')) != 1:
        return False
    args = poly.args
    found_a_y = False
    for arg in args:
        if arg.count(Symbol('y')) == 1:
            if arg.is_Symbol:
                if arg == (Symbol('y')):
                    found_a_y = True
            if arg.is_Mul:
                arg_ = arg.args
                if arg_[1] == (Symbol('y')) and tuple.__len__(arg_) == 2:
                    found_a_y = True
    return found_a_y


def can_be_poli_div(p):
    # TESTING IF THE MULTIVARIATE POLYNOMIAL IS IN THE FORM OF (Y-P(X)) WITH FEW ADDITIONS FOR THE RETURN VALUE
    args = p.args
    for arg in args:
        if arg.count(Symbol('y')) == 1:
            if arg.is_Symbol:
                if arg == (Symbol('y')):
                    return 1
            if arg.is_Mul:
                arg_ = arg.args
                if arg_[1] == (Symbol('y')) and tuple.__len__(arg_) == 2 and arg_[0].is_Number:
                    return arg_[0]
    return 'null'

#########################################################BUILDING THE Q(X,Y)#######################################################
z_acc = []
z_arr = []
for i in range(0, list.__len__(x_arr)):
    double_sigma_algo1(t, k, x_arr[i], y_arr[i], z_arr)
    list.append(z_acc, z_arr)
    z_arr = []
z_acc = numpy.fliplr(z_acc)
z_acc = numpy.fliplr(z_acc)
z_soof = []
for i in range(0, int(numpy.size(z_acc) / numpy.size(z_acc[0]))):
    row = []
    for j in range(0, numpy.size(z_acc[0])):
        if z_acc[i][j] != 0:
            if numpy.size(row) == 0:
                row = [(z_acc[i][j]) * Symbol('a' + str(j))]
            else:
                row[0] = row[0] + z_acc[i][j] * Symbol('a' + str(j))
    list.append(z_soof, row[0])

#############################################################SOLVING THE Q(X,Y)#######################################################################

# now we have the full linear equation ready to solve,
# just need to prepare some things for the final step of building the polynomial.
poly_coeff = []
solved = solve(z_soof)
for i in range(0, numpy.size(z_acc[0])):
    poly_coeff.append('null')
for i in range(0, numpy.size(z_acc[0])):
    if not solved.keys().__contains__(Symbol('a' + str(i))):
        poly_coeff[i] = 1
while True: # Here we keep replacing each 'solved' unknown to further find new unknowns values, this step will work based on
    # RS codes algorithms, thats why we use 'while True', beware, missing with 'D' values will cause this loop to never end sometimes!
    if list.count(poly_coeff, 'null') == 0:  # all coefficients found
        break
    for i in range(0, numpy.size(z_acc[0])):  # going through the coefficients to try and replace them
        if poly_coeff[i] != 'null':
            for x in range(0, list.__len__(z_soof)):
                z_soof[x] = z_soof[x].replace(Symbol('a' + str(i)), poly_coeff[i])
    solved = solve(z_soof)
    for s in solved:  # going through the equations to see if one of them can be turned into a number!
        if solved[s].is_Number:
            poly_coeff[int(str(s)[1:])] = (solved[s])
ff_arr = []
double_sigma_algo1_last_step(t, k, poly_coeff, ff_arr)
ff_arr_flat = 0
for line in ff_arr:
    ff_arr_flat = ff_arr_flat + line
# testing if the polynomial is legit:
for i in range(0, list.__len__(x_arr)):
    if not int(ff_arr_flat.replace(Symbol('x'), x_arr[i]).replace(Symbol('y'), y_arr[i])) == 0:
        print('oops ', i)
        print((ff_arr_flat.replace(Symbol('x'), x_arr[i]).replace(Symbol('y'), y_arr[i])))

#########################################################################ANALYZING THE OUTPUT########################################################################

print('-------')
f = False

# Here we split the Q(X,Y) into smaller polynomials, we study each one of them and see
# if it is in the form of "Y-P(X)", and see if it agrees with atleast 't' coordinates
# and it is a poly with at most 'k' degree.
if not (ff_arr_flat.__eq__(factor(ff_arr_flat))):
    c = 0
    skip = 0
    for x in factor(ff_arr_flat).args:
        if debug:
            print('DEBUG: one of the poly in the BIG poly is :', x)
        p = can_be_poli_div(x)
        if p != 'null':
            for i in range(0, list.__len__(x_arr)):
                if int(x.replace(Symbol('x'), x_arr[i]).replace(Symbol('y'), y_arr[i])) == 0:
                    c = c + 1
            if c > t:
                if not x.is_Number:
                    x = x.replace(Symbol('y'), 0)
                    x_ = 0 - (x * p)
                    ret = ""
                    count = 0
                    index = 0
                    map = {}
                    while index < len(x_.args):
                        if x_.args[index].is_Number:
                            map[0] = x_.args[index]
                        elif len(x_.args[index].args) == 0:
                            map[1] = x_.args[index].replace(Symbol('x'), 1)
                        elif len(x_.args[index].args[1].args) < 2 and x_.args[index].args[0].is_Number:
                            map[1] = x_.args[index].args[0]
                        elif x_.args[index].args[1].is_Number:
                            map[index] = 1
                        else:
                            map[x_.args[index].args[1].args[1]] = x_.args[index].args[0]
                        index += 1
                    for i in range(0, k + 1):
                        if map.__contains__(i):
                            if map[i] < 10:
                                ret += chr(map[i] + ord('0'))
                            else:
                                ret += chr(map[i] - 10 + ord('a'))
                        else:
                            ret += '0'
                    print("Receiving: ", ret)
                    f = True
                    break
            c = 0
else:
    c = 0
    if can_be_poly(ff_arr_flat):
        for i in range(0, list.__len__(x_arr)):
            if int(ff_arr_flat.replace(Symbol('x'), x_arr[i]).replace(Symbol('y'), y_arr[i])) == 0:
                c = c + 1
        if c > t:
            if not ff_arr_flat.is_Number:
                div = can_be_poli_div(ff_arr_flat)
                x = ff_arr_flat.replace(Symbol('y'), 0)
                x_ = 0 - (x * div)
                print('Found one factor of Q(X,Y) that we can use: ', x_)
if not f:
    print('could not find a polynomial that satisfies both \'k\' and \'t\' restrictions ')
