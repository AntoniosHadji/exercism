#!/usr/bin/env bash
# -*- coding: utf-8 -*-
for j in saddle_points{_v0,_v1};
  do echo $j;
  for i in 10 50 100 200 300;
    do echo -n "$i   ";
    python3 -m timeit -s "from first_attempts import ${j} as saddle_points; x=[[i for i in range(${i})] for j in range(${i})]" "saddle_points(x)";
  done;
done
