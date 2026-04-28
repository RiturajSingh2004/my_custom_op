from setuptools import setup
from torch.utils.cpp_extension import CppExtension, BuildExtension

setup(
    name='my_custom_op',
    ext_modules=[
        CppExtension(
            name='my_custom_op',
            sources=['custom_op.cpp'],
        ),
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)