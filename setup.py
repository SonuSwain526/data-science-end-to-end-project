from setuptools import find_packages, setup

def get_req(ip_file):
    with open(ip_file, "r") as f:
        content = f.read()
        return content.split("\n")

setup(
    name="end-to-end-dl-project",
    version="0.0.1",
    author="just me",
    author_email="gourabswain526@gmail.com",
    packages=find_packages(),
    install_requires=get_req("requiremets.txt")
)
