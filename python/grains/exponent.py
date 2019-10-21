#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def square(n):
    if not 0 < n <= 64:
        raise ValueError("n must be greater than zero.")
    return 2 ** (n - 1)


def total(n):
    if not 0 < n <= 64:
        raise ValueError("n must be greater than zero.")
    return 2 ** n - 1
