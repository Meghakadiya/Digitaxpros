import re

with open("index.html", "r") as f:
    index_content = f.read()

# Extract Navbar
nav_match = re.search(r'(<nav.*?</nav>)', index_content, re.DOTALL)
navbar = nav_match.group(1) if nav_match else ""
# Modify navbar links to point to index.html if necessary
navbar = navbar.replace('href="#', 'href="index.html#')

# Extract Head (Before Navbar)
head_match = re.search(r'(.*?)<nav', index_content, re.DOTALL)
head = head_match.group(1) if head_match else ""

# Extract Footer (And everything after)
footer_match = re.search(r'(<footer.*)', index_content, re.DOTALL)
footer = footer_match.group(1) if footer_match else ""
# Modify footer links? they might be fine.

# ==========================================
# 1. GENERATE BLOG.HTML (Listing Page)
# ==========================================

# Use the exact card HTML from index.html (lines 1453-1476)
card_html_template = """
                    <div class="blog-card group h-100 d-flex flex-column">
                        <div class="blog-img-wrapper overflow-hidden rounded-4 bg-light shadow-sm">
                            <span class="badge bg-{badge_color} text-white position-absolute top-0 start-0 m-3 z-2 rounded-pill px-3 py-2 shadow pb-1">{badge_text}</span>
                            <img src="{img_src}"
                                alt="{title}" class="img-fluid w-100 object-fit-cover transition-all proj-img group-hover-scale"
                                style="height: 250px;">
                        </div>
                        <div class="blog-content bg-white rounded-4 p-4 shadow position-relative border border-light mx-sm-3 mx-2 flex-grow-1 d-flex flex-column"
                            style="margin-top: -40px; z-index: 2;">
                            <div class="d-flex align-items-center text-muted small mb-3 fw-medium">
                                <span class="text-primary">{category}</span>
                                <i class="bi bi-circle-fill text-warning mx-2" style="font-size: 5px;"></i>
                                <span>{date}</span>
                            </div>
                            <h5 class="fw-bold text-dark-main mb-4 blog-title transition-all d-block">{title}</h5>

                            <div class="d-flex justify-content-end position-relative z-1 mt-auto pt-3 border-top border-light">
                                <a href="single-blog.html"
                                    class="text-dark-main fw-bold text-decoration-none small d-flex align-items-center transition-all read-more-text">
                                    <i class="bi bi-arrow-right me-2 transition-transform"></i> Read Full Article
                                </a>
                            </div>
                            <div class="blog-trim-shape"></div>
                        </div>
                    </div>
"""

