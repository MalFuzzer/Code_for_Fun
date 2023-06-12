#!/bin/bash

apt install strace -y

strace locate *.txt &> out.txt
grep -ir db out.txt
