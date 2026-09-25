import re

with open("blog.html", "r") as f:
    text = f.read()

# Make sure all .col-lg-4 column containers get a data-category based on their text-primary span
# A card structure inside col-lg-4 has:
# <span class="text-primary">Some Category</span>

def inject_data_category(match):
    col_str = match.group(1)
    card_html = match.group(2)
    
    # Try to find the category in the card HTML
    cat_match = re.search(r'<span class="text-primary">([^<]+)</span>', card_html)
    category = cat_match.group(1) if cat_match else "All"
    
    return f'{col_str} data-category="{category}" >\n{card_html}'

# Find <div class="col-lg-4 col-md-6 mb-5" ... >
text = re.sub(r'(<div class="col-lg-4 col-md-6 mb-5"[^>]*)>\n(.*?blog-card.*?)</div>\n</div>', inject_data_category, text, flags=re.DOTALL)

# Add ID to the filter links and the row container
text = text.replace('<ul class="nav nav-pills justify-content-center mb-5 gap-2" data-aos="fade-up">', '<ul class="nav nav-pills justify-content-center mb-5 gap-2 blog-filter-nav" data-aos="fade-up">')
text = text.replace('<div class="row g-4 pt-2">', '<div class="row g-4 pt-2" id="blogGrid">')

# Add the JavaScript filter logic right before footer
js_script = """
    <!-- Blog Filtering Script -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const filterNavs = document.querySelectorAll('.blog-filter-nav .nav-link');
            const blogCards = document.querySelectorAll('#blogGrid .col-lg-4');

            filterNavs.forEach(nav => {
                nav.addEventListener('click', (e) => {
                    e.preventDefault();
                    
                    // Reset Active Classes
                    filterNavs.forEach(n => {
                        n.classList.remove('active', 'text-white', 'bg-primary');
                        n.classList.add('bg-white', 'text-dark-main');
                    });
                    
                    // Set Target as Active
                    const target = e.target;
                    target.classList.remove('bg-white', 'text-dark-main');
                    target.classList.add('active', 'text-white', 'bg-primary');

                    const categoryFilter = target.innerText.trim();

                    // Filter Cards
                    blogCards.forEach(card => {
                        // Quick animation reset
                        card.style.opacity = '0';
                        card.style.transform = 'translateY(10px)';
                        
                        setTimeout(() => {
                            if (categoryFilter === 'All Articles' || card.getAttribute('data-category') === categoryFilter) {
                                card.style.display = 'block';
                                setTimeout(() => {
                                    card.style.opacity = '1';
                                    card.style.transform = 'translateY(0)';
                                }, 50);
                            } else {
                                card.style.display = 'none';
                            }
                        }, 300);
                        
                    });
                });
            });
        });
    </script>
"""

text = text.replace('<!-- Bootstrap JS Bundle -->', js_script + '\n    <!-- Bootstrap JS Bundle -->')

with open("blog.html", "w") as f:
    f.write(text)

