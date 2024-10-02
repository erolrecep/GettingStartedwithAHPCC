#!/bin/bash
#SBATCH --job-name=hello_world
#SBATCH --output=output_%j.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --time=00:10:00

module purge
module load gcc
gcc -o main main.c -lm
./main
