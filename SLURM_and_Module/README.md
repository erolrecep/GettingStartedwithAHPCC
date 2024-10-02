# SLURM and Module

In this part of the workshop, we will introduce SLURM and Module software to you.

[SLURM](https://slurm.schedmd.com/documentation.html) and [Module](https://modules.sourceforge.net/) are the two very important software we use every day to manage our compute environment and jobs to submit in an HPC system. Once you grasp these software, the rest of the workflow will be a lot easier for you in an HPC systems.

This README file is a kind of guideline for the hands-on exercises for this part of the workshop.
 
## What is Module? and Why we use it?

High Performance Computing (HPC) or Supercomputing systems are shared environments. In other words, multiple users use these systems together. Everybody has their own setup to work on different tasks. To be able to manage these demands, there should be a mechanism where a user manages their software requirements and does dynamic modifications. Module allows these changes and modifications on the software. 

There are a number of software, and almost each software has multiple versions. It's almost impossible to install all these software at the same time to a computer or compute environment. It is very possible to have conflicts between software, and some will prevent others to run. These and a lot more issues would easily be solved if we use __Module__ for our software management.

## What is SLURM? and Why we use it?
Simple Linux Resource Management or Slurm Workload Management is a software that is designed and provided to schedule your jobs, to manage your resources (including CPUs, GPUs, RAM, or storage), or monitor submitted jobs to an HPC system. As we can guess from the name of the software, SLURM is a very useful software for multiple purposes. There are many commands that you can use, and these commands are introduced in the hands-on exercises.

By completing the hands-on exercises in this part of the workshop, you're going to have a solid understanding of how you can manage your compute environment and manage your jobs in an HPC.

## Hands-on Exercises

 - [Module Hands-on Exercise](module.md)
 - [SLURM Hands-on Exercise](slurm.md)

Good Luck!
