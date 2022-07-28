## Makefile
##
## Pizzi Payment
## Product Log Document

PANDOC = pandoc
TEMPLATE_PATH = ./template/eisvogel.tex
PDF_ENGINE = tectonic

NAME = pld.pdf
SOURCES_DIR = ./src/
RESOURCE_PATH = .

SOURCES = main.md \
					cards/cards.md \
          user_stories/stories.md \
					conclusion.md


PANDOC_METADATA_OPTIONS = --metadata date="`date -u '+%d / %m / %Y'`"
PANDOC_OPTIONS = -H ./src/lib.latex -s --resource-path $(RESOURCE_PATH) --template $(TEMPLATE_PATH) $(PANDOC_METADATA_OPTIONS)

$(NAME): cards user_stories
	@$(PANDOC) $(addprefix $(SOURCES_DIR), $(SOURCES)) -o $(NAME) --from markdown --pdf-engine $(PDF_ENGINE) $(PANDOC_OPTIONS)

all: $(NAME)

user_stories:
	@make -C ./src/user_stories --no-print-directory

cards:
	@make -C ./src/cards --no-print-directory

clean:
	rm -f $(NAME)
	@make clean -C ./src/user_stories --no-print-directory
