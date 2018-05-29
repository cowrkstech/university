#include <pybind11/pybind11.h>

namespace py = pybind11;

int add(int i, int j) {
    return i + j;
}

// filename without quotes
PYBIND11_MODULE(addfunc, m) {
    m.def("add",
    	  &add,
    	  "A function which adds two numbers");
}