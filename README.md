- The goal of the project is to implement the Reed Solomon encoding and decoding algorithm.

- The problem is:

	Assume we want to send data through a noisy channel, that we cannot guarantee a 100% recovery of the message, there are many protocols to send it and to have a better change of recovering the original message, one of them is obviously sending the message multiple times, but that will cost us a lot of data usage, and in this Project we will explore the Reed Solomon List Encoding & Decoding algorithm that will have a good chance of recovering the original message without sending too many messages.

- A short explanation of the Reed Solomon List Encoding & Decoding algorithm:

	Decoding: Assume we have ‘n’ pairs of coordinates, were we want to find a polynomial with a degree of ‘k’ that satisfies ‘t’ points of the coordinates, Reed Solomon Decoding algorithm solves this problem by building a bi-variate polynomial with specific traits that will help us to find the requested polynomial.

	Encoding: The encoding process is easy compared to the encoding, we simply take the word we wish to transmit, turn it into a polynomial, s.t:
If we wish to encode the word, we look at each character we haven, <c1,c2,c3..,ck>, and we build a polynomial that the coefficients of each ‘Xi’ are ‘ci’, so we end up with:
c1+(c2*X)+(c3*X^2)...+(ck*X^k), and this is a polynomial with at most K degree.

To further expand knowledge in the Reed Solomon List Encoding & Decoding you can read the article: http://www.cs.cmu.edu/~venkatg/pubs/papers/listdecoding-NOW.pdf

These are some of the experiments, where we have added ‘n’ correct pairs of coordinates that belong to the polynomial and ‘e’ pairs of error coordinates that do not belong, and testing if the polynomial is found through these correct and incorrect coordinates:
