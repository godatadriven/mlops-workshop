curl -fsSL https://get.docker.com -o get-docker.sh \
    && sh get-docker.sh \
    && rm get-docker.sh

python -m venv .venv
source .venv/bin/activate
pip install ".[notebook]"
