#!/usr/bin/env bash

# Works like zz0smoke_t.py.
# Just for your information.

set +x
set -eu

declare -r layout <<'!'
zz0/
	0.mk
	a/
		b/
			0.mk

Both 0.mk look like:
include 4u/prologue.mk

+all\
:
        : $(/4U)
        : $(/..)
        : $(//.)
        : $(./)=$(/.)
!

function you-can/run/this-script/on-any-dir ()
{
	if [[ $0 == */* ]]; then
		declare -r dir=${0%/*}
		if [[ $(cd "$dir"; pwd) != $PWD ]]; then
			set -x
			cd "$dir"
		else
			set -x
		fi
	else
		set -x
	fi
}

you-can/run/this-script/on-any-dir

# following are the results from the author's environment:
mk4u -Czz0 -f0.mk
: /Users/h2/Projects/mk.gmake4u
: /Users/h2/Projects/mk.gmake4u/mk4u
: /Users/h2/Projects/mk.gmake4u/mk4u/zz0
: =.
mk4u -Czz0/a -f../0.mk
: /Users/h2/Projects/mk.gmake4u
: /Users/h2/Projects/mk.gmake4u/mk4u
: /Users/h2/Projects/mk.gmake4u/mk4u/zz0
: ../=..
mk4u -Czz0/a -fb/0.mk
: /Users/h2/Projects/mk.gmake4u
: /Users/h2/Projects/mk.gmake4u/mk4u/zz0/a
: /Users/h2/Projects/mk.gmake4u/mk4u/zz0/a/b
: b/=b
mk4u -Czz0/a/b -f../../0.mk
: /Users/h2/Projects/mk.gmake4u
: /Users/h2/Projects/mk.gmake4u/mk4u
: /Users/h2/Projects/mk.gmake4u/mk4u/zz0
: ../../=../..
mk4u -Czz0/a/b -f0.mk
: /Users/h2/Projects/mk.gmake4u
: /Users/h2/Projects/mk.gmake4u/mk4u/zz0/a
: /Users/h2/Projects/mk.gmake4u/mk4u/zz0/a/b
: =.
