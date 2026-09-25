with open("index.html", "r") as f:
    lines = f.readlines()

header = "".join(lines[:68])
footer = "".join(lines[1885:])

blog_content = """
    <!-- Blog Hero -->
    <section class="section-padding bg-dark-main position-relative overflow-hidden pt-5 mt-5">
        <div class="position-absolute bg-primary rounded-circle opacity-10 float-animation" style="width: 400px; height: 400px; top: -100px; left: -100px; filter: blur(80px);"></div>
        <div class="container position-relative z-1 pt-5 pb-3">
            <div class="text-center" data-aos="fade-up">
                <span class="badge bg-white bg-opacity-10 text-white rounded-pill px-3 py-2 mb-3 shadow"><i class="bi bi-journal-text text-primary-light me-2"></i>OUR BLOG</span>
                <h1 class="display-4 fw-900 text-white font-outfit mb-4">Latest Insights & <br>Growth <span class="text-primary-light">Strategies</span></h1>
                <p class="text-white-50 fs-5 mx-auto col-lg-7">Actionable guides, case studies, and industry news to help you scale your service business using automated lead systems.</p>
            </div>
        </div>
    </section>

    <!-- Blog Grid Content -->
    <section class="section-padding bg-light position-relative">
        <div class="container">
            <!-- Filter Nav (Optional UI) -->
            <ul class="nav nav-pills justify-content-center mb-5 gap-2" data-aos="fade-up">
                <li class="nav-item"><a class="nav-link active rounded-pill px-4 py-2 fw-medium shadow-sm transition-all text-white bg-primary" href="#">All Articles</a></li>
                <li class="nav-item"><a class="nav-link rounded-pill px-4 py-2 fw-medium bg-white text-dark-main shadow-sm transition-all hover-primary" href="#">Google Ads</a></li>
                <li class="nav-item"><a class="nav-link rounded-pill px-4 py-2 fw-medium bg-white text-dark-main shadow-sm transition-all hover-primary" href="#">Local SEO</a></li>
                <li class="nav-item"><a class="nav-link rounded-pill px-4 py-2 fw-medium bg-white text-dark-main shadow-sm transition-all hover-primary" href="#">Lead Generation</a></li>
            </ul>

            <div class="row g-5">
                <!-- Blog Post 1 -->
                <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="100">
                    <div class="blog-card bg-white rounded-5 shadow-sm border border-light overflow-hidden h-100 position-relative group transition-all d-flex flex-column">
                        <div class="blog-image overflow-hidden position-relative">
                            <span class="badge bg-primary-light bg-opacity-25 text-primary position-absolute top-0 start-0 m-3 z-2 rounded-pill px-3 py-2 shadow-sm border border-primary border-opacity-10 pb-1 fw-bold"><i class="bi bi-star-fill text-warning me-1"></i> Featured</span>
                            <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Blog 1" class="img-fluid w-100 h-100 object-fit-cover transition-transform group-hover-scale" style="height: 250px !important;">
                            <div class="blog-overlay position-absolute w-100 h-100 top-0 start-0 bg-dark-main opacity-0 transition-opacity"></div>
                        </div>
                        <div class="blog-content p-4 p-md-5 bg-white position-relative z-2 transform-up-hover transition-all flex-grow-1 d-flex flex-column">
                            <div class="d-flex align-items-center mb-3 small fw-medium text-muted">
                                <span class="text-primary fw-bold">Automation</span>
                                <i class="bi bi-circle-fill text-warning mx-2 opacity-50" style="font-size: 5px;"></i>
                                <span>24 Sep, 2026</span>
                            </div>
                            <h4 class="fw-bold text-dark-main mb-4 blog-title transition-all lh-base font-outfit">The Ultimate Guide to Automating Client Follow-Ups</h4>
                            <p class="text-muted small mb-4 flex-grow-1 lh-lg">Manual follow-ups are killing your close rate. Discover how to build an automated follow-up system that works 24/7 without being annoying.</p>
                            <a href="#" class="text-dark-main fw-bold text-decoration-none small d-flex align-items-center transition-all read-more-text mt-auto border-top border-light pt-4 w-100">
                                Read Full Article <i class="bi bi-arrow-right ms-2 transition-transform group-hover-translate-x"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Blog Post 2 -->
                <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="200">
                    <div class="blog-card bg-white rounded-5 shadow-sm border border-light overflow-hidden h-100 position-relative group transition-all d-flex flex-column">
                        <div class="blog-image overflow-hidden position-relative">
                            <span class="badge bg-white text-dark-main position-absolute top-0 start-0 m-3 z-2 rounded-pill px-3 py-2 shadow-sm border border-light fw-bold">Local SEO</span>
                            <img src="https://images.unsplash.com/photo-1552581234-26160f608093?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Blog 2" class="img-fluid w-100 h-100 object-fit-cover transition-transform group-hover-scale" style="height: 250px !important;">
                        </div>
                        <div class="blog-content p-4 p-md-5 bg-white position-relative z-2 transform-up-hover transition-all flex-grow-1 d-flex flex-column">
                            <div class="d-flex align-items-center mb-3 small fw-medium text-muted">
                                <span class="text-primary fw-bold">Strategy</span>
                                <i class="bi bi-circle-fill text-warning mx-2 opacity-50" style="font-size: 5px;"></i>
                                <span>18 Sep, 2026</span>
                            </div>
                            <h4 class="fw-bold text-dark-main mb-4 blog-title transition-all lh-base font-outfit">Ranking in the Google Maps Pack (3-Pack)</h4>
                            <p class="text-muted small mb-4 flex-grow-1 lh-lg">Learn the exact signal factors Google uses to determine which three businesses dominate the top of local search results.</p>
                            <a href="#" class="text-dark-main fw-bold text-decoration-none small d-flex align-items-center transition-all read-more-text mt-auto border-top border-light pt-4 w-100">
                                Read Full Article <i class="bi bi-arrow-right ms-2 transition-transform group-hover-translate-x"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Blog Post 3 -->
                <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="300">
                    <div class="blog-card bg-white rounded-5 shadow-sm border border-light overflow-hidden h-100 position-relative group transition-all d-flex flex-column">
                        <div class="blog-image overflow-hidden position-relative">
                            <span class="badge bg-white text-dark-main position-absolute top-0 start-0 m-3 z-2 rounded-pill px-3 py-2 shadow-sm border border-light fw-bold">Google Ads</span>
                            <img src="https://images.unsplash.com/photo-1542744094-3a31f272c490?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Blog 3" class="img-fluid w-100 h-100 object-fit-cover transition-transform group-hover-scale" style="height: 250px !important;">
                        </div>
                        <div class="blog-content p-4 p-md-5 bg-white position-relative z-2 transform-up-hover transition-all flex-grow-1 d-flex flex-column">
                            <div class="d-flex align-items-center mb-3 small fw-medium text-muted">
                                <span class="text-primary fw-bold">PPC</span>
                                <i class="bi bi-circle-fill text-warning mx-2 opacity-50" style="font-size: 5px;"></i>
                                <span>12 Sep, 2026</span>
                            </div>
                            <h4 class="fw-bold text-dark-main mb-4 blog-title transition-all lh-base font-outfit">Stop Wasting Money on Broad Match Keywords</h4>
                            <p class="text-muted small mb-4 flex-grow-1 lh-lg">Are your ads bringing in irrelevant traffic? Find out why phrase and exact match keywords are the secret to massive scale.</p>
                            <a href="#" class="text-dark-main fw-bold text-decoration-none small d-flex align-items-center transition-all read-more-text mt-auto border-top border-light pt-4 w-100">
                                Read Full Article <i class="bi bi-arrow-right ms-2 transition-transform group-hover-translate-x"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Blog Post 4 -->
                <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="100">
                    <div class="blog-card bg-white rounded-5 shadow-sm border border-light overflow-hidden h-100 position-relative group transition-all d-flex flex-column">
                        <div class="blog-image overflow-hidden position-relative">
                            <span class="badge bg-white text-dark-main position-absolute top-0 start-0 m-3 z-2 rounded-pill px-3 py-2 shadow-sm border border-light fw-bold">Case Study</span>
                            <img src="https://images.unsplash.com/photo-1563986768609-322da13575f3?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Blog 4" class="img-fluid w-100 h-100 object-fit-cover transition-transform group-hover-scale" style="height: 250px !important;">
                        </div>
                        <div class="blog-content p-4 p-md-5 bg-white position-relative z-2 transform-up-hover transition-all flex-grow-1 d-flex flex-column">
                            <div class="d-flex align-items-center mb-3 small fw-medium text-muted">
                                <span class="text-primary fw-bold">Results</span>
                                <i class="bi bi-circle-fill text-warning mx-2 opacity-50" style="font-size: 5px;"></i>
                                <span>05 Sep, 2026</span>
                            </div>
                            <h4 class="fw-bold text-dark-main mb-4 blog-title transition-all lh-base font-outfit">How Absolute Plumbing Scaled by 300% in 90 Days</h4>
                            <p class="text-muted small mb-4 flex-grow-1 lh-lg">We mapped out the exact multi-channel local SEO and Review generation campaign that led to this explosive growth.</p>
                            <a href="#" class="text-dark-main fw-bold text-decoration-none small d-flex align-items-center transition-all read-more-text mt-auto border-top border-light pt-4 w-100">
                                Read Full Article <i class="bi bi-arrow-right ms-2 transition-transform group-hover-translate-x"></i>
                            </a>
                        </div>
                    </div>
                </div>
                
                <!-- Blog Post 5 -->
                <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="200">
                    <div class="blog-card bg-white rounded-5 shadow-sm border border-light overflow-hidden h-100 position-relative group transition-all d-flex flex-column">
                        <div class="blog-image overflow-hidden position-relative">
                            <span class="badge bg-white text-dark-main position-absolute top-0 start-0 m-3 z-2 rounded-pill px-3 py-2 shadow-sm border border-light fw-bold">Lead Generation</span>
                            <img src="https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Blog 5" class="img-fluid w-100 h-100 object-fit-cover transition-transform group-hover-scale" style="height: 250px !important;">
                        </div>
                        <div class="blog-content p-4 p-md-5 bg-white position-relative z-2 transform-up-hover transition-all flex-grow-1 d-flex flex-column">
                            <div class="d-flex align-items-center mb-3 small fw-medium text-muted">
                                <span class="text-primary fw-bold">Landing Pages</span>
                                <i class="bi bi-circle-fill text-warning mx-2 opacity-50" style="font-size: 5px;"></i>
                                <span>28 Aug, 2026</span>
                            </div>
                            <h4 class="fw-bold text-dark-main mb-4 blog-title transition-all lh-base font-outfit">7 Elements of a High-Converting Landing Page</h4>
                            <p class="text-muted small mb-4 flex-grow-1 lh-lg">If your traffic isn't converting, it's usually your page. Here are the 7 psychological triggers you need to implement today.</p>
                            <a href="#" class="text-dark-main fw-bold text-decoration-none small d-flex align-items-center transition-all read-more-text mt-auto border-top border-light pt-4 w-100">
                                Read Full Article <i class="bi bi-arrow-right ms-2 transition-transform group-hover-translate-x"></i>
                            </a>
                        </div>
                    </div>
                </div>
                
                <!-- Blog Post 6 -->
                <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="300">
                    <div class="blog-card bg-white rounded-5 shadow-sm border border-light overflow-hidden h-100 position-relative group transition-all d-flex flex-column">
                        <div class="blog-image overflow-hidden position-relative">
                            <span class="badge bg-white text-dark-main position-absolute top-0 start-0 m-3 z-2 rounded-pill px-3 py-2 shadow-sm border border-light fw-bold">Reputation</span>
                            <img src="https://images.unsplash.com/photo-1573164713988-8665fc963095?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Blog 6" class="img-fluid w-100 h-100 object-fit-cover transition-transform group-hover-scale" style="height: 250px !important;">
                        </div>
                        <div class="blog-content p-4 p-md-5 bg-white position-relative z-2 transform-up-hover transition-all flex-grow-1 d-flex flex-column">
                            <div class="d-flex align-items-center mb-3 small fw-medium text-muted">
                                <span class="text-primary fw-bold">Trust</span>
                                <i class="bi bi-circle-fill text-warning mx-2 opacity-50" style="font-size: 5px;"></i>
                                <span>15 Aug, 2026</span>
                            </div>
                            <h4 class="fw-bold text-dark-main mb-4 blog-title transition-all lh-base font-outfit">Handling Negative Reviews Like a Professional</h4>
                            <p class="text-muted small mb-4 flex-grow-1 lh-lg">One one-star review isn't the end of the world. Learn the blueprint to address it, spin it positively, and preserve local trust.</p>
                            <a href="#" class="text-dark-main fw-bold text-decoration-none small d-flex align-items-center transition-all read-more-text mt-auto border-top border-light pt-4 w-100">
                                Read Full Article <i class="bi bi-arrow-right ms-2 transition-transform group-hover-translate-x"></i>
                            </a>
                        </div>
                    </div>
                </div>

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
    f.write(header + blog_content + footer)
