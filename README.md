# Automated Tests - TrelloRESTAutomatedTestsBackend

## Table of Contents

1. [Cloning an automated test repository](#cloning-an-automated-test-repository)
2. [Preparation of the environment](#preparation-of-the-environment)

## Cloning an automated test repository

Clone the **TrelloRESTAutomatedTestsBackend** repository:

```bash
git clone https://github.com/Wojtalo94/TrelloRESTAutomatedTestsBackend.git
```

## Preparation of the environment

Create a virtual environment (**venv**) along with the installation of additional libraries from the file **requirements.txt**:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Prepare a **csv file** with the data in the **tools** folder.

File name: *user_data.csv*

Data:
```
TRELLO_API_KEY,{TRELLO_API_KEY}
TRELLO_API_TOKEN,{TRELLO_API_TOKEN}
EMAIL,{EMAIL}
PASSWORD,{PASSWORD}
```