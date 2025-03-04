from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules = cythonize("parallel_list_sum.pyx", annotate=True, compiler_directives={'language_level': "3"}),
    include_dirs=[np.get_include()],
    extra_compile_args=['-fopenmp'],  # habilita OpenMP
    extra_link_args=['-fopenmp'],
)
