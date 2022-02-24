import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="landmaster-library",
    version="0.0.1",
    author="landmaster135",
    author_email="52403447+landmaster135@users.noreply.github.com",
    description="Convenient tools for me",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/landmaster135/landmaster-library",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['sample_command = ExportSqlite3ToCSV:main']
    },
    python_requires='>=3.7',
)
