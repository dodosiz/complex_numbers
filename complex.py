import math
import cmath

def polar2rect(ampl, phase):
	phase = math.radians(phase)
	return cmath.rect(ampl, phase)
	
def sum_of_polars(ampl1, phase1, ampl2, phase2):
	number1 = polar2rect(ampl1, phase1)
	number2 = polar2rect(ampl2, phase2)
	sum = number1 + number2
	(sum_ampl, sum_phase) = cmath.polar(sum)
	return (sum_ampl, math.degrees(sum_phase))
	
def help():
	print "COMPLEX NUMBER LIBRARY\n"
	print "polar2rect(amplitude, phase): converts from polar (phase in degrees) to complex number\n"
	print "sum_of_polars(ampl1, phase1, ampl2, phase2): adds two numbers with amplitudes ampl1, ampl2 and phases phase1, phase2\n"
	
