run: 
	twistd -n twsrs

cov: 
	coverage run --branch --source talkback  `which trial` tests
	coverage report
	coverage html
	google-chrome htmlcov/index.html
.PHONY: run cov
