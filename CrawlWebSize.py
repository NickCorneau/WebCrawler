def crawl_web(seed, max_pages):
    tocrawl = [seed]
    crawled = []
	
    while tocrawl:	
        if (len(crawled) >= max_pages):
            return crawled			
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
			
    return crawled