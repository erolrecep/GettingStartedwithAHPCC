# MODULE

## Why do we need the Module?


---------

__How can we check which packages are loaded to my HPC system?__

    $ module list

__What are the available packages that I can load to my system?__

    $ module avail

__How to search for a package in the module database?__

    $ module spider <keyword>

__How to load a package to my system?__

    $ module load <package>/<version>

__How to remove or unload a package from my system?__

    $ module unload <package>/<version>

__Is there a way to see what happens if I install/load a package to my system?__

    $ module show <package>/<version>

__How to remove all loaded packages from my system?__

    $ module purge

## Exercises!

 1. How can I load required packages to compile a C code? Write the SLURM script for the C_program.
 2. How can I load required packages to run Python project? Write the SLURM script for the Python_program.
 3. Purge all loaded packages and make sure they are all gone?

