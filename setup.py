import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sqlcsvsql",
    version="0.0.2",
    author="Md. Abdur Razzaq Riyadh",
    author_email="riyadh.razzaq@gmail.com",
    description="a lightweight package to convert files between sql and csv",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/riyadhrazzaq/sqlcsvsql",
    project_urls={
        "Bug Tracker": "https://github.com/riyadhrazzaq/sqlcsvsql/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
    entry_points={"console_scripts": ["sqlcsvsql = sqlcsvsql.__main__:main"]},
)
