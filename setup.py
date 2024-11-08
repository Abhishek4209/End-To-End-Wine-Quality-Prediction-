import setuptools

with open('README.md','r',encoding='utf-8') as f:
    long_description=f.read() 

__version__ ='0.0.0'

REPO_NAME='End-To-End-Wine-Quality-Prediction'
AUTHOR_USER_NAME='ABHISHEK UPADHYAY'
SRC_REPO='WineQuality'
AUTHOR_EMAIL='abhishekupadhyay9336@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package for ml app',
    long_description_content='text/markdown',
    url=f'https://github.com/Abhishek4209/End-To-End-Wine-Quality-Prediction-',
    project_urls={
        "Bug Tracker":f"https://github.com/Abhishek4209/End-To-End-Wine-Quality-Prediction-/issues"
    },
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src')
    
)