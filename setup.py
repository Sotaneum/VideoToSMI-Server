from setuptools import setup, find_packages

setup(name='videotosmi-server',
      version='0.0.1',
      url='https://github.com/Sotaneum/VideoToSMI-Server',
      author='Donggun LEE',
      author_email='gnyotnu39@gmail.com',
      description='Create a smi file in Web based on the video',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False,
      setup_requires=['deepgeo','videotosmi','confighelper','tensorflow-gpu==1.9.0','exifread','piexif','pillow','matplotlib','scikit-image','IPython','keras','cython'],
      classifiers=[
          'License :: OSI Approved :: MIT License'
      ]
     )
