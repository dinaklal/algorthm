import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='algorthm',  
     version='0.5',
     author="Dinak Lal V",
     author_email="dinaklal@gmail.com",
     description="A package for studying various Algorithms and visualizing the operations ",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/dinaklal/algorthm",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
         "Development Status :: 2 - Pre-Alpha",
     ], )