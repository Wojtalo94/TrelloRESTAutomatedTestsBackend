# WebAutomatedTestsBackend

# Automated Tests - GameSDKWebTests


## Table of Contents

1. [Cloning an automated test repository](#cloning-an-automated-test-repository)
2. [Preparation of the web application environment](#preparation-of-the-web-application-environment)
3. [Creating and running a container](#creating-and-running-a-container)
4. [Running GameServerSimulator](#running-gameserversimulator) 
5. [Browser configuration](#browser-configuration)
6. [Tips](#tips)


## Cloning an automated test repository

Clone the **AutomatedTests-GameSDKWebTests** repository:
```bash
git clone https://central-bitbucket.novomatic-tech.com/scm/gcf/automatedtests-gamesdkwebtests.git
```


## Preparation of the web application environment

**Step 1:** Clone the **WebAssembly-PoC** repository:
```bash
git clone https://central-bitbucket.novomatic-tech.com/scm/gcf/webassembly-poc.git
```

**Step 2:** Create a folder **web** in **webassembly-poc** folder and put in the **web** folder 2 folders:
* `distillygame`
* `wexiilog`

**Step 3:** Clone **VOCSServerSimulator** repository:
```bash
git clone https://central-bitbucket.novomatic-tech.com/scm/nf/util-web-vocsserversimulator.git
```

**Step 4:** Create a virtual environment (**venv**) for the **VOCSServerSimulator**, so in the downloaded folder **util-web-vocsserversimulator** along with the installation of additional libraries from the file **requirements.txt**:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt  
```


## Creating and running a container

**Step 1:** Install **Docker Desktop** and log into it

**Step 2:** Open a terminal or command line and navigate to the location of the **docker-compose.yaml** file. Then use the **docker-compose up** command, which will load the configuration from the **docker-compose.yaml** file and create containers based on this information. Note that this command must be executed in the folder where the **docker-compose.yaml** file is located:
```bash
docker-compose up
```

*Eventually open the **webassembly-poc** folder in VSC and right-click on the **docker-compose.yaml** file and select **Compose Up**.*

**Step 3:** Go to **Docker Desktop** and see if the container has been started.


## Running GameServerSimulator

**Step 1:** Navigate to the folder **webassembly-poc\tools\util-web-vocsserversimulator** and launch the terminal.

**Step 2:** Activate the virtual environment (**venv**) previously created in [Preparation of the web application environment](#preparation-of-the-web-application-environment) in **Step 4**:
```bash
.venv\Scripts\activate
```

**Step 3:** Run **GameServerSimulator**:
```bash
python GameServerSimulator.py --gamesDataDir VOCSServerSimulator/Windows/GamesData
```

*Eventually open the **webassembly-poc\tools\util-web-vocsserversimulator** folder in VSC and start the server with the **RUN AND DEBUG** button.*


## Browser configuration
In the `config.yml` file we have:
* configured basic address of the game under test
* the type of browser we want to use for testing
* the configuration in which we want to run the browser

```python
# YAML
base_url: 'http://127.0.0.1/distillygame/'
browser: 'firefox' # choose 'chrome' or 'firefox' or 'edge'

# test settings
fullscreen: true
incognito: true
```


## Tips

#### Frequently run tests locally
If we will often run our tests locally, it is a good idea to comment out the `install_browser` method in the `environment.py` file, which installs and updates drivers for browsers. If we leave this method and frequently run our tests locally, at some point we may be blocked from installing/updating drivers because there is a limit for some browsers (e.g., for firefox we have 60 installs/updates per hour).
