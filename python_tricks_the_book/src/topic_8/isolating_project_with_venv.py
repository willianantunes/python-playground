'''
Python includes a powerful packaging system to manage the module dependencies of your programs: pip

One confusing aspect of installing packages with pip is that it tries to install them
into YOUR GLOBAL PYTHON ENVIRONMENT by default.

The solution: virtual environments.

--

Useful commands and steps:

> pydoc modules
# Pointing to the global environment
> which pip3
/home/wantunes/.pyenv/shims/pip3
# New Python virtual environment
> python3 -m venv ./venv
# Even if you install packages now, they'd still end up in the global Python environment
# To change that, execute...
> source venv/bin/activate
# Now if you execute which, you'll get the bin from the venv folder
> which pip3
/home/wantunes/Development/git-work/python-playground/python_tricks_the_book/src/topic_8/test/venv/bin/pip3
# Running `pip list` will show an almost empty list of installed packages...
> pip list
> pip install schedule
# If you want to deactivate the VENV, you can close your session and open another or executes...
> deactivate
# Now `which pip3` will show your global setup

pip freeze > requirements.txt
pip install -r requirements.txt

https://docs.python-guide.org/dev/virtualenvs/
https://realpython.com/pipenv-guide/
'''
