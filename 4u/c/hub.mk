@@	:=$(./)$(??)
include 4u/c/cc.mk

rm/*\
	:=$(sort\
		$(wildcard $(shell sed -n '/^[a-z]/s!^!$(./)!' $(./).gitignore)\
			$(@@) $(**o)\
		)\
	)

include 4u/clean.mk

*/*a\
	:=$(foreach y,$(?*),$(wildcard $(./)../*$y)/lib$y.a)

#{ `=' not `:='
*/@@\
	=$(foreach y,$(?*),$(wildcard $(./)../*$y)/$(yyy))
#}

yyy	:=+clean
*/+clean\
	:=$(*/@@)

yyy	:=+clean?
*/+clean?\
	:=$(*/@@)

yyy	:=+clean!
*/+clean!\
	:=$(*/@@)

+clean\
:$(*/+clean)
+clean?\
:$(*/+clean?)
+clean!\
:$(*/+clean!)

*/*\
	:=$(*/*a) $(*/+clean) $(*/+clean?) $(*/+clean!)
$(*/*)\
:
	$(MAKE) -C$(@D) $(@F)

$(@@)\
:$(*o) $(*/*a)
	gcc --std=gnu99 -g -o $@ $(*o)$(-ld)
