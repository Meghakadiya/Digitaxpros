import re

with open("single-blog.html", "r") as f:
    html = f.read()

# Replace the single column layout with a two-column sidebar layout
# Old: <div class="row justify-content-center">\n                <div class="col-lg-9">
# New: <div class="row g-5">\n                <div class="col-lg-8">

html = html.replace('<div class="row justify-content-center">', '<div class="row g-5">')
html = html.replace('<div class="col-lg-9">', '<div class="col-lg-8">')

# Now insert the sidebar after the col-lg-8 closes, which is right before:
#             </div>\n        </div>\n    </section>\n<footer
sidebar_html = """
                <!-- Sidebar -->
                <div class="col-lg-4">
                    <div class="sticky-top" style="top: 120px;" data-aos="fade-left" data-aos-delay="200">
                        <!-- Recommended Blogs -->
                        <div class="bg-white rounded-4 p-4 shadow-sm border border-light mb-4">
                            <h5 class="fw-bold text-dark-main font-outfit mb-4 d-flex align-items-center pb-3 border-bottom border-light">
                                <i class="bi bi-stars text-primary me-2"></i> Recommended
                            </h5>
                            
                            <!-- Article 1 -->
                            <a href="#" class="d-flex align-items-center text-decoration-none group mb-4">
                                <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=200&q=80" alt="Blog" class="rounded-3 shadow-sm object-fit-cover me-3 transition-transform group-hover-scale" style="width: 80px; height: 80px;">
                                <div>
                                    <span class="text-primary small fw-bold text-uppercase d-block mb-1" style="font-size: 10px; letter-spacing: 0.5px;">Local SEO</span>
                                    <h6 class="fw-bold text-dark-main mb-0 transition-color group-hover-primary lh-sm small">Checklist for Google Maps Domination</h6>
                                </div>
                            </a>
                            
                            <!-- Article 2 -->
                            <a href="#" class="d-flex align-items-center text-decoration-none group mb-4">
                                <img src="https://images.unsplash.com/photo-1553877522-43269d4ea984?auto=format&fit=crop&w=200&q=80" alt="Blog" class="rounded-3 shadow-sm object-fit-cover me-3 transition-transform group-hover-scale" style="width: 80px; height: 80px;">
                                <div>
                                    <span class="text-primary small fw-bold text-uppercase d-block mb-1" style="font-size: 10px; letter-spacing: 0.5px;">Automation</span>
                                    <h6 class="fw-bold text-dark-main mb-0 transition-color group-hover-primary lh-sm small">Automated Funnels for Service Businesses</h6>
                                </div>
                            </a>
                            
                            <!-- Article 3 -->
                            <a href="#" class="d-flex align-items-center text-decoration-none group">
                                <img src="https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&w=200&q=80" alt="Blog" class="rounded-3 shadow-sm object-fit-cover me-3 transition-transform group-hover-scale" style="width: 80px; height: 80px;">
                                <div>
                                    <span class="text-primary small fw-bold text-uppercase d-block mb-1" style="font-size: 10px; letter-spacing: 0.5px;">Sales</span>
                                    <h6 class="fw-bold text-dark-main mb-0 transition-color group-hover-primary lh-sm small">Closing the 10x Lead: Scripts for Agencies</h6>
                                </div>
                            </a>
                        </div>
                        
                        <!-- CTA Box -->
                        <div class="bg-gradient-brand text-white rounded-4 p-4 shadow-lg position-relative overflow-hidden text-center group">
                            <div class="position-absolute top-0 end-0 bg-white opacity-10 rounded-circle" style="width: 150px; height: 150px; transform: translate(30%, -30%);"></div>
                            <h5 class="fw-bold font-outfit mb-3 position-relative z-1">Want to Double Your Calls?</h5>
                            <p class="small opacity-75 mb-4 position-relative z-1">Get a free strategy roadmap for your business.</p>
                            <button class="btn btn-white text-dark-main fw-bold rounded-pill w-100 shadow-sm position-relative z-1 hover-scale transition-all" data-bs-toggle="modal" data-bs-target="#quoteModal">Get Free Audit</button>
                        </div>
                    </div>
                </div>
"""

# The closing of col-lg-8 is followed by closing of row.
# We will find the end of the row and inject the sidebar before it closes the row.
# To be robust, let's locate the row close. 
# It currently looks like:
#                         </div>
#                     </div>
#                 </div>
#             </div>
#         </div>
#     </section>
html = html.replace('                    </div>\n                </div>\n            </div>\n        </div>\n    </section>',
                    '                    </div>\n                </div>' + sidebar_html + '\n            </div>\n        </div>\n    </section>')

# Just to ensure group-hover-primary works, let's inject it if not in style.css
# But we already have group-hover-color maybe, let's check with standard inline logic or rely on existing utils.

with open("single-blog.html", "w") as f:
    f.write(html)
    
