python2: c_unpack.pyx
	cythonize -2 -i c_unpack.pyx

python3: c_unpack.pyx
	cythonize -3 -i c_unpack.pyx