blogs = [
    {"badge_text": "Featured", "badge_color": "warning", "category": "Google Ads", "date": "20 Dec, 2025", "title": "How to Scale Your Ad Budget Without Losing ROI", "img_src": "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?auto=format&fit=crop&w=600&q=80"},
    {"badge_text": "Local SEO", "badge_color": "dark-main", "category": "Local SEO", "date": "18 Dec, 2025", "title": "The Ultimate Checklist for Google Maps Domination", "img_src": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=600&q=80"},
    {"badge_text": "Automation", "badge_color": "primary", "category": "Automation", "date": "15 Dec, 2025", "title": "The Best Automated Funnels for Service Businesses", "img_src": "https://images.unsplash.com/photo-1553877522-43269d4ea984?auto=format&fit=crop&w=600&q=80"},
    {"badge_text": "Sales", "badge_color": "dark-main", "category": "Sales", "date": "10 Dec, 2025", "title": "Closing the 10x Lead: Scripts for Agency Owners", "img_src": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&w=600&q=80"},
    {"badge_text": "Reviews", "badge_color": "primary", "category": "Reputation", "date": "05 Dec, 2025", "title": "Handling 1-Star Google Reviews Like a Professional", "img_src": "https://images.unsplash.com/photo-1573164713988-8665fc963095?auto=format&fit=crop&w=600&q=80"},
    {"badge_text": "Traffic", "badge_color": "dark-main", "category": "Landing Pages", "date": "01 Dec, 2025", "title": "The 7 Key Elements of a High-Converting Landing Page", "img_src": "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=600&q=80"}
]

cards_html = ""
for i, b in enumerate(blogs):
    delay = (i % 3 + 1) * 100
    cards_html += f'<div class="col-lg-4 col-md-6 mb-5" data-aos="fade-up" data-aos-delay="{delay}">\n'
    cards_html += card_html_template.format(**b)
    cards_html += '</div>\n'

blog_list_body = f"""
    <!-- Blog Hero -->
    <section class="bg-dark-main position-relative overflow-hidden" style="padding-top: 160px; padding-bottom: 80px;">
        <div class="position-absolute bg-primary rounded-circle opacity-10 float-animation" style="width: 400px; height: 400px; top: -100px; left: -100px; filter: blur(80px);"></div>
        <div class="container position-relative z-1 pt-4 pb-3">
            <div class="text-center" data-aos="fade-up">
                <span class="badge bg-white bg-opacity-10 text-white rounded-pill px-3 py-2 mb-3 shadow"><i class="bi bi-journal-text text-primary-light me-2"></i>OUR BLOG</span>
                <h1 class="display-4 fw-900 text-white font-outfit mb-4">Latest Insights & <br>Growth <span class="text-primary-light">Strategies</span></h1>
                <p class="text-white-50 fs-5 mx-auto col-lg-7">Actionable guides, case studies, and industry news to help you scale your service business using automated lead systems.</p>
            </div>
        </div>
    </section>

    <!-- Blog Grid Content -->
    <section class="section-padding bg-light position-relative" style="padding-top: 80px;">
        <div class="container">
            <!-- Filter Nav (Optional UI) -->
            <ul class="nav nav-pills justify-content-center mb-5 gap-2" data-aos="fade-up">
                <li class="nav-item"><a class="nav-link active rounded-pill px-4 py-2 fw-medium shadow-sm transition-all text-white bg-primary" href="#">All Articles</a></li>
                <li class="nav-item"><a class="nav-link rounded-pill px-4 py-2 fw-medium bg-white text-dark-main shadow-sm transition-all hover-primary" href="#">Google Ads</a></li>
                <li class="nav-item"><a class="nav-link rounded-pill px-4 py-2 fw-medium bg-white text-dark-main shadow-sm transition-all hover-primary" href="#">Local SEO</a></li>
                <li class="nav-item"><a class="nav-link rounded-pill px-4 py-2 fw-medium bg-white text-dark-main shadow-sm transition-all hover-primary" href="#">Automation</a></li>
            </ul>

            <div class="row g-4 pt-2">
                {cards_html}
            </div>
            
            <!-- Pagination -->
            <div class="d-flex justify-content-center mt-5 pt-4">
                <nav aria-label="Blog pagination">
                    <ul class="pagination pagination-lg gap-2">
                        <li class="page-item disabled">
                            <a class="page-link rounded-circle d-flex align-items-center justify-content-center fw-bold shadow-sm border-0 bg-white text-muted" href="#" style="width: 50px; height: 50px;" tabindex="-1"><i class="bi bi-chevron-left"></i></a>
                        </li>
                        <li class="page-item active"><a class="page-link rounded-circle d-flex align-items-center justify-content-center fw-bold shadow-sm border-0 bg-primary text-white" href="#" style="width: 50px; height: 50px;">1</a></li>
                        <li class="page-item"><a class="page-link rounded-circle d-flex align-items-center justify-content-center fw-bold shadow-sm border-0 text-dark-main bg-white hover-bg-primary" href="#" style="width: 50px; height: 50px;">2</a></li>
                        <li class="page-item"><a class="page-link rounded-circle d-flex align-items-center justify-content-center fw-bold shadow-sm border-0 text-dark-main bg-white hover-bg-primary" href="#" style="width: 50px; height: 50px;">3</a></li>
                        <li class="page-item">
                            <a class="page-link rounded-circle d-flex align-items-center justify-content-center fw-bold shadow-sm border-0 text-dark-main bg-white hover-bg-primary" href="#" style="width: 50px; height: 50px;"><i class="bi bi-chevron-right"></i></a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
    </section>
"""

with open("blog.html", "w") as f:
    f.write(head + navbar + blog_list_body + footer)


# ==========================================
# 2. GENERATE SINGLE-BLOG.HTML (Article Page)
# ==========================================

single_blog_body = """
    <!-- Article Header -->
    <section class="bg-dark-main position-relative overflow-hidden" style="padding-top: 180px; padding-bottom: 200px;">
        <div class="position-absolute bg-primary rounded-circle opacity-10 float-animation" style="width: 600px; height: 600px; top: -200px; right: -100px; filter: blur(100px);"></div>
        <div class="container position-relative z-1 text-center" data-aos="fade-up">
            <div class="d-flex align-items-center justify-content-center mb-4 small fw-bold">
                <span class="badge bg-primary text-white rounded-pill px-3 py-2 shadow-sm">Google Ads</span>
                <i class="bi bi-circle-fill text-warning mx-3 opacity-50" style="font-size: 6px;"></i>
                <span class="text-white-50">December 20, 2025</span>
                <i class="bi bi-circle-fill text-warning mx-3 opacity-50" style="font-size: 6px;"></i>
                <span class="text-white-50">8 Min Read</span>
            </div>
            <h1 class="display-3 fw-900 text-white font-outfit mb-4 mx-auto" style="max-width: 900px;">How to Scale Your Ad Budget Without Losing ROI</h1>
            <div class="d-flex align-items-center justify-content-center mt-5">
                <div class="bg-primary text-white rounded-circle d-flex align-items-center justify-content-center fw-bold fs-5 shadow me-3" style="width: 50px; height: 50px;">SA</div>
                <div class="text-start">
                    <h6 class="fw-bold mb-0 text-white">Sarah Anderson</h6>
                    <span class="small text-white-50">Director of Paid Media</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Article Content -->
    <section class="bg-light pb-5 position-relative z-2" style="margin-top: -120px;">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-9">
                    <!-- Featured Image -->
                    <div class="bg-white p-2 rounded-5 shadow-lg mb-5" data-aos="fade-up" data-aos-delay="200">
                        <img src="https://images.unsplash.com/photo-1542744173-8e7e53415bb0?auto=format&fit=crop&w=1200&q=80" alt="Blog Featured Image" class="img-fluid rounded-4 w-100 object-fit-cover" style="max-height: 500px;">
                    </div>
                    
                    <!-- Blog Text Body -->
                    <div class="bg-white p-4 p-md-5 rounded-5 shadow-sm border border-light" data-aos="fade-up">
                        <p class="lead text-dark-main fw-bold lh-lg mb-5">Scaling a Google Ads budget is one of the most terrifying things for a local business owner. You finally have a winning campaign generating leads at $40 each. You decide to double the budget—and suddenly your cost-per-lead shoots to $90, and the quality drops. What went wrong?</p>

                        <h3 class="fw-bold text-dark-main font-outfit mb-4 mt-5">The "More Money, More Problems" Paradox</h3>
                        <p class="text-muted fs-6 lh-lg mb-4">When you increase a Google Ads budget too quickly, you reset the learning phase of Google's bidding algorithm. If you are using an automated bid strategy like Maximize Conversions or Target CPA, throwing a huge lump of new budget at it forces the algorithm to explore new, potentially unqualified traffic sources it previously ignored.</p>
                        
                        <div class="bg-primary bg-opacity-10 border-start border-4 border-primary p-4 rounded-3 my-5">
                            <h5 class="fw-bold text-dark-main mb-2"><i class="bi bi-lightbulb-fill text-warning me-2"></i> Pro Tip</h5>
                            <p class="text-muted mb-0 small lh-lg">Never increase your daily campaign budget by more than 20% in a single week if you strictly want to preserve the algorithm's current efficiency.</p>
                        </div>

                        <h3 class="fw-bold text-dark-main font-outfit mb-4 mt-5">1. The 20% Rule of Scaling</h3>
                        <p class="text-muted fs-6 lh-lg mb-4">Instead of doubling your budget overnight, employ the 20% rule. Increase your budget by 15-20%, then let the campaign run for 5 to 7 days. Once the algorithm stabilizes and validates that it can still hit your Target CPA at the new budget limit, raise it by another 20%.</p>
                        
                        <p class="text-muted fs-6 lh-lg mb-4">It takes longer, but it completely protects your ROI.</p>

                        <h3 class="fw-bold text-dark-main font-outfit mb-4 mt-5">2. Segmenting High-Intent vs Low-Intent</h3>
                        <p class="text-muted fs-6 lh-lg mb-4">If your budget is capped, your campaign is fundamentally limited. To scale effectively without destroying your Lead Quality, you should siphon off your best-performing, exact-match keywords into an entirely separate Alpha Campaign.</p>
                        
                        <div class="row g-4 my-4">
                            <div class="col-md-6">
                                <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=600&q=80" class="img-fluid rounded-4 w-100 shadow-sm" alt="Analytics">
                            </div>
                            <div class="col-md-6">
                                <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=600&q=80" class="img-fluid rounded-4 w-100 shadow-sm" alt="Stats">
                            </div>
                        </div>

                        <h3 class="fw-bold text-dark-main font-outfit mb-4 mt-5">Conclusion</h3>
                        <p class="text-muted fs-6 lh-lg mb-4">Scaling doesn't have to mean sacrificing profitability. By taking a systematic, patience-driven approach to budget increases, you can predictably multiply your lead volume while keeping your cost-per-acquisition solidly in the green.</p>

                        <!-- Share & Tags -->
                        <div class="d-flex flex-wrap align-items-center justify-content-between border-top border-light mt-5 pt-4">
                            <div class="d-flex align-items-center gap-2 mb-3 mb-md-0">
                                <span class="fw-bold small text-dark-main me-2">Tags:</span>
                                <span class="badge bg-light text-muted border px-3 py-2 rounded-pill">PPC</span>
                                <span class="badge bg-light text-muted border px-3 py-2 rounded-pill">Google Ads</span>
                                <span class="badge bg-light text-muted border px-3 py-2 rounded-pill">Scaling</span>
                            </div>
                            <div class="d-flex align-items-center gap-3">
                                <span class="fw-bold small text-dark-main">Share:</span>
                                <a href="#" class="btn btn-sm btn-outline-primary rounded-circle hover-scale p-2"><i class="bi bi-linkedin"></i></a>
                                <a href="#" class="btn btn-sm btn-outline-primary rounded-circle hover-scale p-2"><i class="bi bi-twitter-x"></i></a>
                                <a href="#" class="btn btn-sm btn-outline-primary rounded-circle hover-scale p-2"><i class="bi bi-facebook"></i></a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

with open("single-blog.html", "w") as f:
    f.write(head + navbar + single_blog_body + footer)

