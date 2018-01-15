clean-pycache:
	find . -type d -name __pycache__ -delete

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .cache

clean: clean-pycache clean-build