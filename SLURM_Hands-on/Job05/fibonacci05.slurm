#!/bin/bash
#SBATCH --job-name=fibonacci05_job            # Job name
#SBATCH --output=fibonacci05_output.txt       # Standard output and error log
#SBATCH --ntasks=1                            # Number of tasks
#SBATCH --time=00:00:10                       # Time limit (HH:MM:SS)
#SBATCH --mem=100M                            # Memory limit

# Load the necessary modules (if applicable)
module load python/3.x

# load miniforge module

# load one of the available Python virtual environments

# Run the Python program
python3 fibonacci05.py
