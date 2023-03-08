# pydocstyle warning (D100) + pylint warning (missing-docstring)

import sys  # pyflakes/pylint warning (unused-import)

import requests


def display(message):
    print(message)


def unused():
    return


if __name__ == "__main__":
    display(["Hello"])  ## pycodestyle warning (E262)

    MY_SECRET = "tethys"

    data = requests.get("https://www.educative.io/", verify=False)
    print(data.status_code)
