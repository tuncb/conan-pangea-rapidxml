from conans import ConanFile
from conans.tools import download, unzip
import os

class RapidXmlConan(ConanFile):
    name = "rapidxml"
    version = "1.13"
    license = "http://rapidxml.sourceforge.net/license.txt"
    url = "http://rapidxml.sourceforge.net/"
    description = ("""RapidXml is an attempt to create the fastest XML parser possible, 
        while retaining useability, portability and reasonable W3C compatibility. 
        It is an in-situ parser written in modern C++, 
        with parsing speed approaching that of strlen function executed on the same data.""")

    def package(self):
        url = "https://sourceforge.net/projects/rapidxml/files/rapidxml/rapidxml%201.13/rapidxml-1.13.zip/download"
        zip_name = "rapidxml-1.13.zip"
        download(url, zip_name)
        unzip(zip_name)
        self.copy("*.hpp", dst="rapidxml", src="./rapidxml-1.13")
        os.unlink(zip_name)

    def package_info(self):
        self.cpp_info.includedirs = ['.']
