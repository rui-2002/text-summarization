import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

    # reading our readme file
    # writing our readme file(incase fo publish)


__version__="0.0.0.0"

REPO_NAME="text-summarization"
AUTHOR_USER_NAME="rui-2002"
SRC_REPO="textsummarizer" # name of src reprository(name of source folder) 
AUTHOR_EMAIL="sangwansumit628@gmail.com"

# it will look for our constructor file(__init__) install it as local package

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)




