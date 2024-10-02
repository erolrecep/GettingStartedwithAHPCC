# SLURM Workload Management

## Why do we need SLURM?

--------

__Which SLURM command lists all running jobs in the HPC system?__

    $ squeue

This command would be very useful if you use with other parameters. For instance, if you would like to see all the running jobs for a specific user or for your account, call this;

    $ squeue -u <username>

If you would like to see the real-time changes on the job, you can call this command;

    $ watch squeue -u <username>

Here is a template that you can use to write your own script for a job:

    #!/bin/bash
    #SBATCH --job-name=hello_world
    #SBATCH --output=output_%j.txt
    #SBATCH --ntasks=1
    #SBATCH --time=00:10:00

    module load gcc
    gcc -o main main.c -lm
    ./main

You can name this script above as "hello.slurm" or "hello.sh". Then, you can submit the job as follows:

    $ sbatch hello.slurm
    $ # or
    $ sbatch hello.sh

After you submit the job, SLURM generates a job ID and prints the job ID to the terminal. Through this job ID, you can start following the stages of the job.

    $ scontrol show job <job-ID>
    $ # or
    $ sstat -j <job-ID>

Congratulations! You submitted your first job. This is huge!

Now, let's learn another important SLURM command.
If you would like to learn which compute nodes are available so you can choose the best fit for your use case: 

    $ sinfo

If you remember the compute node creation job command:

    $ srun -N1 -n1 -c1 -p cloud72 -q cloud -t 72:00:00 --pty /bin/bash

_cloud72_ info is gathered from $ sinfo command results.

We can create a _gpu_ compute job with the similar command:

    $ srun --nodes=1 --ntasks-per-node=1  --cpus-per-task=32 --partition agpu06 --time=0:15:00 --pty /bin/bash

Awesome! We created two interactive compute jobs. 

Sometimes, the time we allocated may be a lot more than we anticipated. In this case, after we complete all our work, we can easily conclude the compute job or any other job that we submitted earlier. This command is:

    $ scancel <job-ID>

As it's seen that, you just provide the job-Id to cancel any job you submitted. 

Sometimes, we may forget what the job ID was. In these cases, you can easily call:

    $ squeue -u <username>

The result of this command is going to give you the job ID of any job you submitted.



## Exercises

In the __"../SLURM_Hands-on"__ folder, there are 6 mini Python projects. In this hands-on exercises, you can practice writing SLURM job scripts and submit these jobs, and then monitor how things go in there. If you have any question, feel free to ask!

Good Luck!


