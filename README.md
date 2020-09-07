# devOpsStuff

This is a simple python application that queries URL "https://api.macaddress.io/ 
for the Company name associated with MAC address specified by the User

## The Code
All of the code (devops_test.py & requirements.txt)is located under the 'test' directory of the deployed container

## Installation (assumption is that docker is installed on the host)
- Clone the repository 'git clone https://github.com/eromsubebe/devOpsStuff'
- Build the image 'docker build -t app_devops .'
- Deploy and start the container 'docker run -it --name devops app_devops:latest /bin/bash'

## Security Implication
The authentication token (api-key) required for making MAC addressed query on the URL above has been hardcoded
within the script. 
This makes it possible for anyone to use your credentials to make calls to the service, pretending to be you. 

The expectation is that the credential details are stored externally (secrets, vault) and are called by the script 
when the script is triggered

Also, the need to include some of rate limiting on the number of requests the applications makes within
a given window needs to be explored further to prevent possible denial of service attack
that could be initiated with this script
