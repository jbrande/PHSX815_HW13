# #! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import re
import json

import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from python.Random import Random

# main function for our coin toss Python code
if __name__ == "__main__":
	# if no args passed (need at least the input file), dump the help message
	# if the user includes the flag -h or --help print the options
	if '-h' in sys.argv or '--help' in sys.argv or len(sys.argv) == 1:
		print ("Usage: %s [-input0 string] [-input1 string] [-Ndice int]" % sys.argv[0])
		print ("-input:      (mandatory) the name of the file which holds the rolled dice data")
		print ("-Ndice:	 	 (mandatory) given this number of dice (< num total rolls) plot the distribution of the sums of those rolls")
		print
		sys.exit(1)

	# read the user-provided arguments from the command line (if there)
	if '-input' in sys.argv:
		p = sys.argv.index('-input')
		try:
			input0 = sys.argv[p+1]
		except IndexError as e:
			print("Must pass input filename")
	else:
		print("Must pass input filename")

	if '-Ndice' in sys.argv:
		p = sys.argv.index('-Ndice')
		try:
			Ndice = int(sys.argv[p+1])
		except IndexError as e:
			print("Must pass number of dice to group")
	else:
		print("Must pass number of dice to group")


	# load json data from file
	res0 = ""
	with open(input0) as f:
		res0 = json.load(f)
		f.close()

	# get split locations to calculate sums of groups of dice
	inds0 = np.arange(0, len(res0["rolls"]), Ndice)[1:]

	# split rolls into subarrays, and sum them
	splits0 = np.split(res0["rolls"], inds0)
	sums0 = []
	for s in splits0:
		sums0.append(np.sum(s))

	# do plotting
	fig = plt.figure(figsize=(10, 8))
	ax = plt.gca()
	h = ax.hist(sums0, 41, density=True, label="Dice Sum Probability") # number of bins manually chosen to give good spacing
	
	# gaussian pdf:
	mu = np.mean(h[1])
	sig = 5.6 # just manually fit, this is very dependent on the number of bins
	x = np.linspace(h[1][0], h[1][-1], 100)
	gaus = (1/(sig*np.sqrt(2*np.pi)))*np.exp((-1/2) * ((x - mu)/sig)**2)
	plt.plot(x, gaus, c="tomato", lw=3, label=r"Gaussian $\sigma=${}, $\mu=${}".format(sig, mu))
	
	plt.legend()
	ax.set_xlabel('Group Sum')
	ax.set_ylabel('Probability')
	plt.title('Sums of {} Dice'.format(Ndice))
	plt.show()
	fig.savefig("plots/dice_hist.jpg", dpi=300)