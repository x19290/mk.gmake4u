$(eval $(shell 0has endian.h))
ifndef endian.h
	-fix?endian\
		:=-fix
endif
-E	+=--include=endian$(-fix?endian).h
ifdef -E
	-E	:=$() $(-E)
endif

-l	:=$() -lz
$(foreach y,$(shell 0has --libs z iconv),$(eval $y))
ifndef -lz
$(error missing -lz)
endif
ifdef -liconv
-l	+=-liconv
endif
