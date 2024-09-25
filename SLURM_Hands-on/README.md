# SLURM Notes

Simple Linux Resource Management Software!

---------

## Demo

Think that you want to run a computation on an HPC and don't know where to start. You want to learn the steps by providing very simple operations to get the idea and add some other stuff or feature until you get into the sample that is similar to your job that you want to run. In this demo, while I was preparing, my thought process was so. So here is my attempt to learn how I can use HPC to get benefit and how can I submit my job then read the output to understand how things went.

 1. I know that there is an interactive way of doing these things but I prefer to do them manually through terminal.
 	a. My first attempt is learning the server name that the SLURM scheduler assigned my computation. Is this the same with my compute environment or different.
 	a. Run the already written slurm job and show the results.
 	b. Also mention about the job id assigned and the other information you need 
 2. The next job is get the information about the node that this job run.
 	a. Number of CPU cores, RAM, IP address, and model make of the CPU.
 	b. Run this job in C and Python codes!
 3. Let's run a matrix multiplication with C and Python
 4. Clone moviebarcode repository and run as slurm batch and the manually running job!
 	a. First try to run as manually job. (Linux 101 practice will be helpful for this example!)
 	b. After I learn the steps, I believe I can write slurm job and submit it!
 5. Provide multi-thread Python script to run the Python program on multiple threads.
 6. Provide multi-core Python script to run the Python program on multiple processes. Also display the htop in live process to support the multi-process run to the audience!
 7. Run an MPI job on multi-core first then multi-node.
 8. Discuss, what would happen if your job fail?

In these examples, do not forget to show how to read the information about the SLURM and diagnose the code if it's not running. Also let them know that, you may always face with and issue then learn how to read the issue!
 - SLURM is used for multiple things
	+ Resource management
	+ Software management
	+ Resource allocation
	+ Scheduling and job assignment
 - Also inform users what to do to learn more about the fail job!



-----------------------

# Demo: Hands-on Training for SLURM, resource management and job submission


 1. fibonacci1.py --> Initial version
 2. fibonacci2.py --> List all the elements of the sequence up to user input
 3. fibonacci3.py --> records the sequence to a list
 4. fibonacci4.py --> Write the sequence to a txt file
 5. fibonacci5.py --> search the input data from the recorded txt file and if it's not in the list then calculate the new one.
 6. fibonacci6.py --> Let's visualize the first 100 numbers in a plot and also display the ratio of sequence in a plot as well.

It looks like we can easily do all the stuff here however, in an HPC environment, we need to automate these kind of stuff and submit these jobs with SLURM.

Lets change directory to slurm-jobs folder and run each one of the fibonacci files with slurm jobs.

#TODO --> Make sure to have slurm-jobs directory and create a separate folder for each job submission there. Also mention about why we created a separate directory for each job there!
























