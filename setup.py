from setuptools import setup

def _requires_from_file(filename):
    return open(filename).read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="landmasterlibrary",
    version="0.0.8",
    description="Convenient tools for me.",
    author="kinkinnbeer135ml",
    author_email="52403447+landmaster135@users.noreply.github.com",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="git+https://github.com/landmaster135/landmasterlibrary.git",
    packages=["landmasterlibrary"],
    package_dir={"landmasterlibrary": "src/landmasterlibrary"},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': [
            'text_replacer = landmasterlibrary.text_replacer:main',
            "printfunc = landmasterlibrary.generaltool:printfunc"
        ]
    },
    python_requires=">=3.7",
    install_requires=_requires_from_file("requirements.txt"),
    setup_requires=["pytest-runner"],
    extras_require={
        "test": ["pytest", "pytest-cov"],
        "doc": ["sphinx"]
    }
)
