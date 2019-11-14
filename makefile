

a:
	python .

setup:
	@ python -m pip show pyme || echo 1
	#python -m pip install pygame