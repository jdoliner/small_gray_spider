import urllib2 as url
import re

class sgs:

    def __init__(self, base_url):
        self.base_url = base_url
        self.list_of_code = []
        self.already_visited = [self.base_url]
        
        self.list_of_code = [url.urlopen(self.base_url).read()]
        self.first_conn = self._get_first_connections_urls(self.list_of_code[0])
        

    def _get_first_connections_urls(self, _source_url):
        """Returns all of the urls given by any <a> tag in the _source_url."""

        pattern = r"""(<a href=.)(.*?)(['"])"""
        _list = re.findall(pattern, _source_url)
        _list_urls = [item[1] for item in _list]
        return _list_urls
        

    def _get_first_connections_code(self, _list_urls):       
        """Adds the source code for every element in _list_urls if
            it has not already been added."""    
        if (type(_list_urls) == type("")):
            _list_urls = [_list_urls]

        for addr in _list_urls:
            if addr in self.already_visited: pass
            else:                
                try: 
                    self.list_of_code.append(url.urlopen(addr).read())
                    self.already_visited.append(addr)
                except: pass

############################            
         
k = sgs("https://news.ycombinator.com/news")

def get_title(_list):
    biglist = []
    for i in _list:
        k = re.findall(r"(<head>.*?<title>)(.*?)(</)", i, re.DOTALL)
        biglist += [i[1] for i in k]
    return biglist
    
# Example.
#k._get_first_connections_code(k.first_conn)
#r = get_title(k.list_of_code)
#for item in r: print item
