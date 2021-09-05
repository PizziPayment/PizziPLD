NAME = cards.md
COMPILER_PATH = ./cards_compiler.py
PYTHON = $(shell which python)

all:
	@echo 'Generating "$(NAME)"...'
	echo $(PYTHON)
	@$(PYTHON) $(COMPILER_PATH)

clean:
	rm -f $(NAME)

.PHONY: all
