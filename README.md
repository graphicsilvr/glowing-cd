# Continous Deployment with Digital Ocean and GitHub Actions
This repository contains the code for a continous deployment workflow that automatically deploys a Python application to a Digital Ocean droplet using GitHub Actions and SSH. It is still in the phase of debuggin because not all the steps are completely able to successfully automate the application of deployment process. 

# Components of the Solution

Solution Components
The solution consists of three main components: GitHub Actions, Digital Ocean, and SSH.

- GitHub Actions: This is the workflow automation tool we used to automate our application deployment process. We created a workflow that builds and deploys our application to a Digital Ocean VPS on each push to the main branch of our GitHub repository.

- Digital Ocean: This is the cloud hosting provider we used to host our application. We created a Droplet (VPS) on Digital Ocean and configured it to run our application.

- SSH: We used SSH (Secure Shell) to establish a secure connection between our local machine and the remote server. We used SSH to remotely execute commands on the Digital Ocean Droplet, such as pulling the latest changes from the GitHub repository and restarting the application.

The three components work together to create a seamless deployment workflow. GitHub Actions triggers the workflow, which then uses Bash scripts to automate the deployment process, and Digital Ocean provides the hosting environment for our application.

# Deployment Steps
- Provision a VPS: Rent a VPS from a provider such as DigitalOcean or AWS.

- Install APT packages: Use APT to install packages and dependencies that your Flask app needs to run. For example, you might need to install Python, pip, and other libraries like psycopg2 or flask_sqlalchemy.

- Clone your Flask app from GitHub: Clone your Flask app from GitHub onto your VPS using git clone. Make sure to create a virtual environment for your Flask app to run in.

- Install required Python packages: Use pip to install required Python packages for your Flask app. This might include Flask, Gunicorn, and any other required libraries.

- Configure Gunicorn: Create a Gunicorn configuration file to run your Flask app using the WSGI interface. This will allow Gunicorn to handle incoming web requests to your Flask app.

- Test the Gunicorn configuration: Test the Gunicorn configuration to ensure that your Flask app is running properly. You can do this by running Gunicorn in the background and visiting your Flask app in a web browser.

- Install NGINX: Use APT to install NGINX on your VPS. NGINX will handle web requests and reverse-proxy them to your Flask app.

- Configure NGINX: Create an NGINX configuration file to handle incoming web requests and reverse-proxy them to your Flask app. You will also need to configure NGINX to serve static files and handle SSL encryption if necessary.

- Test the NGINX configuration: Test the NGINX configuration to ensure that web requests are properly handled and reverse-proxied to your Flask app.

- Automate deployment with GitHub Actions: Create a GitHub Actions workflow to automatically deploy your Flask app to your VPS whenever you push changes to your GitHub repository. This will save you time and ensure that your Flask app is always up-to-date.

- Make sure to provide detailed instructions for each step and any relevant configuration files or scripts.

# Problems Encountered and Solutions
During the development of this solution, we encountered several problems, including:

1. SSH Authentication Issues: 

We initially had trouble setting up SSH authentication between GitHub Actions and Digital Ocean. We solved this problem by generating an SSH key pair and adding the public key to the authorized keys file on our Digital Ocean droplet.

2. Python Environment Setup: 

Setting up the Python environment on the Digital Ocean droplet was more complicated than we anticipated. We solved this problem by using the actions/setup-python GitHub Action to automate the process.

3. File Permissions: 

We encountered issues with file permissions when trying to restart the application after a deployment. We solved this problem by setting the appropriate file permissions on the application files and using the sudo command to execute the restart command with elevated privileges.

4. GitHub Actions Workflow Syntax Errors:

During the creation of the GitHub Actions workflow file, we encountered syntax errors that caused the workflow to fail. We solved this problem by carefully reviewing the documentation and correcting the syntax errors in the workflow file.

5. Debugging Remote Server Issues:

When deploying the Flask application to the remote Digital Ocean server, we encountered issues with the application not running as expected. We solved this problem by reviewing the server logs, debugging the code, and making necessary changes to the application configuration.

6. Host key verification failed: We encountered this error when trying to SSH into our Digital Ocean Droplet from our GitHub Actions workflow. To solve this problem, we updated the authorized_keys file on the server with the correct information.

7. StrictHostKeyChecking error: We encountered this error when trying to SSH into our Digital Ocean Droplet from our GitHub Actions workflow. To solve this problem, we updated our SSH client configuration by adding a config file in the ~/.ssh directory with the following lines of code:

Python

Host *
StrictHostKeyChecking no
UserKnownHostsFile=/dev/null

8. Missing SSH config file: We encountered this problem when trying to locate the SSH config file on our local machine. We solved this problem by creating a new file in the ~/.ssh directory and naming it "config".

# Conclusion
Overall, this project was a great learning experience in continous deployment and automation. 

By using GitHub Actions, Bash scripts, SSH and Digital Ocean, i am able to do some configurations to create a seamless deployment workflow that automatically deploys our Python application whenever new code is pushed to the repository. I learned valuable lessons about SSH authentication, Python environment setup, file permissions and more.

The implementation of my solution involved several iterations of troubleshooting and debugging. This debuggin is still actual because not all the steps are completely able to successfully automate the application of deployment process with all the steps described using GitHub Actions and Digital Ocean SSH.



