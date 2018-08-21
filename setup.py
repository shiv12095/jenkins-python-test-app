from setuptools import setup, find_packages

requirements = []

test_requirements=[]

setup(
	name='app',
	packages=['app'],
	version='0.0.1',
	author='Shiv Kandikuppa',
    url ='https://github.com/shiv12095/mapviz',
	packages=find_packages(),
	install_requires=requirements,
	zip_safe=False
)
