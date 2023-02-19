# Use a minimal base image for Ubuntu
FROM ubuntu:20.04

# Update the package index and install Python
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends python3-minimal \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Remove unnecessary packages and files
RUN apt-get update \
    && apt-get remove --purge --auto-remove -y python3-dev python3-lib2to3 python3-distutils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create the output directory
RUN mkdir /home/output

# Copy the Python script into the container
COPY word_count.py /app/

# Set the working directory and the entrypoint
WORKDIR /app
ENTRYPOINT ["python3", "word_count.py"]
