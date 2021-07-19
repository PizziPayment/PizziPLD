## Makefile
##
## Pizzi Payment
## Product Log Document

PANDOC = pandoc
TEMPLATE_PATH = ./template/eisvogel.tex
PDF_ENGINE = tectonic

NAME = pld.pdf
SOURCES_DIR = ./src/
SOURCES = main.md

PANDOC_METADATA_OPTIONS = --metadata date="`date -u '+%d / %m / %Y'`"
PANDOC_OPTIONS = --resource-path $(RESOURCE_PATH) --listings --template $(TEMPLATE_PATH) $(PANDOC_METADATA_OPTIONS)

all:
	$(PANDOC) $(addprefix $(SOURCES_DIR), $(SOURCES)) -o $(NAME) --from markdown --pdf-engine $(PDF_ENGINE) $(PANDOC_OPTIONS)

