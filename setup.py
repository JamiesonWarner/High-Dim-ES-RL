import setuptools

with open("README.rst", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="esrl",
    version="0.0.1",
    author="Nils Müller",
    author_email="nils.mueller@ini.rub.de",
    description="Challenges in High-dimensional Reinforcement Learning with Evolution Strategies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "numpy>=1.18.2",
        "matplotlib>=3.1.3"
        "tensorflow>=2.1.0",
        "gym>=0.15.4",
        "keras>=2.3.1"
    ],                                             
    url="https://github.com/NiMlr/High-Dim-ES-RL",  
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",   
    ),
)
