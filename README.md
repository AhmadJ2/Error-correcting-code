Required libraries:
 numpy
 random
 sympy

------------------------------------------------------------------------------------------------------------------------------------------------------------

The goal of the project is to implement the Reed Solomon encoding and decoding algorithm
The problem definition is : (explain about ECC abit and bring an example)
Solutions (Count the lazy approach, sending the message N times, others are like Reed Solomon)
Explain abit about how reed solomon works (Encode a word to polynomial, send N pairs (of X and P(X)) ;(a,b). and to decode them we have implemented the Reed Solomon decode...explain how)
Experiments: Testing limits of the grade of the polynomials (we try big numbers), the amount of "error", and the length of the polynomial
Conclusion: ...
note : n is not the sum of points, but the correct coordinations

1- P(x) = (x + 1):
	n = 3
	e = 1
	PICTURE OF THE OUTPUT:

2 - P(x) = (x^2):
	n = 7
	e = 2
	


3- P(x) = (x^2 - 3)
	n = 7
	e = 3


4- P(x) = (x^3 - x^2 + x)
	n = 10
	e = 3


5- P(x) = (x^4 - 3x^3 -7x^2 + x + 1)
	n = 15
	e = 6


Run the algo on 5 trials, with 5 polynomials:
	(x + 1)
	(x^2)
	(x^2 - 3)
	(x^3 - x^2 + x)
	(x^4 - 3x^3 -7x^2 + x + 1)
Test them with different error coordinations
Print the result

--------------------------------------------
Explain about the code a bit:
Steps:
Step 1) We have two arrays of coordinates (X_arr and Y_arr), we need to find a polynomial with degree 'K' that will satisfy 'D' points of coordinates
Step 2) We build a (1,k)-weighted degree polynomial that satisfies 'D' points, we do this by solving the linear system
Step 3) We have the solution for the equation, we simply plug the values of the free variables to find all the coeffecient of the polynom
Step 4) We factorize the polynom Q(X,Y) we built, and find which of the polynomials we found is polynomial with degree K
Step 5 .... not done) we plug the coordinates and see if the polynomial satisfies atleast 't', if yes, return the polynomial




--------------------------------------------------------And now the decoding is done------------------------------------------------
