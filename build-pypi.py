import os
from shutil import rmtree, move
from glob import glob

PACKAGE_NAME = "funkpy"

os.system("python3 setup.py sdist bdist_wheel")
rmtree("./" + PACKAGE_NAME + ".egg-info")
rmtree("./build")
os.system('python3 -m twine upload --repository-url "https://test.pypi.org/legacy/" "dist/*"')
