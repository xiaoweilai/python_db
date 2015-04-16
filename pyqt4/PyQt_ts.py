#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8

import sys
from PyQt4.QtGui import QApplication, QPushButton
app = QApplication(sys.argv)
button = QPushButton("Hello world!")
button.show()
sys.exit(app.exec_())