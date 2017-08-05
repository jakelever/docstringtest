#!/bin/bash
set -euxo pipefail

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then

	# Install some custom requirements on OS X
	# e.g. brew install pyenv-virtualenv
	brew update
	brew install pyenv-virtualenv

	case "${TOXENV}" in
	py27)
		# Install some custom Python 3.2 requirements on OS X
		pyenv install 2.7.10
		pyenv virtualenv 2.7.10 my-virtual-env-2.7.10
		pyenv activate my-virtual-env-2.7.10
#		brew upgrade python;
#		pip install --upgrade virtualenv
#		python -m venv venv;
#		source venv/bin/activate;
#		pyenv virtualenv -p /usr/local/opt/python/libexec/bin/python2 myenv2
#		pyenv activate myenv2
		;;
	py36)
		pyenv install 3.5.0
		pyenv virtualenv 3.5.0 my-virtual-env-3.5.0
		pyenv activate my-virtual-env-3.5.0
		# Install some custom Python 3.3 requirements on OS X
#		brew install python3;
#		pip3
#		python3 -m venv venv;
#		source venv/bin/activate;
#		pyenv virtualenv -p `which python3` myenv3
#		pyenv activate myenv3
		;;
	esac
else
	# Install some custom requirements on Linux
	done=1
fi

