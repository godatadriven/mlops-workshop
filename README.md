# **How to MLOps** 🚀

Welcome to this tutorial!

This repository contains code, exercises and explanations to help you turn a notebook solution into an operational machine learning application.
All the information can be found in the `/exercises` folder. If you feel like there is something missing, or you're getting stuck on a technical problem, try and find a solution with your neighbour! Still can't figure it out? Ask the host!

## **Setting up your environment** 💻

Before we get started, we need to make sure you have access to a coding environment and have all necessary dependencies installed, so you can edit and run the code.

### **Prerequisites**

- (optional) Fork this repository so you can make changes to it. This will be useful if you want to work on the bonus CI/CD exercise.

### **Setting up your editor**

There are two options you may choose from:

1. Using Github Codespaces (Recommended)
2. Using your own editor (e.g. VSCode) 

#### **1. Using Github Codespaces**

These are the steps to get started with GitHub Codespaces:

1. Navigate to this repository [on GitHub](https://github.com/ykerus/mlops-tutorial).
2. Click on the "Code" button on the right above the folder structure
3. Select "Codespaces"
4. Click on "Open Codespaces on main"
5. Wait until your environment is set up (this may take a while) and your terminal is ready
6. Wait a little bit longer, as another setup step may run
7. The setup is done when you you can run `docker` in a terminal and get a list of commands
9. Run the following in a terminal to check if all went well:
```bash
python -c "import turbine_power"
```
No ouput? Good! <br>Getting a `ModuleNotFoundError`? Not good... The automated setup didn't work. Please follow the *Installing dependencies* section below to set up the environment manually.

#### **2. Using your own editor**

These are the steps to get started with your own editor (e.g. VSCode):
1. Open a terminal
2. Clone the repository
```bash
git clone https://github.com/ykerus/mlops-tutorial.git
```

1. Open this folder (the cloned repo) in your editor
2. Open a terminal in this folder
3. Continue setting up in the "Installing dependencies" section below

### **Installing dependencies**

Assuming you've set up your editor with one of the above options, install the necessary dependencies as follows:

1. Create a virtual environment
```bash
python -m venv .venv
```
2. Activate the environment
```bash
source .venv/bin/activate
```

3. Install the dependencies
```bash
pip install -e ".[notebook]"
```
Not working? Double check in which folder you are running this in. It should contain `pyproject.toml` and `setup.cfg`.

4. Install the environment as kernel so we can use it in Jupyter
```bash
ipython kernel install --name ".venv" --user
```

5.  Check if all went well:
```bash
python -c "import turbine_power"
```
No ouput? Good! <br>Getting a `ModuleNotFoundError`? Not good... Double check if you went through all the steps above, check with your neighbours, or ask the host.

> **Note:** If you're getting installation errors, consider switching to Codespaces if you're working in your own editor.

6. Now your environment should be ready! Make sure, in all of the following, that you are running code within this environment (`.venv`). That means, if you create a new terminal, make sure to run `source .venv/bin/activate` again. That also means, if you run a notebook, select `.venv` as the kernel.

> **Note:** You may have to install the kernel first, depending on which editor you use. In the above instructions, we are assuming a VSCode environment, in which this is not necessary.


## **Exercises** 🧑‍💻

Find the exercises in the `/exercises` folder. Start with the first notebook and go from there!
