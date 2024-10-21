.DEFAULT: help

.PHONY: help
help:
	@ grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: test
test: ## Run all the tests
	@ echo "~~~~ Running tests ~~~~"
	@ poetry run pytest tests
	@ echo ""

.PHONY: black
black:
	@ echo "~~~~ Running black ~~~~"
	@ poetry run black -- .
	@ echo ""

.PHONY: isort
isort:
	@ echo "~~~~ Running isort ~~~~"
	@ poetry run isort .
	@ echo ""

.PHONY: lint
lint: black isort ## Checks and fixes linting with black, isort

.PHONY: check_type
check_type:
	@ echo "~~~~ Running mypy ~~~~"
	@ poetry run mypy --explicit-package-bases
	@ echo ""

.PHONY: tarif
tarif:
	@ poetry run tarif