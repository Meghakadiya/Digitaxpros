import re

with open("index.html", "r") as f:
    index_content = f.read()

# Extract Navbar
nav_match = re.search(r'(<nav.*?</nav>)', index_content, re.DOTALL)
navbar = nav_match.group(1) if nav_match else ""
navbar = navbar.replace('href="#', 'href="index.html#')

# Extract Head
head_match = re.search(r'(.*?)<nav', index_content, re.DOTALL)
head = head_match.group(1) if head_match else ""

# Extract Footer
footer_match = re.search(r'(<footer.*)', index_content, re.DOTALL)
footer = footer_match.group(1) if footer_match else ""

# ==========================================
# 2. GENERATE SINGLE-BLOG.HTML (Article Page)
# ==========================================

single_blog_body = """
    <!-- Article Header -->
    <section class="bg-dark-main position-relative overflow-hidden" style="padding-top: 180px; padding-bottom: 200px;">
        <div class="position-absolute bg-primary rounded-circle opacity-10 float-animation" style="width: 600px; height: 600px; top: -200px; right: -100px; filter: blur(100px);"></div>
        <div class="container position-relative z-1">
            <nav aria-label="breadcrumb" class="mb-4" data-aos="fade-up">
                <ol class="breadcrumb">
                    <li class="breadcrumb-item"><a href="index.html" class="text-white-50 text-decoration-none transition-all hover-primary">Home</a></li>
                    <li class="breadcrumb-item"><a href="blog.html" class="text-white-50 text-decoration-none transition-all hover-primary">Blog</a></li>
                    <li class="breadcrumb-item active text-primary fw-bold" aria-current="page">Google Ads</li>
                </ol>
            </nav>
            <div class="row">
                <div class="col-lg-10" data-aos="fade-up">
                    <div class="d-flex align-items-center mb-4 small fw-bold">
                        <span class="badge bg-primary text-white rounded-pill px-3 py-2 shadow-sm">Google Ads</span>
                        <i class="bi bi-circle-fill text-warning mx-3 opacity-50" style="font-size: 6px;"></i>
                        <span class="text-white-50">December 20, 2025</span>
                        <i class="bi bi-circle-fill text-warning mx-3 opacity-50" style="font-size: 6px;"></i>
                        <span class="text-white-50">8 Min Read</span>
                    </div>
                    <h1 class="display-3 fw-900 text-white font-outfit mb-4 pe-lg-5">How to Scale Your Ad Budget Without Losing ROI</h1>
                    <div class="d-flex align-items-center mt-5">
                        <div class="bg-primary text-white rounded-circle d-flex align-items-center justify-content-center fw-bold fs-5 shadow-sm border border-white border-opacity-10 me-3" style="width: 55px; height: 55px;">SA</div>
                        <div class="text-start">
                            <h6 class="fw-bold mb-0 text-white tracking-wide">Sarah Anderson</h6>
                            <span class="small text-white-50">Director of Paid Media</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Article Content & Sidebar -->
    <section class="bg-light pb-5 position-relative z-2" style="margin-top: -100px;">
        <div class="container">
            <!-- Full Width Featured Image -->
            <div class="bg-white p-2 rounded-5 shadow-lg mb-5" data-aos="fade-up" data-aos-delay="100">
                <img src="https://images.unsplash.com/photo-1542744173-8e7e53415bb0?auto=format&fit=crop&w=1400&q=80" alt="Blog Featured Image" class="img-fluid rounded-4 w-100 object-fit-cover" style="height: 450px;">
            </div>

            <div class="row g-5">
                <!-- Main Article Column (Fills out left space) -->
                <div class="col-lg-8" data-aos="fade-up" data-aos-delay="200">
                    <div class="bg-white p-4 p-md-5 rounded-5 shadow-sm border border-light h-100">
                        <p class="lead text-dark-main fw-bold lh-lg mb-5">Scaling a Google Ads budget is one of the most terrifying things for a local business owner. You finally have a winning campaign generating leads at $40 each. You decide to double the budget—and suddenly your cost-per-lead shoots to $90, and the quality drops. What went wrong?</p>

                        <h3 class="fw-bold text-dark-main font-outfit mb-4 mt-5">The "More Money, More Problems" Paradox</h3>
                        <p class="text-muted fs-6 lh-lg mb-4">When you increase a Google Ads budget too quickly, you reset the learning phase of Google's bidding algorithm. If you are using an automated bid strategy like Maximize Conversions or Target CPA, throwing a huge lump of new budget at it forces the algorithm to explore new, potentially unqualified traffic sources it previously ignored.</p>
                        
                        <div class="bg-primary bg-opacity-10 border-start border-4 border-primary p-4 rounded-3 my-5">
                            <h5 class="fw-bold text-dark-main mb-2"><i class="bi bi-lightbulb-fill text-warning me-2"></i> Pro Tip</h5>
                            <p class="text-muted mb-0 small lh-lg">Never increase your daily campaign budget by more than 20% in a single week if you strictly want to preserve the algorithm's current efficiency.</p>
                        </div>

                        <h3 class="fw-bold text-dark-main font-outfit mb-4 mt-5">1. The 20% Rule of Scaling</h3>
                        <p class="text-muted fs-6 lh-lg mb-4">Instead of doubling your budget overnight, employ the 20% rule. Increase your budget by 15-20%, then let the campaign run for 5 to 7 days. Once the algorithm stabilizes and validates that it can still hit your Target CPA at the new budget limit, raise it by another 20%.</p>
                        
                        <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80" class="img-fluid rounded-4 w-100 shadow-sm my-4" alt="Analytics">

                        <h3 class="fw-bold text-dark-main font-outfit mb-4 mt-5">2. Segmenting High-Intent vs Low-Intent</h3>
                        <p class="text-muted fs-6 lh-lg mb-4">If your budget is capped, your campaign is fundamentally limited. To scale effectively without destroying your Lead Quality, you should siphon off your best-performing, exact-match keywords into an entirely separate Alpha Campaign.</p>
                        
                        <h3 class="fw-bold text-dark-main font-outfit mb-4 mt-5">Conclusion</h3>
                        <p class="text-muted fs-6 lh-lg mb-4">Scaling doesn't have to mean sacrificing profitability. By taking a systematic, patience-driven approach to budget increases, you can predictably multiply your lead volume while keeping your cost-per-acquisition solidly in the green.</p>

                        <!-- Share & Tags -->
                        <div class="d-flex flex-wrap align-items-center justify-content-between border-top border-light mt-5 pt-4">
                            <div class="d-flex align-items-center gap-2 mb-3 mb-md-0">
                                <span class="fw-bold small text-dark-main me-2">Tags:</span>
                                <span class="badge bg-light text-muted border px-3 py-2 rounded-pill shadow-sm">PPC</span>
                                <span class="badge bg-light text-muted border px-3 py-2 rounded-pill shadow-sm">Google Ads</span>
                                <span class="badge bg-light text-muted border px-3 py-2 rounded-pill shadow-sm">Scaling</span>
                            </div>
                            <div class="d-flex align-items-center gap-3">
                                <span class="fw-bold small text-dark-main">Share:</span>
                                <a href="#" class="btn btn-sm btn-outline-primary rounded-circle transition-all hover-scale d-flex align-items-center justify-content-center" style="width: 35px; height: 35px;"><i class="bi bi-linkedin"></i></a>
                                <a href="#" class="btn btn-sm btn-outline-primary rounded-circle transition-all hover-scale d-flex align-items-center justify-content-center" style="width: 35px; height: 35px;"><i class="bi bi-twitter-x"></i></a>
                                <a href="#" class="btn btn-sm btn-outline-primary rounded-circle transition-all hover-scale d-flex align-items-center justify-content-center" style="width: 35px; height: 35px;"><i class="bi bi-facebook"></i></a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Sidebar (Fills out right side) -->
                <div class="col-lg-4" data-aos="fade-up" data-aos-delay="300">
                    <div class="position-sticky" style="top: 120px;">
                        
                        <!-- Search Widget -->
                        <div class="bg-white p-4 rounded-5 shadow-sm border border-light mb-4 text-center">
                            <h5 class="fw-bold text-dark-main mb-3 font-outfit">Search Articles</h5>
                            <div class="position-relative">
                                <input type="text" class="form-control rounded-pill pe-5 py-3 bg-light border-0" placeholder="Find strategies...">
                                <i class="bi bi-search position-absolute top-50 translate-middle-y text-primary fw-bold" style="right: 20px;"></i>
                            </div>
                        </div>

                        <!-- Related Articles Widget -->
                        <div class="bg-white p-4 p-xl-5 rounded-5 shadow-sm border border-light mb-4">
                            <h5 class="fw-bold text-dark-main mb-4 font-outfit d-flex align-items-center"><i class="bi bi-journal-richtext text-primary me-2"></i> Related Articles</h5>
                            
                            <!-- Related Card 1 -->
                            <div class="d-flex mb-4 group cursor-pointer border-bottom border-light pb-4">
                                <div class="overflow-hidden rounded-4 shadow-sm" style="width: 100px; height: 100px; flex-shrink: 0;">
                                    <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=300&q=80" alt="Related" class="img-fluid w-100 h-100 object-fit-cover transition-transform group-hover-scale">
                                </div>
                                <div class="ms-3 d-flex flex-column justify-content-center">
                                    <div class="small fw-bold text-primary mb-1">LOCAL SEO</div>
                                    <h6 class="fw-bold text-dark-main mb-0 lh-base transition-all group-hover-translate-x" style="font-size: 0.95rem;">The Ultimate Checklist for Google Maps</h6>
                                </div>
                            </div>
                            
                            <!-- Related Card 2 -->
                            <div class="d-flex mb-4 group cursor-pointer border-bottom border-light pb-4">
                                <div class="overflow-hidden rounded-4 shadow-sm" style="width: 100px; height: 100px; flex-shrink: 0;">
                                    <img src="https://images.unsplash.com/photo-1553877522-43269d4ea984?auto=format&fit=crop&w=300&q=80" alt="Related" class="img-fluid w-100 h-100 object-fit-cover transition-transform group-hover-scale">
                                </div>
                                <div class="ms-3 d-flex flex-column justify-content-center">
                                    <div class="small fw-bold text-primary mb-1">AUTOMATION</div>
                                    <h6 class="fw-bold text-dark-main mb-0 lh-base transition-all group-hover-translate-x" style="font-size: 0.95rem;">Automated Funnels for Service Businesses</h6>
                                </div>
                            </div>

                            <!-- Related Card 3 -->
                            <div class="d-flex group cursor-pointer">
                                <div class="overflow-hidden rounded-4 shadow-sm" style="width: 100px; height: 100px; flex-shrink: 0;">
                                    <img src="https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=300&q=80" alt="Related" class="img-fluid w-100 h-100 object-fit-cover transition-transform group-hover-scale">
                                </div>
                                <div class="ms-3 d-flex flex-column justify-content-center">
                                    <div class="small fw-bold text-primary mb-1">LANDING PAGES</div>
                                    <h6 class="fw-bold text-dark-main mb-0 lh-base transition-all group-hover-translate-x" style="font-size: 0.95rem;">Elements of a High-Converting Page</h6>
                                </div>
                            </div>
                        </div>

                        <!-- Newsletter CTA -->
                        <div class="bg-primary p-4 p-xl-5 rounded-5 shadow-sm text-center overflow-hidden position-relative border border-primary-light">
                            <i class="bi bi-envelope-paper-fill display-4 text-white opacity-25 position-absolute" style="top: -20px; right: 10px;"></i>
                            <span class="badge bg-white text-primary rounded-pill px-3 py-2 mb-3 position-relative z-1 shadow-sm fw-bold">WEEKLY NEWSLETTER</span>
                            <h4 class="fw-900 text-white mb-3 font-outfit position-relative z-1">Get Weekly Growth Tips</h4>
                            <p class="text-white-50 small mb-4 position-relative z-1 lh-lg">Join 15,000+ service business owners receiving our best strategies.</p>
                            <div class="position-relative z-1">
                                <input type="email" class="form-control rounded-pill py-3 mb-3 bg-dark-main bg-opacity-25 border-0 text-white shadow-none placeholder-white" placeholder="Enter your email address">
                                <button class="btn btn-dark-main rounded-pill w-100 py-3 fw-bold hover-lift transition-all shadow">Subscribe Now</button>
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
