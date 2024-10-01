# SLURM Hands-on Job Submission Exercises

In this part of the workshop, you will play with 6 mini Python projects, and you will make them run on HPC environment. You can either create an interactive SLURM compute job and run the programs in this compute node or write SLURM job scripts for each of them and submit these job scripts and get the results. On both scenarios, we will experience and compare which way would fit to your use case.

## Exercises
 - [Job01](Job01) -- In this Python project, you will run a fibonacci project and get the result to the terminal. The expected output is just a value.
 - [Job02](Job02) -- In this version of the Python project, you will get the fibonacci sequence up to the user input value. The expected output is printing the sequence with all the items.
 - [Job03](Job03) -- We want to record the output in a Python list. The expected output of the program is printing the items in a Python list.
 - [Job04](Job04) -- Time to write the output of the program in a file. The expected output is a txt file where the sequence is recorded to this file.
 - [Job05](Job05) -- We don't need to calculate the sequence everytime we run the program. Let's read the sequence from the txt file and return the user input value. The expected output is just the value.
 - [Job06](Job06) -- Let's visualize the first 100 items of the fibonacci sequence in a plot. In the another plot, visualize the ratio between two values of the sequence. The expected output is two plots.

These mini projects may seem very easy to run on our laptops or PCs. With these exercises, you will learn how to automate running projects and build SLURM job scripts and the following all the stages of a job with the commands we learned in the previous hands-on exercises.

Have fun and Good Luck!

## Reference
[Fibonacci Sequence Wiki](https://en.wikipedia.org/wiki/Fibonacci_sequence)
