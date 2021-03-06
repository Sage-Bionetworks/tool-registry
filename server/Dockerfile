FROM python:3.8.5-slim-buster

ENV APP_DIR=/opt/app

# Safer bash scripts with 'set -euxo pipefail'
SHELL ["/bin/bash", "-euxo", "pipefail", "-c"]

# Install dependencies
# hadolint ignore=DL3008
RUN apt-get update -qq -y \
    && apt-get install --no-install-recommends -qq -y \
        build-essential \
        gosu \
        libpcre3 \
        libpcre3-dev \
    && apt-get -y autoclean \
    && apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/*

# Copy server files
COPY openapi_server ${APP_DIR}/openapi_server
COPY requirements.txt uwsgi.ini ${APP_DIR}/
COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

# Install dependencies
RUN pip install --no-cache-dir \
    -r ${APP_DIR}/requirements.txt uWSGI==2.0.19.1

# Expose the port used by the application
EXPOSE 8080

# Set the entrypoint script and the default command run by the container
ENTRYPOINT ["/docker-entrypoint.sh"]

# Run server in development mode
# CMD ["python", "-m", "openapi_server"]

# Run server in production mode
CMD ["uwsgi", "--ini", "uwsgi.ini", "--lazy", "--http", ":8080"]