import re

with open("blog.html", "r") as f:
    html = f.read()

# 1. Update the filter nav
nav_old = '<ul class="nav nav-pills justify-content-center mb-5 gap-2" data-aos="fade-up">'
nav_new = '<ul class="nav nav-pills justify-content-center mb-5 gap-2 blog-filter-nav" data-aos="fade-up">'
html = html.replace(nav_old, nav_new)

# 2. Add ID to the grid container
grid_old = '<div class="row g-4 pt-2">'
grid_new = '<div class="row g-4 pt-2" id="blogGrid">'
html = html.replace(grid_old, grid_new)

# 3. Add data-category to each col-lg-4 BEFORE the > character
def inject_cat(match):
    full_wrapper = match.group(0)
    
    # Extract the category from the span inside the match
    cat_match = re.search(r'<span class="text-primary">([^<]+)</span>', full_wrapper)
    category = cat_match.group(1) if cat_match else "All"
    
    # Insert data-category="Category" right before the closing > of the col-lg-4 div
    # Match group 1 is the outer div start string
    d_match = re.search(r'(<div class="col-lg-4 col-md-6 mb-5" data-aos="fade-up"[^>]*)>', full_wrapper)
    if d_match:
        old_div_start = d_match.group(0)
        new_div_start = f'{d_match.group(1)} data-category="{category}">'
        return full_wrapper.replace(old_div_start, new_div_start)
    return full_wrapper

# Using regex to find the entire blog card block non-greedily up to <div class="blog-trim-shape"></div>\n                        </div>\n                    </div>\n</div>
pattern = r'<div class="col-lg-4 col-md-6 mb-5" data-aos="fade-up"[^>]*>.*?<div class="blog-trim-shape"></div>\s*</div>\s*</div>\s*(?:</div>|)'

html = re.sub(pattern, inject_cat, html, flags=re.DOTALL)

# 4. Add the JavaScript
js_script = """
    <!-- Blog Filtering Script -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const filterNavs = document.querySelectorAll('.blog-filter-nav .nav-link');
            const blogCards = document.querySelectorAll('#blogGrid .col-lg-4');

            if (filterNavs.length > 0) {
                filterNavs.forEach(nav => {
                    nav.addEventListener('click', (e) => {
                        e.preventDefault();
                        
                        // Reset
                        filterNavs.forEach(n => {
                            n.classList.remove('active', 'text-white', 'bg-primary');
                            n.classList.add('bg-white', 'text-dark-main');
                        });
                        
                        // Set Active
                        const target = e.target;
                        target.classList.remove('bg-white', 'text-dark-main');
                        target.classList.add('active', 'text-white', 'bg-primary');

                        const filterValue = target.innerText.trim();

                        // Filter
                        blogCards.forEach(card => {
                            const cat = card.getAttribute('data-category');
                            if (filterValue === 'All Articles' || cat === filterValue) {
                                card.style.display = 'block';
                            } else {
                                card.style.display = 'none';
                            }
                        });
                    });
                });
            }
        });
    </script>
"""
if "Blog Filtering Script" not in html:
    html = html.replace('<!-- Bootstrap JS Bundle -->', js_script + '\n    <!-- Bootstrap JS Bundle -->')

with open("blog.html", "w") as f:
    f.write(html)
