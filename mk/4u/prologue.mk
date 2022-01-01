+all .SUFFIXES\
:

#{
# differ from $(PWD) sometimes
pwd	:=$(shell pwd)
#}

#{
# conventions
#	*.	path
#	*/	prefix (empty sometimes)
#	/*	absolute sometimes

#{
# project root.
# relative to the first GNUmakefile, not $(PWD):
#	/.	relative mostly
#	//.	absolute always
./	:=$(dir $(firstword $(MAKEFILE_LIST)))
ifeq '$(./)' './'
./	:=
endif
/.	:=$(shell 0relpath $(./).)
ifneq '$(/.)' '.'
	./	:=$(/.)/
endif
//.	:=$(shell cd $(/.); pwd)
#}

#{
# interproject root.
# relative to the first GNUmakefile, not $(PWD):
#	... relative mostly
#	/.. absolute always
...	:=$(shell 0relpath $(./)..)
/..	:=$(shell cd $(...); pwd)
ifeq '$(/..)' '/'
../	:=/
else
../	:=$(...)/
endif
#}

#}conventions

# project name
?.	:=$(notdir $(//.))

# project stem
??	:=$(?.:3%=%)
??	:=$(??:c.%=%)
??	:=$(??:lib%=%)

+remake\
:+clean! +all
