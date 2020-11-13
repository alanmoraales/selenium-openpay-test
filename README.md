an automated test using selenium

## Installation

- install python

- install virtualenv by running

```
pip install virtualenv
```

- inside de project's root directory, run:

```
virtualenv env
```

this creates the env folder

- go to env/Scrips/ folder, and run

```
activate
```

you should see now a "(env)" mark in the console line.

- return to the project's root directory
- now run:

```
pip install -r requirements.txt
```

this is going to install all the packages you need (selenium in this case)

- now you need the chrome web driver, you can get it in the follow link

```
https://sites.google.com/a/chromium.org/chromedriver/
```

- download and install the version corresponding to your Chrome version (you can check the Chrome version in help -> about Chrome)

- extract the .zip file in you pc root directory (C:)

- congrats, you can now run the test. Go to the project's root directory and run

```
python src/main.py
```
