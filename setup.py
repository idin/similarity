
from setuptools import setup, find_packages

setup(
	name='similarity',
	version='0.0.1',
	description='Python library for measuring string similarity',
	url='https://github.com/idin/similarity',
	author='Idin',
	author_email='py@idin.ca',
	license='MIT',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Programming Language :: Python :: 3 :: Only',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Topic :: Software Development :: Libraries :: Python Modules'
	],
	packages=find_packages(exclude=["jupyter_tests", ".idea", ".git"]),
	install_requires=[
		'editdistance', 'jellyfish', 'numpy', 'interaction'
	],
	python_requires='~=3.6',
	zip_safe=False
)
