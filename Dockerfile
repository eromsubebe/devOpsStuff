# set base image
From python:3.8

# set working directory in the container
WORKDIR /test

# copy dependencies file to working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy content from local src directory to the working directory
COPY src/ .


# command to run on the container start
ENTRYPOINT [ "python", "./devops_test.py"]

# Keep the container UP
CMD tail -f /dev/null


