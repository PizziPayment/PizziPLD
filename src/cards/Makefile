NAME = cards.md
PYTHON = $(shell which python)
COMPILER_PATH = ./cards_compiler.py

all:
	@echo 'Generating "$(NAME)"...'
	@$(PYTHON) $(COMPILER_PATH)

clean:
	rm -f $(NAME)

.PHONY: all
