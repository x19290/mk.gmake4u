@@	:=$(./)lib$(??).a
include 4u/c/cc.mk

rm/*\
 	:=$(wildcard $(shell grep '^[a-z]' $(./).gitignore) $(@@) $(**o))
include 4u/clean.mk

$(@@)\
:$(*o)
	ar r $@ $(*o) 2> /dev/null
