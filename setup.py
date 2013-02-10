from setuptools import setup

setup(name='fakelbst',
      version='1.0',
      description='OpenShift App',
      author='Yijie Mao',
      author_email='example@example.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['Flask==0.9', 'uWsgi', 'flask_mongoengine', 'BeautifulSoup'],
     )
