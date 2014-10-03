#coding:utf-8
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attr):
        print "Encountered a start tag:",tag
    def handle_endtag(self,tag):
        print "Encountered an end tag:",tag
    def handle_data(self,data):
        print "Encountered some data:",data

parser=MyHTMLParser()
parser.feed("<html><head><title>Test</title></head></html><body><h1>Parse me!</h1></body>"
            )