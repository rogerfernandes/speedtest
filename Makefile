OS=$(shell uname -s)

run: ## Run speedtest
	python3 speedtest.py
.PHONY: run

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.SILENT: # this has no purpose but to prevent echoing of commands for all targets