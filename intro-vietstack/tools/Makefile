SVGDOCS = ../images/releases.svg
MDDOCS = ../programs.md

all: $(SVGDOCS) $(MDDOCS)

../images/releases.svg: programs.yaml
	sh plot-releases.sh $@

../programs.md: programs.yaml
	python release-programs.py -m programs.yaml icehouse > $@ || rm -f $@

