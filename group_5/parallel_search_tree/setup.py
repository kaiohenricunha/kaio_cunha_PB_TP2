from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules = cythonize("parallel_tree_search.pyx", annotate=True,
                            compiler_directives={'language_level': "3"}),
    include_dirs=[np.get_include()],
    extra_compile_args=['-fopenmp'],
    extra_link_args=['-fopenmp'],
)
