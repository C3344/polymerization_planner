from setuptools import setup, find_packages


from setuptools import setup, find_packages

setup(
    name="polymerization_planner",
    version="0.1.0",
    description="A tool to generate polymerization reaction recipes from user-defined molar ratios and stock concentrations."
    "Please see the PDF instruction in the github link provided",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Cesar Ramirez",
    author_email="cr828@scarletmail.rutgers.edu",  # <-- Optional but required for PyPI upload
    url="https://github.com/C3344/polymerization_planner",  # <-- Optional but recommended
    packages=find_packages(),
    install_requires=[
        "pandas",
        "openpyxl",
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Change if you're using another license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": ["polymerization-planner=polymerization_planner.runner:main"]
    },
)
parser = argparse.ArgumentParser(
    description="Polymerization Planner CLI\n\n📘 Tutorial: https://github.com/C3344/polymerization_planner/blob/main/docs/tutorial.pdf",
    formatter_class=argparse.RawTextHelpFormatter,
)
