#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :__init__.py.py
# @Time      :2024/7/29 
# @Author    :SophistGuaPi

import pathlib
import tomli

path = pathlib.Path(__file__).parent / "conf.toml"
with path.open(mode="rb") as fp:
    conf = tomli.load(fp)

if __name__ == "__main__":
    pass
