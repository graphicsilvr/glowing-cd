# Continous Deployment with Digital Ocean and GitHub Actions
This repository contains the code for a continous deployment workflow that automatically deploys a Python application to a Digital Ocean droplet using GitHub Actions and SSH.

# Components of the Solution

The solution consists of three main components:

1. GitHub Actions: 
GitHub Actions is a feature of GitHub that enables you to automate workflows, such as building, testing, and deploying your code. In this solution, we use GitHub Actions to automatically trigger the deployment workflow whenever code is pushed to the main branch of the repository.

2. Bash Scripts: 
We use Bash scripts to perform various tasks, such as setting up the Python environment, installing dependencies, and restarting the application after a deployment. The Bash scripts are executed by the GitHub Actions workflow.

3. Digital Ocean: 
Digital Ocean is a cloud hosting provider that we use to host our Python application. We use Digital Ocean droplets, which are virtual machines that can be used to host websites, applications, and other services.

The three components work together to create a seamless deployment workflow. GitHub Actions triggers the workflow, which then uses Bash scripts to automate the deployment process, and Digital Ocean provides the hosting environment for our application.

# Problems Encountered and Solutions
During the development of this solution, we encountered several problems, including:

1. SSH Authentication Issues: 

We initially had trouble setting up SSH authentication between GitHub Actions and Digital Ocean. We solved this problem by generating an SSH key pair and adding the public key to the authorized keys file on our Digital Ocean droplet.

2. Python Environment Setup: 

Setting up the Python environment on the Digital Ocean droplet was more complicated than we anticipated. We solved this problem by using the actions/setup-python GitHub Action to automate the process.

3. File Permissions: 

We encountered issues with file permissions when trying to restart the application after a deployment. We solved this problem by setting the appropriate file permissions on the application files and using the sudo command to execute the restart command with elevated privileges.

# Conclusion
Overall, this project was a great learning experience in continous deployment and automation. 

By using GitHub Actions, Bash scripts, and Digital Ocean, we were able to create a seamless deployment workflow that automatically deploys our Python application whenever new code is pushed to the repository. We also learned valuable lessons about SSH authentication, Python environment setup, and file permissions.