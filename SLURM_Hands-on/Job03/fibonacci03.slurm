#!/bin/bash
#SBATCH --job-name=fibonacci03_job            # Job name
#SBATCH --output=fibonacci03_output.txt       # Standard output and error log
#SBATCH --ntasks=1                            # Number of tasks
#SBATCH --time=00:00:10                       # Time limit (HH:MM:SS)
#SBATCH --mem=100M                            # Memory limit

# Purge previously loaded packages

# Load the necessary modules (if applicable)
module load ???

# Run the Python program
python3 fibonacci03.py
