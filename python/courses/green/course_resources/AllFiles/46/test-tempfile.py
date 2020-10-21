import os
import shutil
import tempfile
import unittest

class TestTempfile(unittest.TestCase):

    # [Named]TemporaryFile, mkstemp, and mkdtemp guarantee no collisions.  You
    # should use them for all your file and directory needs.
    def test_tempfile(self):
        # [Named]TemporaryFile cleans up its file when the object is destroyed
        file1                  = tempfile.TemporaryFile()
        file2                  = tempfile.NamedTemporaryFile()

        # mkstemp and mkdtemp expect you to clean up after them
        filehandle3, filename3 = tempfile.mkstemp()
        self.addCleanup(os.remove, filename3)
        dirname                = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, dirname)


    # I am not even going to give an example of how to safely generate your own
    # temporary file or directory, because it amounts to re-implementing one of
    # the four objects above.  It is easy to do wrong, and already done right.


    # If you need to know the location of the temporary directory for this
    # worker process for some reason
    def test_tempdir_location(self):
        tempdir_location = tempfile.gettempdir()

    # If you need something to uniquely identify this worker process
    def test_process_id(self):
        process_id = os.getpid()

    # You will usually want to re-use the same external systems for your entire
    # worker process. See the lecture about initializers & finalizers for more
    # information about that.
