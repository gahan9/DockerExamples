# This file creates executable from script main.py to generate artifact

__author__ = "Gahan Saraiya"

try:
    from setuptools import setup, find_packages, Extension
except ImportError:
    from distutils.core import setup, find_packages, Extension

from Cython.distutils import build_ext
import numpy as np

ext_modules = [Extension("main",["main.pyx"])]



def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='Publish_Artifact',
    cmdclass = {'build_ext': build_ext},
    version='1.0',
    description='Publish Artifact',
    author='Gahan Saraiya',
    long_description=readme(),
    include_dirs = [np.get_include()],
    ext_modules = ext_modules,
)

