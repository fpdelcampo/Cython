from setuptools import setup
from Cython.Build import cythonize
import Cython
print(Cython)
setup(
    ext_modules = cythonize("./hello_world.pyx")
)