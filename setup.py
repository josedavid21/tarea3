from setuptools import setup, find_packages
setup(
	name='PaqueteTarea3',
	version='0.1',
	package_dir= {'PaqueteTarea3':'proyecto'}, 
	packages= find_packages(),
	description='El paquete requerido para la solución de la tarea número 3 del curso microprocesadores y microcontroladores',
	# long_description=open('README.txt').read(),
	scripts= ["proyecto/MetodoSonido.py","proyecto/imagen.py","proyecto/metodo_texto.py"],
	install_requires=['playsound==1.2.2',
	     'pillow>=7.0.0',
	     'tabulate>=0.8.7',
	     'argparse>=1.4.0',
	     'wheel>= 0.35.1'
	      ],
	Python_requires= '>=3',
	    
	url='https://github.com/josedavid21/tarea3',
	author='Mendez, Rojas, Solís, Soto ',
	author_email='cristofhersj@gmail.com, josedavidsz@hotmail.com, mendez.ceciliano@gmail.com'
	) 
