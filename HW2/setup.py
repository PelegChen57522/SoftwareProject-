from setuptools import Extension, setup

module = Extension("kmeanssp", sources=['kmeansmodule.c'])
setup(name='kmeanssp',
     version='1.0',
     description='K-means clustering extension module',
     ext_modules=[module])
