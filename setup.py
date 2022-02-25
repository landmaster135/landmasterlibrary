from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages

def _requires_from_file(filename):
    return open(filename).read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="landmasterlibrary",
    version="0.0.1",
    description="Convenient tools for me.15",
    author="kinkinnbeer135ml",
    author_email="52403447+landmaster135@users.noreply.github.com",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="git+https://github.com/landmaster135/landmasterlibrary.git",
    # packages=find_packages(where="src"),
    packages=["src"],
    # package_dir={"": "src"},
    package_dir={"src": "landmasterlibrary"},
    # py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    # py_modules=["src"],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # entry_points = {
    #     'console_scripts': ['sample_command = sample_command.sampleCommand:main']
    # },
    python_requires=">=3.7",
    install_requires=_requires_from_file("requirements.txt"),
    setup_requires=["pytest-runner"],
    extras_require={
        "test": ["pytest", "pytest-cov"],
        "doc": ["sphinx"]
    }
)
