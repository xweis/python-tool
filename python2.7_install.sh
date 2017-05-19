#!/bin/bash

wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz
tar zxf Python-2.7.12.tgz
cd Python-2.7.12 && ./configure
make -j 5
make install
cd ..
wget http://pypi.doubanio.com/packages/87/ba/54197971d107bc06f5f3fbdc0d728a7ae0b10cafca46acfddba65a0899d8/setuptools-27.2.0.tar.gz
tar zxf setuptools-27.2.0.tar.gz
cd setuptools-27.2.0 && python2.7 setup.py install
python2.7 easy_install.py pip
mv /usr/bin/python /usr/bin/python.old && ln -s /usr/local/bin/python2.7 /usr/bin/python 
pip install supervisor
echo_supervisord_conf > /etc/supervisord.conf
