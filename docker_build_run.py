import docker
import time
import requests
import os
import subprocess

from docker import errors
from pathlib import Path

PORT = 443

def build_docker_image(client, dockerfile='Dockerfile'):
    try:
        client.images.build(path="run", tag="ankiflask-multistage:latest")
        print("Docker image built successfully.")
    except errors.BuildError as e:
        print(f"Error building Docker image: {e}")
        return False
    return True

def build_docker_image_subprocess():
    try:
        result = subprocess.run(
            ['docker', 'build', '-t', 'ankiflask-multistage:latest', '.'],
            check=True,
            capture_output=True,
            text=True
        )
        print("Docker image built successfully.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error building Docker image: {e.stderr}")
        return False
    return True

def run_docker_container(client):
    container = None

    try:
        container = client.containers.run(
            "ankiflask-multistage:latest",
            name="ankiflask-container",
            ports={f'{PORT}/tcp': PORT},
            detach=True
        )
        time.sleep(5)
        response = requests.get(f"http://localhost:{PORT}/anki_flask/test")
        if response.status_code == 200:
            print("Server is running")
        else:
            print("Failed to connect to the server")
    except Exception as e:
        print(f"Error running Docker container: {e}")
    finally:
        if container:
            container.stop()
            container.remove()

def main():
    client = docker.from_env()
    project_root = Path(__file__).resolve().parent.parent
    dockerfile_path = 'Dockerfile'

    if build_docker_image_subprocess():
        run_docker_container(client)

if __name__ == "__main__":
    main()