import re

# We will read the blog cards from index.html (which hasn't been corrupted) to rebuild them.
# The cards in index.html and blog.html are identical in HTML structure.

with open("index.html", "r") as f:
    idx_content = f.read()

# Extract the 6 cards from index.html
cards_match = re.search(r'<div class="row g-4 mb-5 pt-4">(.*?)<div class="text-center mt-5">', idx_content, re.DOTALL)

if cards_match:
    original_cards_html = cards_match.group(1)
else:
    print("Failed to find original cards in index.html")
    exit(1)

# Now we need to add data-category to these cards based on the text-primary span
def inject_data_category(match):
    col_str = match.group(1)
    card_inner = match.group(2)
    
    cat_match = re.search(r'<span class="text-primary">([^<]+)</span>', card_inner)
    category = cat_match.group(1) if cat_match else "All"
    
    # We include the proper closing div structure this time!
    return f'{col_str} data-category="{category}">\n{card_inner}</div>\n</div>'

fixed_cards_html = re.sub(r'(<div class="col-lg-4 col-md-6 mb-5"[^>]*>)\n(.*?blog-card.*?)</div>\n\s*</div>', inject_data_category, original_cards_html, flags=re.DOTALL)

# Now read blog.html
with open("blog.html", "r") as f:
    blog_content = f.read()

# Replace everything from <div class="row g-4 pt-2" id="blogGrid"> up to <!-- Pagination -->
new_blog_content = re.sub(r'<div class="row g-4 pt-2" id="blogGrid">.*?<!-- Pagination -->', 
                          f'<div class="row g-4 pt-2" id="blogGrid">\n{fixed_cards_html}\n            </div>\n            \n            <!-- Pagination -->', 
                          blog_content, flags=re.DOTALL)

with open("blog.html", "w") as f:
    f.write(new_blog_content)
    
print("Successfully repaired blog.html layout!")
