#from future.utils import iteritems
import sys
sys.path.insert(0,"/home/psimen/anaconda3/lib/python3.6/site-packages")
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


ext = [Extension('HysterisisMM',
                sources=['HysterisisMM.pyx'],
                library_dirs=['/usr/local/cuda-9.1/lib64', '/home/thomasnemeh/SimenWinterTerm2019/Hysterisis_Cuda_Programs/Updated_MM'],
                libraries=['cudart', 'HysterisisMM'],
                language='c++',
                runtime_library_dirs=['/usr/local/cuda-9.1/lib64', '/home/thomasnemeh/SimenWinterTerm2019/Hysterisis_Cuda_Programs/Updated_MM'],
                include_dirs = ['/home/psimen/anaconda3/lib/python3.6/site-packages/Cython/Includes', '/usr/local/cuda-9.1/include', '/home/psimen/anaconda3/lib/python3.6/site-packages/numpy/core/include'])]


setup(name='HysterisisMM',
	  cmdclass = {'build_ext': build_ext},
      ext_modules = ext)