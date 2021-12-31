include 4u/prologue.mk

+all\
:
	: $(/4U)
	: $(/..)
	: $(//.)
	: $(./)=$(/.)
