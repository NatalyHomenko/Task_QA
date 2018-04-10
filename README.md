Created by Khomenko Nataliia
Environment: PyCharm
----------------------------------
used re, json, requests libraries
----------------------------------
For running scripts you need:

-open cmd(command line interpreter)
-move to folder with scripts
-run command: pytest test.py

---------------------------------
Also project contain next files:

1.serverAPI
contain methods that implement current API

2.test.py
contain test methods. Methods verifies that data is added to server.

3.testHelper
contain methods that verifies correctness of returned response codes.

4.datamining
this script calculates % of successful requests per hour from file dataminung.log and store answer in file "result"

