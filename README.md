## Installation (for collaborators)

1. First, set up your Github account and install git

1. Clone https://github.com/dmartinezgamboa/praiseme-bot
   ```
   $ git clone git@github.com:dmartinezgamboa/praiseme-bot
   ```
   > Make sure to clone the praiseme repository.

1. Fork praiseme-bot and set up your remote
   ```
   $ git remote add <your_name> git@github.com:<your_username>/praiseme-bot
   ```
   > Replace `<your_name>` with your first name and `<your_username>` with your GitHub username.

1. Install [Docker for Mac](https://docs.docker.com/docker-for-mac/)


## Setup your dev environment

### 1. Setup the container(s):
- Run `./bin/dev/setup` from root dir
### 2. Access the container
- To run a python shell `docker exec -it praiseme_main_1 python`
- To start the app `docker exec -it praiseme_main_1 python main.py`
- To just access the container `docker exec -it praiseme_main_1 bash`
- To use ipython (recommended) `docker exec -it praiseme_main_1 ipython`
- To run tests in the `tests` directory `docker exec -it praiseme_main_1 python -m unittest discover -s ./tests -v -p "test_*.py"`
