cmake_minimum_required (VERSION 3.5)
project(dummy_proj)

find_package(pybind11 REQUIRED)
pybind11_add_module(addfunc addfunc.cpp)