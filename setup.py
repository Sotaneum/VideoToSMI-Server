from setuptools import setup, find_packages

setup(name='videotosmi-server',
      version='0.0.1',
      url='https://github.com/Sotaneum/VideoToSMI-Server',
      author='Donggun LEE',
      author_email='gnyotnu39@gmail.com',
      description='Create a smi file in Web based on the video',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      zip_safe=False,
<<<<<<< HEAD
      setup_requires=['deepgeo','videotosmi','confighelper'],
      classifiers=[
          'License :: OSI Approved :: MIT License'
      ]
     )
=======
      setup_requires=['deepgeo','videotosmi','confighelper','tensorflow-gpu==1.9.0','exifread','piexif','pillow','matplotlib','scikit-image','IPython','keras','cython'],
      classifiers=[
          'License :: OSI Approved :: MIT License'
      ]
     )
>>>>>>> 80dacef53020ed35ccba091b257654f34bdbd5b0
