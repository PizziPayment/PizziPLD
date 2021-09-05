NAME = stories.md
COMPILER_PATH = ./user_story_compiler.py
PYTHON = $(shell which python)

all:
	@echo 'Generating "$(NAME)"...'
	@$(PYTHON) $(COMPILER_PATH)

clean:
	rm -f $(NAME)

.PHONY: all
