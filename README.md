# WebCrawler
##A basic Python web crawler.


### MAIN FUNCTIONS / FEATURES
###### crawl_web(seed)
- given a seed page, create index of all links and create a relational graph between the pages

###### compute_ranks(graph)
- computes ranks of a given webpage using inlinks/outlinks

###### lucky_search(index, ranks, keyword)
- returns the highest ranked page off a given keyword 

###### lookup(index, keyword)
- returns a list of all the url's associated with the given keyword


### BUGS
###### get_page(page)
- only works with 3 specific url's so far
- update to work on any URL (using Beautiful Soup to parse HTML)
 
