curl -fsSL https://get.docker.com -o get-docker.sh \
    && sh get-docker.sh \
    && rm get-docker.sh

groupadd docker \
    && usermod -aG docker vscode


# Install pip dependencies
pip install -e ".[notebook]"

ipython kernel install --user