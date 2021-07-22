NAME = stories.md
PYTHON = $(shell which python)
COMPILER_PATH = ./user_story_compiler.py

all: $(NAME)

$(NAME):
	@echo 'Generating "$@"...'
	@$(PYTHON) $(COMPILER_PATH)

clean:
	rm -f $(NAME)

.PHONY: all
