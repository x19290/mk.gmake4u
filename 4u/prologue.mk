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
# project root:
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
# interproject root
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

#{
# macro:
#	+project-roots := +project-root ~ +/interproject-root
# targets:
#	+projects: $(+project-roots)
#	+project-root ~ +/interproject-root
+project-roots\
	:=$(foreach y,+ +/ +inter +/inter,$yproject-root)

+projects\
:$(+project-roots)

$(+project-roots)\
:
	: $@
	: $(+root)
	:

+project-root\
:+root\
	:=$(/.)
+/project-root\
:+root\
	:=$(//.)
+interproject-root\
:+root\
	:=$(...)
+/interproject-root\
:+root\
	:=$(/..)
#}

+remake\
:+clean! +all
