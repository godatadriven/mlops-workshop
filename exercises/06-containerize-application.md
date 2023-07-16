# Containerizing the application 🐳

We've now created an API that uses our model to make predictions. However, we are still running it locally, so others cannot benefits from it yet. 

We need our API to run on a server, so others can use it.
Let's now containerize our application, so we can easily deploy it to a server.

## Why containerize?

Containerization is a way to package software so it can run in isolation from other processes on a machine. This makes it easy to run the same software, with the same dependencies, on different machines. 

Perfect if we want to deploy our application to a server in the cloud!

> **Note:** in the following, we refer to a *container* as the running instance of a *container image*. An image is a file that contains all the dependencies and configuration required to run a container.

## Build and run container image locally

We've already created a `Dockerfile` in the root of our project. This file contains instructions on how to build our container image.

Excercises:

1. Inspect the `Dockerfile`
2. Build the container using:
```bash
docker build -t turbine-image .
```

3. Run the container using:
```bash
docker run -p 8080:8080 turbine-image
```

> **Note:** If you are working in Codespaces, you may need to forward port 8080 to your local machine. To do this, click the "Ports" button in the bottom left of the Codespaces window, and add a new port forwarding rule for port 8080. 

4. When prompted, navigate to the URL in your browser: [http://0.0.0.0:8080/docs](http://0.0.0.0:8080/docs) and try the API again!

Exacly the same as before, but now running in a container! 🎉
