import setuptools

with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "chicken-disease-classification"
AUTHOR_USER_NAME = "Gerard-47"
SRC_REPO = "CDClassifier"
AUTHOR_EMAIL = "niyigengagerard.47@gmail.com"

setuptools.setup(
name = SRC_REPO,
version = __version__,
author = AUTHOR_USER_NAME,
author_email = AUTHOR_EMAIL,
description = "Chicken classifier project using Fecal image to classify whether the chicken has Coccidiosis or not using CNN",
long_description = long_description,
long_description_content = "text/markdown",
url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
project_url = {
    "Bug Tracker" : f"https://githu.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
},
package_dir = {"":"src"},
packages = setuptools.find_packages(where = "src")
)