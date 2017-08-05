#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then

	# Install some custom requirements on OS X
	# e.g. brew install pyenv-virtualenv
	brew install pyenv-virtualenv

	case "${TOXENV}" in
	py27)
		# Install some custom Python 3.2 requirements on OS X
		pyenv virtualenv 2.7.10 my-virtual-env-2.7.10
		pyenv activate my-virtual-env-2.7.10
		;;
	py36)
		# Install some custom Python 3.3 requirements on OS X
		;;
	esac
else
	# Install some custom requirements on Linux
fi

