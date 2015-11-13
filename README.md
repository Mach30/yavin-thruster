Unit Tests
----------
Unit tests can be executed by using python's built-in unit test discovery and 
execution. Simply execute `python -m unittest discover`

The CAD tests in test_cad.py will be automatically skipped if run with a Python
version > 2.7.  This is because the current versions of the FreeCAD library do 
not support Python 3.x.
