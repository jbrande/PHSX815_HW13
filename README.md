# PHSX815_HW13

This code allows a user to simulate the effects of dice rolls of various magnitudes and fairnesses. The user can modify the simulation by setting values for several input parameters.

The main program file is python/DiceRoll.py, which can be run with these input parameters:

-seed:		(optional) the seed for the random number generator

-Nrolls:	(optional) the number of rolls to make (>=1, default 1)

-Nsides:	(optional) the number of sides of the dice (>=2, default 6)

-probs:		(optional) the probabilities of the sides ordered least to greatest ("[P(1), ..., P(N)]", default equal probabilities. If this array does not match the number of sides, or it does not sum to 1, it will default to a fair die.)

-output:	(optional) the name of the output file to print to. if not given, the program will just print the results to stdout

Random.py has been modified to sample numbers from a categorical distribution with given probabilities.


After the dice are rolled, and the output saved to a file, the user can then plot the results of the simulations with python/DicePlot.py. This takes two input parameters:

-input:     (mandatory) the name of the file which holds the rolled dice data"

-Ndice:	 	(mandatory) given this number of dice (< num total rolls) plot the distribution of the sums of those rolls"

This reads in the results from the file, then plots a histogram of the sums of groups of Ndice dice, and also overplots a Gaussian PDF showing that these sums of groups of dice approximate a Gaussian function, as the Central Limit Theorem predicts.

**For this, I ran 1,000,000 fair dice rolls, grouped them into groups of 10 dice, binned the histogram with 41 bins, and manually fit the Gaussian mu=35, sigma=5.6 to fit the specifics of the histogram. While the mean will basically always be the mean of the histogram bins, the std deviation will strongly depend on the specific number of bins (and their widths) chosen, and so I picked a set of bins that gave no odd probability spikes and had no gaps. Then I manually picked the sigma that fit the histogram. This neatly shows the effect of the central limit theorem, as the dice rolls produce discrete outcomes, not continuous ones, but as the number of trials (sums of N dice) increases, the distribution of these sums approximates the Gaussian PDF.**


For best results, run the programs from the top level directory as "python python/program_name.py -params"
