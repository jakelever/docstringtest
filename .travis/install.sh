#!/bin/bash
set -euxo pipefail

echo "travis_fold:start:SCRIPT folding starts"
if [[ $TRAVIS_OS_NAME == 'osx' ]]; then

	# Install some custom requirements on OS X
	# e.g. brew install pyenv-virtualenv

	brew update
#	brew install pyenv-virtualenv
#	eval "$(pyenv init -)"
#	eval "$(pyenv virtualenv-init -)"

	case "${TOXENV}" in
	py27)
		# Install some custom Python 3.2 requirements on OS X
#		pyenv install 2.7.10
#		pyenv virtualenv 2.7.10 my-virtual-env-2.7.10
#		pyenv activate my-virtual-env-2.7.10
		brew upgrade python;
#		pip install --upgrade virtualenv
#		python -m venv venv;
#		source venv/bin/activate;
#		pyenv virtualenv -p /usr/local/opt/python/libexec/bin/python2 myenv2
#		pyenv activate myenv2
		pip2 install --upgrade virtualenv
		virtualenv env2 -p python2
		PS=${PS:=} source env2/bin/activate
		;;
	py36)
#		pyenv install 3.5.0
#		pyenv virtualenv 3.5.0 my-virtual-env-3.5.0
#		pyenv activate my-virtual-env-3.5.0
		# Install some custom Python 3.3 requirements on OS X
		brew install python3;
#		pip3
#		python3 -m venv venv;
#		source venv/bin/activate;
#		pyenv virtualenv -p `which python3` myenv3
#		pyenv activate myenv3
		pip3 install --upgrade virtualenv
		virtualenv env3 -p python3
		PS=${PS:=} source env3/bin/activate
		;;
	esac
else
	# Install some custom requirements on Linux
	done=1
fi
echo "travis_fold:end:SCRIPT folding ends"

