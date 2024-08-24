# Facial Recognition

This is a small demo made with the power of Python and Docker that labels
faces of people in a video.

To do this, the model must be fed images of the people we want to recognize
and a video.

It has the following directory structure:

- app
    - images
        - person1.jpg
        - person2.jpg
        - ...
    - videos
        - video1.mp4
        - video2.mp4
        - ...
    - output
        - video1.mp4
        - video2.mp4
        - ...
    - main.py
- dockerfile
- docker-compose.yml
- readme.md
- .gitignore

## How to use

First of all you should make sure that you have loaded the images directory
with photos of the faces you want to be able to recognize. They should follow
the naming convention persons_name.jpg.

In the main.py script you can change the name of the file to be processed. In
the future, this should be an env variable in the docker compose file.

To run just write the following command:

```docker compose up```

Docker and Docker compose are required to run this repository.
