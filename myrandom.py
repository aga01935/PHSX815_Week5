import numpy as np
import sys
import matplotlib.pyplot as plt

sys.path.append(".")
from python.Random import Random

#global variables
bin_width = 0.
Xmin = -0.
Xmax = 3.14
random = Random()

# Normal distribution with mean zero and sigma = 1
# Note: multiply by bin width to match histogram
def Our(x):
	return np.sin(x)*np.sin(x)

def plotour(x,bin_width):
	return bin_width*Our(x)


# flat distribution with exponential tail on both side
def ourflat(x):
	curve =0.
	if x<0.8:
		curve = np.exp(-0.8)* np.exp(x)
	elif x>2.2:
		curve = np.exp(2.2)* np.exp(-x)
	else:
		curve = 1.

	return curve
#function to generate the tail
def sampleourflat():
	flat = 3.14 - 3.14 * random.rand()
	#print (flat, abs(np.log(random.rand())))
	curve = flat
	#while curve>3.14 or curve < 0.:
	if  flat<0.8:
		while (curve>0.8 or curve < 0.):

			curve = 0.8-abs(np.log(random.rand()))*0.8
			#print ("this is wrong low",curve)

		#print ("curve is ",curve)
			#print ("this should be less than 0.8 and greater than 0..but ", curve)

	elif flat > 2.2:
		#print ("second curve is  ", curve)
		while (curve>3.14 or curve<2.2):

			curve = 3.14 -abs(np.log(random.rand()))*3.14
			#print ("this is wrong",curve)

		#print ("second curve is  ", curve)
	return curve



def plotourflat(x, bin_width):
	return bin_width*ourflat(x)




#main function
if __name__ == "__main__":


	# default number of samples
	Nsample = 100

	doLog = False
	doExpo = False

	# read the user-provided seed from the command line (if there)
	#figure out if you have to have -- flags before - flags or not
	if '-Nsample' in sys.argv:
		p = sys.argv.index('-Nsample')
		Nsample = int(sys.argv[p+1])

		doLog = bool(sys.argv[p])
	if '-h' in sys.argv or '--help' in sys.argv:
		print ("Usage: %s [-Nsample] number" % sys.argv[0])
		print
		sys.exit(1)


	data = []
	Ntrial = 0.
	i = 0.
	while i < Nsample:
		Ntrial += 1
		#print (Ntrial , Nsample)

		X = sampleourflat()
		R = Our(X)/ourflat(X)#Gaus(X)/Flat(X)
		rand = random.rand()
		if(rand > R): #reject if outside
			#print ("should be rejected")
			continue
		else: #accept if inside
			data.append(X)
			i += 1 #increase i and continue

	if Ntrial > 0:
		print("Efficiency was",float(Nsample)/float(Ntrial))


	#normalize data for probability distribution
	weights = np.ones_like(data) / len(data)
	n = plt.hist(data,weights=weights,alpha=0.3,label="samples from f(x)",bins=100)
	plt.ylabel("Probability / bin")
	plt.xlabel("x")

	bin_width = (Xmax-Xmin)/100#n[1][1] - n[1][0]
	bw2 = (Xmax-Xmin)/100
	#print (bin_width, bw2)
	hist_max = max(n[0])


	plt.ylim(min(bin_width*Our(Xmax),1./float(Nsample+1)),
	1.5*max(hist_max,bin_width*Our(0)))



	x = np.arange(Xmin,Xmax,0.001)
	#y_norm = list(map(PlotGaus,x,np.ones_like(x)*bin_width))
	y_norm = list(map(plotour,x,np.ones_like(x)*bin_width))
	# y_norm = list(map(PlotGaus(x,bin_width))
	plt.plot(x,y_norm,color='green',label='target f(x)')


	y_flat = list(map(plotourflat,x,np.ones_like(x)*bin_width))

	plt.plot(x,y_flat,color='red',label='proposal g(x)')
	plt.title("Density estimation with Monte Carlo")


	plt.legend()
	plt.show()
	#plt.savefig("RandomGaussPy.pdf")
	plt.savefig("ourfunc.pdf")
