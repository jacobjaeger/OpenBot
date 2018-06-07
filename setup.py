from setuptools import setup

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='Discord OpenBot',
      version='0.1.4',
      description='Simple Custom Bots and Plugins for discord.py',
      author='jcb1317',
      packages=['openbot'],
      license='MIT',
      install_requires=requirements,
      classifiers=[
          "Development Status :: 3 - Alpha",
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3.6",
          "Topic :: Communications :: Chat",
          "Topic :: Software Development :: Libraries :: Python Modules"
      ]
      )

