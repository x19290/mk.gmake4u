+clean/local\
:
ifdef rm/*
	rm $(rm/*)
endif

+clean +clean? +clean!\
:+clean/local

+all\
:$(@@)
