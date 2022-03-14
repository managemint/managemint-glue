from distutils.core import setup
import setuptools

setup(
    name='hansible-glue',
    version='0.1.0',
    author="Jonas Gunz",
    author_mail="himself@jonasgunz.de",
    description="Python glue for hansible",
    packages=setuptools.find_packages(),
    install_requires=[
        "ansible>=2.12",
    ],
    license='GPL3',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)

