# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from sympy import *
import numpy
import random

x_arr = []
y_arr = []
# The polynomial we are trying to find is "P(x) = x^2 - x + 3", so we add 10 x and y coordinates
for i in range (0,16):
    x_arr.append(i)
    y_arr.append(i**4 - 3*i**3 -7*i**2 + i + 1)
# We add 5 more pairs of "errors" to see if the code still finds the original polynomial
for i in range (0,14):
    x_arr.append(random.randint(0, 100))
    y_arr.append(random.randint(0, 100))

k = 4
n = list.__len__(x_arr)
D = int(sqrt(2 * k * n))
print('n is: ', n, '\nD is: ', D)

for i in range(0,list.__len__(x_arr)):
    x_arr[i] = x_arr[i]
def double_sigma_algo1(D, k, X, Y, Z_arr):
    for x in range(0, list.__len__(x_arr)):  # fix with +1
        for y in range(0, list.__len__(x_arr)):
            if x + k * y <= D:
                list.append(Z_arr, ((pow(X, x)) * (pow(Y, y))))


def double_sigma_algo1_last_step(D, k, co_acc, Z_arr):
    i = 0
    for x in range(0, list.__len__(x_arr)):  # fix with +1
        for y in range(0, list.__len__(x_arr)):
            if x + k * y <= D:
                list.append(Z_arr, ((co_acc[i]) * Symbol('x') ** (x) * Symbol('y') ** y))
                i = i + 1


def can_be_poly(poly):
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



z_acc = []
z_arr = []
for i in range(0, list.__len__(x_arr)):
    double_sigma_algo1(D, k, x_arr[i], y_arr[i], z_arr)
    list.append(z_acc, z_arr)
    z_arr = []
z_acc = numpy.fliplr(z_acc)
z_acc = numpy.fliplr(z_acc)
# print(pol_array)
#print(z_acc)
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
# now we have the full linear equation ready to solve,
# just need to prepare some things for the final step of building the polynomial.
poly_coeff = []
# print('zsoof is ', z_soof)
solved = solve(z_soof)
# print(solved)
# print('solved is', solved)
for i in range(0, numpy.size(z_acc[0])):
    poly_coeff.append('null')
for i in range(0, numpy.size(z_acc[0])):
    if not solved.keys().__contains__(Symbol('a' + str(i))):
        poly_coeff[i] = 1
while True:
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
double_sigma_algo1_last_step(D, k, poly_coeff, ff_arr)
# print(ff_arr)
ff_arr_flat = 0
for line in ff_arr:
    ff_arr_flat = ff_arr_flat + line
# testing if the polynomial is legit:
for i in range(0, list.__len__(x_arr)):
    if not int(ff_arr_flat.replace(Symbol('x'), x_arr[i] ).replace(Symbol('y'), y_arr[i] ))  == 0:
        print('oops ', i)
        print((ff_arr_flat.replace(Symbol('x'), x_arr[i] ).replace(Symbol('y'), y_arr[i] )) )
print('-------')
if not (ff_arr_flat.__eq__(factor(ff_arr_flat))):
    # print('Q_(X,Y): ', ff_arr_flat)
    # print('Q(X,Y): ', factor(ff_arr_flat))
    c = 0
    for x in factor(ff_arr_flat).args:
        if (can_be_poly(x)):
            # print(x.count(Symbol('y')))
            p = can_be_poli_div(x)
            for i in range(0, list.__len__(x_arr)):
                if int(x.replace(Symbol('x'), x_arr[i] ).replace(Symbol('y'), y_arr[i] ))  == 0:
                    c = c + 1
            if c > D:
                if not x.is_Number:
                    x = x.replace(Symbol('y'), 0)
                    x_ = 0 - (x * p)
                    print('Found one factor of Q(X,Y) that we can use:\n    ', x_)
            c = 0
else:
    # print('Q_(X,Y): ', ff_arr_flat)
    # print('Q_(X,Y): ', factor(ff_arr_flat))
    c = 0
    if can_be_poly(ff_arr_flat):
        for i in range(0, list.__len__(x_arr)):
            if int(ff_arr_flat.replace(Symbol('x'), x_arr[i] ).replace(Symbol('y'), y_arr[i] ))  == 0:
                c = c + 1
                print('calculate')
        if c > D:
            if not ff_arr_flat.is_Number:
                div = can_be_poli_div(ff_arr_flat)
                x = ff_arr_flat.replace(Symbol('y'), 0)
                x_ = 0 - (x * div)
                print('Found one factor of Q(X,Y) that we can use: ', x_)
# This is the summary of the entire work, including the algorithms used and future plans

# 1) First we take the input points as x_arr and y_arr
# 2) Build the (1,k) degree polynomial with at most D (1,k) degree, we do that by building equations
# so such Q(X,Y) is not only (1,k) D degree, and also fits the points we have,
# if we choose D big enough ( That's what she said ), we are guaranteed to have an answer
# 3) now with the answers we have, we simply need to find final answers since for example,
# in the returned array of sympy.solve we have (a1: a2 + a3), a2 and a3 are free variables
# and for that we replace them with 1 and now a1 = 2
# 4) With the final answers in our hands, now we have Q(X,Y) and need to factorize it, using sympy
# we can do so and recieve P1(X), P2(X)... Pn(X)
# 5.1) We find the Pi(X) with degree K (not implemented, TODO: IMPLEMENT THIS)
# 5.2) We find the Pi(X) such that the polynomial is "(y - pi(x))" and return 'pi(x)'
# 6?) I'm not sure if I need to find a polynomial with at most K degree or exactly K, so we might
# need to look at all the polynomials combinations to see which one to take

# This is a summary of April month, I've been busy but thankfully I managed to work on it.

# Summary of the current code:
# So far the code seems to work fine, I've added the (F)n Field calculating so now
# numbers wont go as big as they used to be, and we get additional polynomials, for now sometimes I have to make
# D = D - 1

# Need to know if we should take the D or the t as an initial parameter, so far I've not done the encoding
# though it should not be a hard job since most of the work is on the decoding

# I need more tests, as you see up in x_arr and y_arr I've tested multiple polynomials suck (X^2-4) (X^3)
# and few more, they worked fine.

# Casting to 'int' in some places is dangerous, I still have not fully migrated the N field to (F)n over finite n
# I need to know if (1/2) is considered 1 or 0 in (F)3 for example, and if so, is managing fractions as easy as
# managing natural numbers? meaning can I just round it down or up and call the day off?

# So far I'm doing great in this project, I need to make sure all parameters are rounded correctly,
# and not to forget, test, test, test!

# I'm planning to simulate a faulty channel that will take message m and turn into m' with one (or more) errors
# and see if I can find the error, no promises thought since I have exams soon and this seems like a hard job.
