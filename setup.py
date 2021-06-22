import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sqlcsvsql",
    version="0.0.1",
    author="Md. Abdur Razzaq Riyadh",
    author_email="riyadh.razzaq@gmail.com",
    description="a lightweight package to convert sql files to csv and vice versa",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/riyadhrazzaq/sqlcsvsql.git",
    project_urls={
        "Bug Tracker": "https://github.com/riyadhrazzaq/sqlcsvsql.git/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    entry_points={"console_scripts": ["sqlcsvsql = sqlcsvsql.__main__:main"]},
    install_requires=["pandas"],
)
