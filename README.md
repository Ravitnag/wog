
# DevOps Final Project - Python Game & Flask Scoreboard

## Overview

This project is a simple game written in Python, with a Flask-based web page that displays the user's score. The main goal of this repository is to demonstrate a complete DevOps pipeline using Jenkins, Docker, and Selenium for testing.

## Features

-   Python-based game logic
-   Flask web application to display the score
-   Jenkins pipeline for CI/CD
-   Dockerfile to containerize the application
-   Automated testing with Selenium
-   Image pushed to Docker Hub

**in order to run Jenkins pipeline and push the image into docker-hub, you should add Docker Hub credentials to Jenkins:**
1. Log in to your Jenkins instance.
2. Go to Manage Jenkins > Manage Credentials (or Credentials in the left-hand menu if you have a specific credentials store configured).
3. Select the appropriate domain (or global credentials if you're unsure).
4. Click on Add Credentials.
5. Select Username with password as the kind.
6. Enter your Docker Hub username and password.  give the credentials a unique ID:  docker-hub-credentials
7. Click OK to save the credentials.
