#!/usr/bin/make -f
# -*- mode:makefile -*-

SRC=$(wildcard *.py)

all:   	$(SRC:.py=.rtf)

%.rtf %.html: %.py
	highlight --style edit-emacs -o $@ -i $<

print:
	for i in `ls *.py`; do \
	   a2ps $$i; \
	done

test:
	nosetests3 -v test/test.py

generate-certs:
	openssl req -x509 -newkey rsa:4096 -keyout ca-key.pem -out ca-cert.pem -days 365 -nodes -subj "/CN=MyCA"
	openssl req -newkey rsa:4096 -keyout server-key.pem -out server-req.pem -nodes -subj "/CN=localhost"
	openssl x509 -req -in server-req.pem -CA ca-cert.pem -CAkey ca-key.pem -CAcreateserial -out server-cert.pem -days 365


clean:
	$(RM) *~ *.pyc $(SRC:.py=.html) *.rtf
	$(RM) *.pem
