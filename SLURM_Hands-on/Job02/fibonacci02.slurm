#!/bin/bash
#SBATCH --job-name=fibonacci02_job            # Job name
#SBATCH --output=fibonacci02_output.txt       # Standard output and error log
#SBATCH --ntasks=1                            # Number of tasks
#SBATCH --time=00:00:10                       # Time limit (HH:MM:SS)
#SBATCH --mem=100M                            # Memory limit

# Purge all the previously loaded packages

# Load the necessary modules (if applicable)
module load python/3.x

# Run the Python program
python3 fibonacci02.py
