Documentation
-------------
The documentation for things like calculations is done using Mach 30's 
Mathematics ToolKit (MTK). This documentation is available in its raw format
under the documentation directory. These can easily be viewed by launching MTK
from within the root directory, and then within MTK navigating to the 
documentation directory.

Unit Tests
----------
Unit tests can be executed by using python's built-in unit test discovery and 
execution. Simply execute `python -m unittest discover`

The CAD tests in test_cad.py will be automatically skipped if run with a Python
version > 2.7.  This is because the current versions of the FreeCAD library do 
not support Python 3.x.
