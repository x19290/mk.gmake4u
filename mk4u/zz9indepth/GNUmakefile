include 4u/prologue.mk

# must be sync with .gitignore
hub	:=id3edit
lib	:=libprinthex
**	:=$(hub) $(lib)

+clean:
	rm -rf $(**)

*/+fetch\
:=$(foreach y,$(**),$(./)$y/+fetch)
*/+fix\
:=$(foreach y,$(**),$(./)$y/+fix)
*/stamp\
:=$(foreach y,$(**),$(./)$y/GNUmakefile)

from/github\
=git://github.com/$(author)/$(@D).git

$(hub)/+fetch:\
tag=v2.1.2
$(hub)/+fetch:\
author\
:=rstemmer
$(hub)/+fetch:\
from\
=$(from/github)

$(lib)/+fetch:\
tag=v1.0.1
$(lib)/+fetch:\
author\
:=rstemmer
$(lib)/+fetch:\
from\
=$(from/github)

$(*/+fetch)\
:
	rm -rf $(@D)
	git -C $(/.) clone $(from)
	git -C $(./)$(@D) reset --hard $(tag)

+fetch\
:$(*/+fetch)

$(*/+fix)\
:$(@D)/GNUmakefile

+fix\
:$(*/stamp)

/fix\
=$(./)0fix/$(notdir $(@D))

*cp\
=$(wildcard $(/fix)/0cp/*)
*patch\
=$(wildcard $(/fix)/1patch/*)

$(*/stamp)\
:
	[ '$(*cp)' ] && cp $(/fix)/0cp/* $(@D) || :
	[ '$(*patch)' ] && cat $(/fix)/1patch/* | patch -p1 -d$(@D) || :

# demo
+all\
:
	$(MAKE) +fetch  # made always
	$(MAKE) +fix  # made always
	$(MAKE) +fix  # made not
	$(MAKE) -C $(./)$(hub)  # made always
