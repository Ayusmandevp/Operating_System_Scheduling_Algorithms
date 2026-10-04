def lru_page_replacement(pages, capacity):
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) == capacity:
                memory.pop(0) # Remove the least recently used (front)
            memory.append(page)
            page_faults += 1
            print(f"Page {page}: Miss -> {memory}")
        else:
            # If hit, move the page to the end to mark it as "recently used"
            memory.remove(page)
            memory.append(page)
            print(f"Page {page}: Hit  -> {memory}")

    return page_faults

# Usage
p = [7, 0, 1, 2, 0, 3, 0, 4]
lru_page_replacement(p, 3)
