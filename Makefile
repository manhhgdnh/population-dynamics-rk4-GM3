PYTHON ?= python3

figures:
	$(PYTHON) scripts/generate_figures.py

test:
	$(PYTHON) -m unittest discover -s tests -v

lotka:
	$(PYTHON) main.py --model lotka

logistic:
	$(PYTHON) main.py --model logistic
