import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ids-ac",
    version="0.0.1",
    author="dzokha",
    author_email="dzokha1010@gmail.com",
    description="Adaptive Cybersecurity Intrusion Detection System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dzokha/ids-ac",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

# python3 setup.py sdist bdist_wheel
# twine upload dist/*