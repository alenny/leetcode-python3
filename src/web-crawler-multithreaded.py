# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

import threading

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        domainEnd = startUrl.find('/', 7)
        domain = startUrl[:domainEnd] if domainEnd >= 0 else startUrl
        
        def IsSameDomain(url: str):
            return url.startswith(domain)

        urls = [startUrl]
        ret = set(urls)
        retLock = threading.Lock()

        def crawl(url, nextUrls):
            foundUrls = htmlParser.getUrls(url)
            retLock.acquire()
            try:
                for u in foundUrls:
                    if not u in ret and IsSameDomain(u):
                        nextUrls.append(u)
                        ret.add(u)
            finally:
                retLock.release()

        while urls:
            nextUrls = []
            jobs = []
            for url in urls:
                job = threading.Thread(target=crawl, args=(url, nextUrls))
                job.start()
                jobs.append(job)
            for job in jobs:
                job.join()
            urls = nextUrls
        return list(ret)