REQ=package-list.txt	# package requirements name
ENV=data-projects		# name of env

# Conda is the package manager for this projects

# ==================================================
# Clean
# ==================================================

.PHONY: clean
clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
	find . -type d -name '*.py[cod]' -exec rm -f {} +
	@echo "Python cache cleaned."

# ==================================================
# Dependencies
# ==================================================

.PHONY: save
save:
	conda list --export > $(REQ)
	@echo "Saved dependencies to $(REQ)."

.PHONY: install
install:
	conda install --file $(REQ)

# ==================================================
# Linting
# ==================================================

.PHONY: format
format:
	ruff format .

.PHONY: lint
lint:
	ruff check .



