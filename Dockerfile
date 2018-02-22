FROM selenium/standalone-firefox
WORKDIR /app

# Install python, pip, xvfb
RUN sudo apt-get -qq update && \
    sudo apt-get install -y python python-pip python-dev build-essential && \
    sudo pip install --upgrade pip

# Install selenium
RUN sudo pip install selenium

CMD ["bash"]
