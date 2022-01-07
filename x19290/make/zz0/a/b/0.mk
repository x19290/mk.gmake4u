include 4u/prologue.mk

+all\
:
	: $(/MK)
	: $(/..)
	: $(//.)
	: $(./)=$(/.)
