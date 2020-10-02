
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hmrsplanner",  # Replace with your own username
    version="0.0.1",
    author="Gabriel Rodrigues",
    author_email="gabrielsr@gmail.com",
    description="Planner for Heterogeneous Multi-Robots Systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gabrielsr/hmrsplanner",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
