def fifo_page_replacement(pages, capacity):
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            # If memory is full, remove the oldest page (index 0)
            if len(memory) == capacity:
                memory.pop(0)
            
            memory.append(page)
            page_faults += 1
            print(f"Page {page}: Miss (Fault) -> Memory: {memory}")
        else:
            print(f"Page {page}: Hit         -> Memory: {memory}")

    return page_faults

# Example Usage
page_reference_string = [7, 0, 1, 2, 0, 3, 0, 4]
frames = 3
total_faults = fifo_page_replacement(page_reference_string, frames)
print(f"\nTotal Page Faults: {total_faults}")

