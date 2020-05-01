from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='package_name',
      version='0.0.1',
      description='Template repository for python packages with an command line interface.',
      long_description = readme(),
      long_description_content_type='text/markdown',
      keywords='python template',
      url='http://github.com/temken/template_python',
      author='author',
      author_email='email@address.com',
      license='MIT',
      packages=['package_name'],
      install_requires=[
          'argparse'
      ],
      entry_points = {
        'console_scripts': ['package_command=package_name.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)