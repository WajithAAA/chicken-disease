import setuptools

with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()


__version__ = "0.0.0"


REPO_NAME = 'chicken-disease'
AUTHOER_USER_NAME = "WajithAAA"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "azeeswajid@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version= __version__,
    author= AUTHOER_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "A Small package for CNN projects",
    long_description= long_description,
    long_description_content= "text/markdown",
    url= "http://github.com/{USER_NAME}/{REPO_NAME}",
    project_url= {
        "https://github.com/{USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir= {"":"src"},
    packages= setuptools.find_packages(where="src")

)