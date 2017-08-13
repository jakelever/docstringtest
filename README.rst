=============
docstringtest
=============

|pypi| |build-status| |coverage| |docs| |license|

.. |pypi| image:: https://img.shields.io/pypi/v/docstringtest.svg
   :target: https://pypi.python.org/pypi/docstringtest
   :alt: PyPI Release
   
.. |build-status| image:: https://travis-ci.org/jakelever/docstringtest.svg?branch=master
   :target: https://travis-ci.org/jakelever/docstringtest
   :alt: Travis CI status

.. |coverage| image:: https://coveralls.io/repos/github/jakelever/docstringtest/badge.svg?branch=master
   :target: https://coveralls.io/github/jakelever/docstringtest?branch=master
   :alt: Coverage status
   
.. |docs| image:: https://readthedocs.org/projects/docstringtest/badge/
   :target: http://docstringtest.readthedocs.io/
   :alt: Documentation status
   
.. |license| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT
   :alt: MIT license

docstringtest is a small package for regression testing of docstrings in Python code. It checks that all appropriate methods and functions are using ReST docstrings with parameter information so that nice documentation can be generated. This format looks like:

.. code-block:: python

   def example_function(varA,varB):
      """
      This function does nothing

      :param varA: The first variable
      :param varB: The second variable
      :type varA: The type of the first variable
      :type varB: The type of the second variable
      """
      pass

It makes it easy to check that the docstrings match with the current parameters so that documentation doesn't become out-of-step with the code. 

If you wanted to add docstringtest to a standard test algorithm, it would simply be something like this

.. code:: python

        import mymodule
        import docstringtest

        def test_docstringtest():
                docstringtest.testModule(mymodule)

Installation
------------

You can install "docstringtest" via `pip`_ from `PyPI`_::

   $ pip install docstringtest
   

Contributing
------------
Contributions are very welcome.

License
-------

Distributed under the terms of the `MIT`_ license, "docstringtest" is free and open source software

Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.


.. _`MIT`: http://opensource.org/licenses/MIT
.. _`file an issue`: https://github.com/jakelever/docstringtest/issues
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi
