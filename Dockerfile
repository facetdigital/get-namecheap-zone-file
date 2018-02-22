FROM selenium/standalone-firefox
WORKDIR /app

# Install python, pip, xvfb
RUN sudo apt-get -qq update && \
    sudo apt-get install -y python python-pip python-dev build-essential && \
    sudo pip install --upgrade pip

# Install selenium
RUN sudo pip install selenium

# Install cli53
RUN sudo wget -O /usr/local/bin/cli53 https://github.com/barnybug/cli53/releases/download/0.8.12/cli53-linux-amd64 && \
    sudo chmod +x /usr/local/bin/cli53

CMD ["bash"]
