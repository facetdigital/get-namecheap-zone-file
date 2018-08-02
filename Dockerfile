FROM selenium/standalone-firefox
WORKDIR /app

# Install python, pip, xvfb
RUN sudo apt-get -qq update && \
    sudo apt-get install -y python python-pip python-dev build-essential git libgtk-3-0 libdbus-glib-1-2 && \
    sudo -H pip install --upgrade pip

# Install selenium
RUN sudo -H pip install selenium

# Install dns_compare
RUN sudo -H pip install dnspython git+http://github.com/joemiller/dns_compare.git#egg=dns_compare

# Install cli53
RUN sudo wget -O /usr/local/bin/cli53 https://github.com/barnybug/cli53/releases/download/0.8.12/cli53-linux-amd64 && \
    sudo chmod +x /usr/local/bin/cli53

RUN sudo apt-get -y autoremove

CMD ["bash"]
