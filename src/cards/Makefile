NAME = cards.md
COMPILER_PATH = ./cards_compiler.py
PYTHON = $(shell which python3)

all:
	@echo 'Generating "$(NAME)"...'
	@$(PYTHON) $(COMPILER_PATH)

clean:
	rm -f $(NAME)

.PHONY: all
