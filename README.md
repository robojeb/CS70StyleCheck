OpenStyleCheck
==============

A library for building extensible style checking scripts. It is designed to be
able to be extended to more languages in the future.

Supported Languages
---
  * C++

Installation
---
 1. Pull OpenStyleCheck from the github and add the OpenSC directory location to
your PYTHONPATH environment variable
 2. Install clang, and the libclang libraries
 3. Install python bindings for the version of clang you installed. The command
 to do this is `sudo pip install clang==#.#`
 4. Inside your script set the variable `CheckFile.LIB_CLANG_PATH` to the
 location of `libclang.so` on your machine.
