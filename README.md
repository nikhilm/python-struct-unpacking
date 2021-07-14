Small experiment comparing time to deserialize a simple, fixed-width, 4 uint64 C struct using the struct module.

Compares Python and Cython.

Clone the repo, then:

On Python 3:
```
python3 -m venv py3env
source py3env/bin/activate
python3 -m pip install cython
make python3
python2 main.py
```

On Python 2:
```
sudo apt install python-virtualenv  # (or similar to get virtualenv)
python2 -m virtualenv py2env
source py2env/bin/activate
python2 -m pip install cython
make python2
python2 main.py
```

Some results on a Pixelbook

Python 3:
```
---------------------------------------------
Test Name                      Time (s)
---------------------------------------------
plain unpack()                 0.323
plain unpack_from()            0.350 (+108.31%)
cython unpack()                0.244 (+75.66%)
cython unpack_from()           0.246 (+76.11%)
cython typed unpack()          0.698 (+216.30%)
plain compiled unpack()        0.283 (+87.80%)
cython compiled unpack()       0.225 (+69.68%)
```

Python 2:
```
---------------------------------------------
Test Name                      Time (s)
---------------------------------------------
plain unpack()                 0.456
plain unpack_from()            0.481 (+105.42%)
cython unpack()                0.377 (+82.70%)
cython unpack_from()           0.401 (+87.99%)
cython typed unpack()          1.119 (+245.40%)
plain compiled unpack()        0.434 (+95.26%)
cython compiled unpack()       0.342 (+75.01%)
```
