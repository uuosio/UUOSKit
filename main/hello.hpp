/*
 * hello.hpp
 *
 *  Created on: Oct 8, 2018
 *      Author: newworld
 */

#ifndef MAIN_HELLO_HPP_
#define MAIN_HELLO_HPP_

#include <Python.h>

PyObject* init_wallet();
PyObject* init__uuosapi();

extern "C" {
   PyObject* PyInit_wallet();
   PyObject* PyInit__uuosapi();
   PyObject* PyInit_pyobject();
   PyObject* PyInit_block_log();
}

#endif /* MAIN_HELLO_HPP_ */
