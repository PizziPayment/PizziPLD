NAME = cards.md
COMPILER_PATH = ./cards_compiler.py
PYTHON = $(shell which python3)

all:
	@echo 'Generating "$(NAME)"...'
	echo '$PYTHON -> ' $(PYTHON)
	which python
	which python3
	@$(PYTHON) $(COMPILER_PATH)

clean:
	rm -f $(NAME)

.PHONY: all
