#!/bin/bash

dirPath=${0%/*}
pyrcc5 -o "$dirPath/resources_rc.py" "$dirPath/resources.qrc"