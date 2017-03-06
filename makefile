.PHONY: clean

clean:
	find . -name '*.pyc' -delete
	find . -name '*.py~' -delete
	find . -name '*.pyo' -delete

all:
	$(shell echo "what" )

default:
	$(ls;pwd;)

register:
	python setup.py register -r pypi

publish:
	python setup.py sdist upload -r pypi

testregister:
	python setup.py register -r pypitest

testpublish:
	python setup.py sdist upload -r pypitest

.PHONY : deploy
deploy:
	python setup.py register -r pypi
	python setup.py sdist --manifest-only -r pypi
	python setup.py sdist --formats zip,gztar upload -r pypi

md2rst:
	pandoc README.md -f markdown -t rst -o README.rst
	cp README.rst index.rst
	cp README.md  docs/README.md
	cp README.rst docs/README.rst
	cp README.rst docs/index.rst