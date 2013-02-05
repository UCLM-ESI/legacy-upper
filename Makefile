
SRC=$(wildcard *.py)

all:   	$(SRC:.py=.rtf)

%.rtf: %.py
	highlight -R --style emacs $< -o $@

%.html: %.py
	highlight -X --style emacs $< -o $@

print:
	for i in `ls *.py`; do \
	   a2ps $$i; \
	done

clean:
	$(RM) *~ *.pyc *.html *.rtf
