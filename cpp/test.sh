#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# touch $(basename $(pwd)).cpp
mkdir -p build
cd build
cmake -G "Unix Makefiles" ..
make
cd ../
rm -rf build
