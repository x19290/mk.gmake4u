# master project
ifdef ??/
	/??	:=$(??/:%/=%)
else
	/??	:=$(/.)
	??/	:=$(./)
endif
-include $(??/)?config.mk

**c	:=$(wildcard $(./)*.c $(./)*/*.c)
*c	:=$(filter-out $(./)test%,$(**c))
**o	:=$(**c:%.c=%.o)
*o	:=$(*c:%.c=%.o)

-I.	:=$() -I$(/.)
ifneq '$(/??)' '$(/.)'
-I.	+=-I$(/??)
endif

yyy	:=$(foreach y,$(?*),-L$(shell 0relpath $(wildcard $(./)../*$y)))
ifdef yyy
-L/*\
	:=$() $(yyy)
endif

yyy	:=$(foreach y,$(?*),-I$(shell 0relpath $(wildcard $(./)../*$y)))
ifdef yyy
-I/*\
	:=$() $(yyy)
-l/*\
	:=$() $(?*:%=-l%)
endif

-cc	:=$(-I.)$(-I/*)$(-E)
-ld	:=$(-L/*)$(-l/*)$(-l)

$(*o)\
:%.o	:%.c $(MAKEFILE_LIST)
	gcc --std=gnu99 -Wno-multichar -g -c$(-cc) -o $@ $*.c
