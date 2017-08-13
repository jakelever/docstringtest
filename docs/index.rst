Welcome to docstringtest documentation!
=======================================

.. currentmodule:: docstringtest

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

Testing
-------

These methods will test a module/class or function to check that all functions contain the appropriately formatted docstrings. If not they will raise a DocstringTestError

.. autofunction:: testModule
.. autofunction:: testClass
.. autofunction:: testFunction

The Error generated for a failed docstring will be of the following class:

.. autoclass:: DocstringTestError

Generation
----------
These functions help to create docstrings for functions. They will provide strings for skeleton docstrings for an individual function or all the functions in a module/class.

.. autofunction:: generateDocstring
.. autofunction:: generateAllDocstrings


