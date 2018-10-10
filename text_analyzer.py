# -*- coding: utf-8 -*-
"""Understanding the use of unittest module library
Created on Thu Aug 16 11:57:03 2018

@author: 130873
"""
import os
import unittest
from analyze_text import *

#def analyze_text(filename):
#    """ return the number of line and charatcter in a file.
#    Args:
#        filename: Name of the file to analyze
#    
#    Raises:
#        IOError: If 'filename' does not exist or cant't be read"
#    
#    Returns:A Tuple where the first element is the number of line present in 
#    the file and the second element is the number of charaters present 
#    in the file
#    """
#    lines = 0
#    chars = 0
#    with open(filename,mode='rt',encoding='utf-8') as f:
#        for line in f:
#            lines += 1
#            chars += len(line)
#            
#    return (lines,chars)
    

class TextAnalysisTests(unittest.TestCase):
    """ tests for the analyze_text() function"""
    def setUp(self):
        """ Fixture that create a file to be used by next method"""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename,mode='wt',encoding='utf-8') as f:
            f.writelines(["testing of unittest module library.\n",
                     "This is the setup fixture where the file gets created.\n",
                     "In the next method call this file would be accessed\n",
                     "In teardown setup method the file would be deleted.\n"])
    
    
    def tearDown(self):
        """Fixture that deletes the created files for unittesting"""
        try:
            os.remove(self.filename)
        except:
            pass        
        
    
    def test_function_runs(self):
        """Basic smoke test: tests whether the function runs or not """
        analyze_text(self.filename)
        
    
    def test_line_count(self):
        """Check that the line count functionality works"""
        self.assertEqual(analyze_text(self.filename)[0],4)
        
        
    def test_character_count(self):
        """Check that the character count is correct"""
        self.assertEqual(analyze_text(self.filename)[1],195)
        
        
    def test_no_such_file(self):
        with self.assertRaises(IOError):
            analyze_text('foobar.txt')
            
            
    def test_no_deletion(self):
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))
        

if __name__ == '__main__':
    unittest.main()
    
