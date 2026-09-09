FROM python:3.13-slim

WORKDIR /app

RUN pip install --upgrade pip

# Copy source first so we can install in editable mode
COPY . .

# Install plugins and automate-home from the dev branches (same order as CI:
# plugins first so the final automate-home install is not overwritten)
RUN pip install ".[dev]" && \
    pip install --force-reinstall \
        "git+https://github.com/majamassarini/automate-knx-plugin.git@dev" && \
    pip install --force-reinstall \
        "git+https://github.com/majamassarini/automate-lifx-plugin.git@dev" && \
    pip install --force-reinstall \
        "git+https://github.com/majamassarini/automate-sonos-plugin.git@dev" && \
    pip install --force-reinstall \
        "git+https://github.com/majamassarini/automate-home.git@dev"

CMD ["python", "field_test/server.py"]
