# SE507µ Hacking password hashes with rainbow tables

## Assignment 1

For the first assignment, you have to write a program that will try to access the secret part
of a website, by finding the correct credentials. Some code to start with has been made
available to you:
- `server.py` is a small web application
- `test.py` is an automated test for the web application

First install the `flask` and `selenium` Python modules. Then, install the
`selenium` driver for Chrome (https://sites.google.com/a/chromium.org/chromedriver/downloads)

You can launch the server by running the following command from the `code` directory:

    FLASK_APP=server flask run

The way to set the `FLASK_APP` environment variable may depend on your actuel operating system.
Please refer to the `flask` documentation.

Then, you can launch the test by running the following command from the `code` directory:

    python3 test.py

Do not forget to include the path to `chromedriver` in your `PATH` environment variable.

For this first assignment, you have two missions to execute:
1. Modify the web application so that no to store the password in clear, but only store a hash
of the password. For this assignment, use an _LM Hash_ that you can compute with the
`passlib` module (https://passlib.readthedocs.io/en/stable/lib/passlib.hash.lmhash.html)
2. Then modify the automated test to make it a brute-force attack that will try all the passwords,
one after the other, and measure how much time it takes to guess the right password.
For this assignment, we will assume that passwords are only made of lowercase letters.

