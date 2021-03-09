# PHSX815_Week5
## Homework MonteCarlo


###Homework 1
To run this you have to run:
python3 myrandom.py -Nsample number


###Homework 2
python3 integrator.py -trapezoidal
This code used lagurre gaussian quatrature to compute the integration. This code has some limitations. This can only integrate properly with in the range of 0 to infinity as I have not performed the change of variable to change the limit.  Hence, we need to use exponentially decaying function e^-x such as ((x^2+2) e^-x). I will be updating this code to run integration on a to b  and any kind of function.
