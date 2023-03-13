from setuptools import setup

setup(name='fclener',
      packages=['fclener'],
      entry_points={'console_scripts': ['fclen = fclener.fclener_sorter:main']}
      )

