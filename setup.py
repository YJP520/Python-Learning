# - 确定发布的模块(目录结构)
# - setup的编辑工 - - setup()
# - 构建模块 命令行模式 - - python setup.py build
# - 发布模块 - - setup.py sdist

from distutils.core import setup

setup(name='NameOfPackage', version='1.0',author='YJP',
      description='Function of Module.',
      py_modules=['package1.MyMath',])