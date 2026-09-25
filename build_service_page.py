import re
import os

with open("index.html", "r") as f:
    index_content = f.read()

# Extract Navbar
nav_match = re.search(r'(<nav.*?</nav>)', index_content, re.DOTALL)
navbar = nav_match.group(1) if nav_match else ""
navbar = navbar.replace('href="#', 'href="../index.html#')
navbar = navbar.replace('href="blog.html"', 'href="../blog.html"')

# Extract Head (up to <nav)
head_match = re.search(r'(.*?)<nav', index_content, re.DOTALL)
head = head_match.group(1) if head_match else ""
# Modify asset paths in head
head = head.replace('href="assets/', 'href="../assets/')

# Extract Footer (And everything after)
footer_match = re.search(r'(<footer.*)', index_content, re.DOTALL)
footer = footer_match.group(1) if footer_match else ""
footer = footer.replace('href="#', 'href="../index.html#')
footer = footer.replace('src="assets/', 'src="../assets/')
footer = footer.replace('href="assets/', 'href="../assets/')
footer = footer.replace('href="blog.html"', 'href="../blog.html"')


# Generate the modernized Service Page

service_body = """
    <!-- Service Header -->
    <section class="bg-dark-main position-relative overflow-hidden" style="padding-top: 200px; padding-bottom: 220px;">
        <div class="position-absolute bg-primary rounded-circle opacity-10 float-animation" style="width: 500px; height: 500px; top: -150px; left: -100px; filter: blur(90px);"></div>
        <div class="position-absolute bg-warning rounded-circle opacity-10 float-animation-delayed" style="width: 300px; height: 300px; bottom: -50px; right: -50px; filter: blur(70px);"></div>
        
        <div class="container position-relative z-1 text-center">
            <span class="badge bg-white bg-opacity-10 text-white rounded-pill px-4 py-2 border border-white border-opacity-10 mb-4 tracking-wider letter-spacing-1 shadow text-uppercase">Google Maps SEO Expert & Management</span>
            <h1 class="display-3 fw-900 text-white font-outfit mb-4 text-shadow mx-auto" style="max-width: 900px;">Google Business Profile <span class="text-primary-light">Management</span></h1>
            <p class="text-white-50 fs-5 mx-auto max-w-700 lh-lg mb-5" style="max-width: 800px;">
                Stop letting competitors steal your local traffic. We provide complete Google My Business optimization routines to ensure you rank #1 in the Local Map Pack.
            </p>
            <button class="btn btn-primary rounded-pill px-5 py-3 fw-bold shadow-lg hover-scale transition-all d-inline-flex align-items-center">
                Optimize My Profile <i class="bi bi-arrow-right ms-2 fs-5"></i>
            </button>
        </div>
    </section>

    <!-- Detailed Content Area -->
    <section class="bg-light position-relative z-2" style="margin-top: -100px; padding-bottom: 120px;">
        <div class="container">
            <!-- Full Width Stat Bar -->
            <div class="bg-white p-4 p-lg-5 rounded-4 shadow-lg mb-5 text-center d-flex flex-wrap justify-content-center gap-4 gap-lg-5" data-aos="fade-up">
                <div class="px-3 border-end">
                    <h2 class="display-6 fw-bold text-dark-main mb-0">8x</h2>
                    <p class="text-muted small mb-0 fw-medium">More Local Calls</p>
                </div>
                <div class="px-3 border-end">
                    <h2 class="display-6 fw-bold text-dark-main mb-0">94%</h2>
                    <p class="text-muted small mb-0 fw-medium">Map Pack ROI</p>
                </div>
                <div class="px-3">
                    <h2 class="display-6 fw-bold text-dark-main mb-0">#1</h2>
                    <p class="text-muted small mb-0 fw-medium">Local Ranking</p>
                </div>
            </div>

            <div class="row g-5 align-items-start pt-5">
                <!-- Left Sidebar Details -->
                <div class="col-lg-4" data-aos="fade-up">
                    <div class="position-sticky" style="top: 130px;">
                        <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80" alt="Dashboard" class="img-fluid rounded-4 shadow-sm mb-4 w-100 object-fit-cover" style="height: 300px;">
                        
                        <div class="bg-white p-4 rounded-4 shadow-sm border border-light">
                            <h5 class="fw-bold text-dark-main mb-4 font-outfit border-bottom border-light pb-3">What's Included</h5>
                            <ul class="list-unstyled mb-0">
                                <li class="mb-3 d-flex"><i class="bi bi-check-circle-fill text-primary me-3 fs-5"></i> <span class="text-muted fw-medium py-1">Full GMB Setup</span></li>
                                <li class="mb-3 d-flex"><i class="bi bi-check-circle-fill text-primary me-3 fs-5"></i> <span class="text-muted fw-medium py-1">Category Optimization</span></li>
                                <li class="mb-3 d-flex"><i class="bi bi-check-circle-fill text-primary me-3 fs-5"></i> <span class="text-muted fw-medium py-1">Geo-Grid Tracking</span></li>
                                <li class="mb-3 d-flex"><i class="bi bi-check-circle-fill text-primary me-3 fs-5"></i> <span class="text-muted fw-medium py-1">Weekly Posts</span></li>
                                <li class="mb-0 d-flex"><i class="bi bi-check-circle-fill text-primary me-3 fs-5"></i> <span class="text-muted fw-medium py-1">Review Response Gen</span></li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Right Main Content -->
                <div class="col-lg-8" data-aos="fade-up" data-aos-delay="100">
                    <div class="bg-white p-4 p-md-5 rounded-5 shadow-sm border border-light">
                        <span class="badge bg-primary-light bg-opacity-25 text-primary rounded-pill px-3 py-2 mb-3 fw-bold border border-primary border-opacity-10">THE PROBLEM</span>
                        <h2 class="display-6 fw-bold mb-4 text-dark-main font-outfit">Why You Need Professional Google Business Management</h2>
                        <p class="text-muted lh-lg fs-5 mb-5">
                            Managing a local business profile goes beyond just claiming your name. From <strong>Google Maps SEO</strong> to active <strong>Google Business Profile optimization</strong>, the ecosystem requires constant signal generation, Q&A management, and review responses. If you are not posting updates, adding photos, and fighting spam, Google's algorithm will favor competitors who do.
                        </p>

                        <div class="row g-4 mt-2 mb-5">
                            <div class="col-md-6">
                                <div class="p-4 bg-light rounded-4 h-100 border border-light transition-all hover-shadow group">
                                    <div class="icon-box-lg bg-white rounded-circle shadow-sm d-flex align-items-center justify-content-center text-primary mb-4 transition-transform group-hover-scale" style="width: 60px; height: 60px;">
                                        <i class="bi bi-geo-alt-fill fs-4"></i>
                                    </div>
                                    <h5 class="fw-bold text-dark-main mb-3 font-outfit">Local SEO Signals</h5>
                                    <p class="text-muted small mb-0 lh-lg">We optimize your primary categories, update metadata in your photos, and create weekly SEO-rich Google Posts.</p>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="p-4 bg-light rounded-4 h-100 border border-light transition-all hover-shadow group">
                                    <div class="icon-box-lg bg-white rounded-circle shadow-sm d-flex align-items-center justify-content-center text-primary mb-4 transition-transform group-hover-scale" style="width: 60px; height: 60px;">
                                        <i class="bi bi-star-fill text-warning fs-4"></i>
                                    </div>
                                    <h5 class="fw-bold text-dark-main mb-3 font-outfit">Review Management</h5>
                                    <p class="text-muted small mb-0 lh-lg">We help generate 5-star reviews and actively respond to all comments building deep, local consumer trust.</p>
                                </div>
                            </div>
                        </div>

                        <span class="badge bg-primary-light bg-opacity-25 text-primary rounded-pill px-3 py-2 mb-3 fw-bold border border-primary border-opacity-10 mt-4">OUR PROCESS</span>
                        <h2 class="display-6 fw-bold mb-4 text-dark-main font-outfit mt-2">How We Drive Results</h2>
                        <ul class="list-unstyled mt-5">
                            <li class="d-flex mb-5">
                                <div class="bg-primary text-white rounded-circle d-flex align-items-center justify-content-center shadow border border-4 border-white flex-shrink-0" style="width: 50px; height: 50px; font-weight: 900; font-size: 1.2rem; margin-top: -5px;">1</div>
                                <div class="ms-4">
                                    <h4 class="fw-bold text-dark-main mb-2 font-outfit">Audit & Optimization</h4>
                                    <p class="text-muted lh-lg">We analyze your current rankings, strip out keyword stuffing that triggers penalties, and rewrite your descriptions using hyper-local SEO data.</p>
                                </div>
                            </li>
                            <li class="d-flex mb-5">
                                <div class="bg-primary text-white rounded-circle d-flex align-items-center justify-content-center shadow border border-4 border-white flex-shrink-0" style="width: 50px; height: 50px; font-weight: 900; font-size: 1.2rem; margin-top: -5px;">2</div>
                                <div class="ms-4">
                                    <h4 class="fw-bold text-dark-main mb-2 font-outfit">Consistent Signal Generation</h4>
                                    <p class="text-muted lh-lg">Google rewards activity. We upload optimized images, create weekly product/service posts, and deploy Q&As to signal consistent activity.</p>
                                </div>
                            </li>
                            <li class="d-flex">
                                <div class="bg-primary text-white rounded-circle d-flex align-items-center justify-content-center shadow border border-4 border-white flex-shrink-0" style="width: 50px; height: 50px; font-weight: 900; font-size: 1.2rem; margin-top: -5px;">3</div>
                                <div class="ms-4">
                                    <h4 class="fw-bold text-dark-main mb-2 font-outfit">Geo-Grid Tracking</h4>
                                    <p class="text-muted lh-lg">We use advanced heatmaps to track your exact ranking position across a 5-mile radius, adjusting our strategy based on the hardest-to-win neighborhoods.</p>
                                </div>
                            </li>
                        </ul>

                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Animated CTA Section (Same as Main) -->
    <section class="cta-section py-5 bg-dark-main position-relative overflow-hidden text-center text-lg-start">
        <div class="position-absolute bg-primary rounded-circle opacity-10 float-animation" style="width: 300px; height: 300px; bottom: -50px; right: 10%; filter: blur(60px);"></div>
        <div class="container position-relative z-1">
            <div class="bg-white p-5 rounded-5 shadow-lg position-relative overflow-hidden">
                <div class="position-absolute top-0 end-0 bg-primary opacity-10 h-100" style="width: 30%; clip-path: polygon(20% 0, 100% 0, 100% 100%, 0% 100%);"></div>
                <div class="row align-items-center position-relative z-2">
                    <div class="col-lg-8 mb-4 mb-lg-0 text-center text-lg-start">
                        <span class="badge bg-primary text-white rounded-pill px-3 py-2 mb-3 shadow-sm">Ready to Grow?</span>
                        <h2 class="display-6 fw-bold text-dark-main mb-2 font-outfit">Ready to Scale Your Service Business?</h2>
                        <p class="text-muted fs-5 mb-0">Stop losing local leads to your competitors. Let's build your automated growth engine.</p>
                    </div>
                    <div class="col-lg-4 text-center text-lg-end">
                        <button class="btn btn-dark-main rounded-pill px-5 py-3 fw-bold shadow-lg hover-scale transition-all" data-bs-toggle="modal" data-bs-target="#quoteModal">
                            Book Free Audit <i class="bi bi-arrow-right ms-2 fs-5"></i>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

with open("services/google-business-profile.html", "w") as f:
    f.write(head + navbar + service_body + footer)

