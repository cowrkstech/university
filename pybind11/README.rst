COMPILE WITH CMAKE
==================
::

  sudo apt install python3-dev cmake
  conda install pybind11 -c conda-forge
  gcc --version > 4.7

cmake .

make


COMPILE WITH GCC
================
::

  sudo apt install python3-dev cmake
  pip install pybind11
  gcc --version > 4.7

Ubuntu:
-------
gcc -O3 -shared -std=c++11 -fPIC $(python -m pybind11 --includes) XXXXX.cpp -o XXXXX$(python3-config --extension-suffix)

Mac:
----
gcc -O3 -shared -std=c++11 -fPIC $(python -m pybind11 --includes) XXXXX.cpp -o XXXXX$(python3-config --extension-suffix) -undefined dynamic_lookup


Video
=====
https://youtu.be/jQedHfF1Jfw


CPP reference
=============
http://www.cplusplus.com/reference


Usages
======
- GIL
- Cpp to python
- Garbage Collector
- Reference counter
- Static types
- Overloading
- Custom data structures
- Instance, static funcs, variables
- Custom Exceptions
- Callbacks
- Custom operators
- STL data structures
- Virtual methods in python