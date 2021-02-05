from setuptools import setup

setup(
  name    = "Hardware",
  version = "0.0.1",
  install_requires =[
    "scipy",
    "numpy>=1.15.0"
    "matplotlib"
    "lmfit",
    "pyside2",
    "pyvisa",
    "pandas",
    "pyqtgraph",
    "nidaqmx",],
 description= "Tools for controlling a equipment in Goldsmith lab",
 long_description=read("README.md"),
 authors="Brandon Mehlenbacher",
 license="MIT",
 classifiers=[
   "Intended Audience :: Science/Research",
   "License :: OSI Approved :: MIT License",
   "Natural Language :: English",
   "Programming Language :: Python :: 3",
   "Programming Language :: Python :: 3.7",
   "Programming Language :: Python :: 3.8",
   "Topic :: Scientific/Engineering",]
)
    
