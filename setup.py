from setuptools import setup
from funkpy import __version__, __name__
setup(
  name=__name__,
  version=__version__,
  packages=[__name__],
  author="Nikolay L. Vaklev",
  license='MIT',
  python_requires='>=3.4'
)
