#!/usr/bin/env bash
set -e
# see also ".mailmap" for how email addresses and names are deduplicated
{
	cat <<- 'EOH'
		# This file lists all individuals contributed content to the repository.
		# For the AirBnB projects.
	EOH
	echo
	git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} > AUTHORS
