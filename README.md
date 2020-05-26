# Docker-Flask-Waitress-Demo

Dockerized Flask &amp; Waitress Demo

## Notes

* **Flask**: Main Web Application Framework
* **Waitress**: Serves Flask Application
* **Paste**: Outputs Logs to Console (StdOut)

## Usage

1. Run Docker Container

    ``` bash
    docker build --target Development -t pkeech/docker-flask-waitress-demo:latest .
    docker run -d -p 80:80 --name demo pkeech/docker-flask-waitress-demo:latest
    ```

## (Optional) Update PIP Packages

1. Run Docker Container

2. Login to Bash Console of Docker Container

    ``` bash
    docker exec -it demo /bin/bash
    ```

3. Update PIP Packages

    ``` bash
    pip install flask -U
    pip install waitress -U
    pip install paste -U
    ```

4. List Current Requirements with `pip freeze`

5. Copy requirements to `requirements.txt`.
