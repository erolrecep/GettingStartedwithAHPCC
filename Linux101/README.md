# Linux 101: Hands-On Training

In this training, we are going to learn the basics of linux based OS operations. From creating a file to moving a folder to another document, downloading a file from internet. Now, let's get started.
<br>

We are going to start with a building a Python project template and then we are going to fill the inside of the template later.

- Change directory to where you want to create your project template

		$ cd /home/rerol/Desktop
 	
- Create the project folder

		$ mkdir python-project-template

- List the directory to see if we actually created the folder ???

		$ ls

- It looks like we created successfully! The next step is creating the each required file-folder for the project template.

		# Check if we are in the correct directory ???
		$ pwd

		# Yes, we are still in the correct directory!
		# Let's continue completing the tasks

		$ touch main.py
		$ touch requirements.txt
		$ mkdir data
		$ mkdir output

		# Now, we have enough files and folders to start project development.

Have you heard about fibonacci sequence? I love the idea, the sequence and how it's used for different purposes in the science, finance, and medical fields. Anyways, we are going to implement fibonacci sequence and apply some features to use the other folders we created. Let's continue.

		$ code .  
		# In the VM GUI, this command opens the Visual Studio Editor.

Now, we are in the editor. Let's continue writing some code.


		...

It looks like writing code in the training is going to take more than I anticipated. Let's clone the repo and continue working on there!

		$ git clone erolrecep/python-project-template-full.git

Since the name of the repository is different than we created, you can easily clone the repository to the same directory of "/home/rerol/Desktop/python-project-template".
<br>

To make sure the cloned repository is correctly cloned, let's check it.

		$ pwd 			# /home/username/Desktop/python-project-template
		$ cd .. 		# This command changes the directory to the parent directory
		$ cd python-project-template-full
		# Now, we are in the repository folder
