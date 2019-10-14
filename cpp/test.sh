#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# touch $(basename $(pwd)).cpp
mkdir -p build
cd build || return
cmake -G "Unix Makefiles" ..
make
cd ../ || return
# rm -rf build
