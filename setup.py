import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="godaddy_reseller_client",
    version="0.9.0",
    author="Bokhari Chemseddine Ismail",
    author_email="bychis6@gmail.com",
    description="A small wrapper client of godaddy reseller api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bychis/godaddy-reseller",
    project_urls={
        "Bug Tracker": "https://github.com/bychis/godaddy-reseller/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)