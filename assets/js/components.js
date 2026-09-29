// components.js - Automatically handle header and footer across all pages

class AppHeader extends HTMLElement {
    connectedCallback() {
        const basePath = this.getAttribute('base-path') || './';
        
        this.innerHTML = `
    <nav id="mainNav" class="navbar navbar-expand-lg fixed-top custom-navbar mt-3 mx-lg-auto rounded-pill glass-nav"
        style="max-width: 1200px; right: 15px; left: 15px;">
        <div class="container">
            <a class="navbar-brand fw-bold logo-text" href="${basePath}index.html">DigitalX<span class="text-primary-light">Pro</span></a>
            <button class="navbar-toggler border-0 focus-ring" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarContent">
                <i class="bi bi-list fs-1 text-primary"></i>
            </button>
            <div class="collapse navbar-collapse" id="navbarContent">
                <ul class="navbar-nav mx-auto mb-2 mb-lg-0 gap-3">
                    <li class="nav-item"><a class="nav-link" href="${basePath}index.html#home">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="${basePath}index.html#about">About</a></li>
                    <li class="nav-item"><a class="nav-link" href="${basePath}index.html#projects">Results</a></li>
                    <li class="nav-item"><a class="nav-link" href="${basePath}index.html#industries">Industries</a></li>
                    <li class="nav-item dropdown dropdown-hover">
                        <a class="nav-link dropdown-toggle" href="${basePath}index.html#services" role="button" data-bs-toggle="dropdown"
                            aria-expanded="false">Services</a>
                        <ul class="dropdown-menu border-0 shadow-lg border-primary border-top border-3 rounded-4 animate-dropdown m-0 mt-2 p-2 glass-dropdown">
                            <li><a class="dropdown-item py-2 fw-medium rounded text-dark-main" href="${basePath}services/google-business-profile.html">Google Business Profile</a></li>
                            <li><a class="dropdown-item py-2 fw-medium rounded text-dark-main" href="${basePath}services/google-ads-management.html">Google Ads & AdSense</a></li>
                            <li><a class="dropdown-item py-2 fw-medium rounded text-dark-main" href="${basePath}services/local-seo.html">Local SEO</a></li>
                            <li><a class="dropdown-item py-2 fw-medium rounded text-dark-main" href="${basePath}services/review-management.html">Review Management</a></li>
                            <li><a class="dropdown-item py-2 fw-medium rounded text-dark-main" href="${basePath}services/lead-generation.html">Lead Generation</a></li>
                            <li><a class="dropdown-item py-2 fw-medium rounded text-dark-main" href="${basePath}services/lead-automation.html">Lead Automation</a></li>
                            <li><hr class="dropdown-divider opacity-10 my-2"></li>
                            <li><a href="${basePath}services.html" class="dropdown-item py-2 fw-bold text-primary text-center bg-light rounded d-flex justify-content-center align-items-center transition-all hover-scale shadow-sm" style="font-size: 0.9rem;">View All Services <i class="bi bi-arrow-right ms-2"></i></a></li>
                        </ul>
                    </li>
                    <li class="nav-item"><a class="nav-link" href="${basePath}blog.html">Blog</a></li>
                    <li class="nav-item"><a class="nav-link" href="${basePath}contact.html">Contact</a></li>
                </ul>
                <button class="btn btn-primary rounded-pill px-4 py-2 fw-semibold shadow-sm pulse-btn"
                    data-bs-toggle="modal" data-bs-target="#quoteModal">Free Audit</button>
            </div>
        </div>
    </nav>
        `;
    }
}

class AppFooter extends HTMLElement {
    connectedCallback() {
        const basePath = this.getAttribute('base-path') || './';
        
        this.innerHTML = `
    <footer class="footer pt-0 pb-4 bg-dark-main text-white position-relative overflow-hidden border-0 mt-0">
        <!-- White Wave Top Divider -->
        <div class="position-absolute w-100" style="top: -1px; left: 0; line-height: 0; z-index: 2;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320" style="width: 100%; height: auto; display: block;">
                <path fill="#ffffff" fill-opacity="1" d="M0,96L80,106.7C160,117,320,139,480,128C640,117,800,75,960,69.3C1120,64,1280,96,1360,112L1440,128V0L1360,0C1280,0,1120,0,960,0C800,0,640,0,480,0C320,0,160,0,80,0L0,0Z"></path>
            </svg>
        </div>

        <!-- Background Shapes -->
        <div class="glow-orb" style="width: 400px; height: 400px; background: rgba(37, 211, 102, 0.1); bottom: -100px; right: -100px; z-index: 0;"></div>
        <div class="glow-orb" style="width: 300px; height: 300px; background: rgba(255, 255, 255, 0.05); top: -50px; left: -50px; z-index: 0;"></div>
        
        <!-- Subtle Pattern Overlay -->
        <div class="position-absolute w-100 h-100" style="top: 0; left: 0; background-image: radial-gradient(rgba(255,255,255,0.05) 1px, transparent 1px); background-size: 30px 30px; opacity: 0.4; z-index: 0;"></div>

        <div class="container position-relative z-1 pt-5" style="margin-top: 10vw;">
            <div class="row g-5 mb-5 pb-5 border-bottom border-white border-opacity-10 justify-content-between">
                <!-- Brand Info -->
                <div class="col-lg-4 pe-lg-5">
                    <a class="navbar-brand fw-bold fs-3 text-white logo-text d-flex align-items-center mb-4" href="${basePath}services/comprehensive-marketing.html">
                        <i class="bi bi-hexagon-fill me-2 fs-2 text-primary"></i>
                        DigitalXPro
                    </a>
                    <p class="text-white-75 mb-4 small" style="line-height: 1.8;">
                        Your elite growth partner for local dominance. We build high-converting systems, 
                        manage reviews, and scale service businesses.
                    </p>
                    <div class="d-flex flex-column gap-3 mb-4">
                        <a href="mailto:hello@digitalxpro.com" class="text-white text-decoration-none small transition-all d-flex align-items-center">
                            <div class="bg-white bg-opacity-10 rounded-circle d-flex align-items-center justify-content-center me-3 hover-scale hover-bg-primary" style="width: 38px; height: 38px; transition: all 0.3s;">
                                <i class="bi bi-envelope-fill text-primary" style="transition: color 0.3s;"></i>
                            </div>
                            hello@digitalxpro.com
                        </a>
                        <span class="text-white text-decoration-none small d-flex align-items-center">
                            <div class="bg-white bg-opacity-10 rounded-circle d-flex align-items-center justify-content-center me-3 hover-scale hover-bg-primary" style="width: 38px; height: 38px; transition: all 0.3s;">
                                <i class="bi bi-telephone-fill text-primary" style="transition: color 0.3s;"></i>
                            </div>
                            +91 8488905688
                        </span>
                    </div>
                </div>

                <!-- Quick Links -->
                <div class="col-lg-2 col-md-4 col-sm-6">
                    <h6 class="fw-bold mb-4 text-uppercase tracking-wider small text-white">Company</h6>
                    <ul class="list-unstyled footer-links mb-0 gap-3 d-flex flex-column">
                        <li><a href="${basePath}index.html#home" class="text-white text-decoration-none small transition-all hover-white d-flex align-items-center"><i class="bi bi-chevron-right me-2 small text-white"></i> Home</a></li>
                        <li><a href="${basePath}index.html#about" class="text-white text-decoration-none small transition-all hover-white d-flex align-items-center"><i class="bi bi-chevron-right me-2 small text-white"></i> About Us</a></li>
                        <li><a href="${basePath}blog.html" class="text-white text-decoration-none small transition-all hover-white d-flex align-items-center"><i class="bi bi-chevron-right me-2 small text-white"></i> Our Blog</a></li>
                        <li><a href="${basePath}contact.html" class="text-white text-decoration-none small transition-all hover-white d-flex align-items-center"><i class="bi bi-chevron-right me-2 small text-white"></i> Contact Us</a></li>
                    </ul>
                </div>

                <!-- Services Column 1 -->
                <div class="col-lg-3 col-md-4 col-sm-6">
                    <h6 class="fw-bold mb-4 text-uppercase tracking-wider small text-white">SERVICES</h6>
                    <ul class="list-unstyled footer-links mb-0 gap-3 d-flex flex-column">
                        <li><a href="${basePath}services/google-business-profile.html" class="text-white text-decoration-none small transition-all hover-white d-flex align-items-center"><i class="bi bi-chevron-right me-2 small text-white"></i> Google Profile</a></li>
                        <li><a href="${basePath}services/local-seo.html" class="text-white text-decoration-none small transition-all hover-white d-flex align-items-center"><i class="bi bi-chevron-right me-2 small text-white"></i> Local SEO</a></li>
                        <li><a href="${basePath}services/google-ads-management.html" class="text-white text-decoration-none small transition-all hover-white d-flex align-items-center"><i class="bi bi-chevron-right me-2 small text-white"></i> Google Ads</a></li>
                        <li><a href="${basePath}services/review-management.html" class="text-white text-decoration-none small transition-all hover-white d-flex align-items-center"><i class="bi bi-chevron-right me-2 small text-white"></i> Review Mgmt</a></li>
                    </ul>
                </div>

                <!-- Services Column 2 -->
                <div class="col-lg-3 col-md-4 col-sm-6">
                    <h6 class="fw-bold mb-4 text-uppercase tracking-wider small opacity-0 d-none d-md-block">SERVICES</h6>
                    <h6 class="fw-bold mb-4 text-uppercase tracking-wider small text-white d-md-none">SERVICES</h6>
                    <ul class="list-unstyled footer-links mb-0 gap-3 d-flex flex-column">
                        <li><a href="${basePath}services/lead-generation.html" class="text-white text-decoration-none small transition-all hover-white d-flex align-items-center"><i class="bi bi-chevron-right me-2 small text-white"></i> Lead Funnels</a></li>
                        <li><a href="${basePath}services/lead-automation.html" class="text-white text-decoration-none small transition-all hover-white d-flex align-items-center"><i class="bi bi-chevron-right me-2 small text-white"></i> Lead Automation</a></li>
                        <li><a href="${basePath}services/whatsapp-automation.html" class="text-white text-decoration-none small transition-all hover-white d-flex align-items-center"><i class="bi bi-chevron-right me-2 small text-white"></i> WhatsApp Bot</a></li>
                        <li><a href="${basePath}services/comprehensive-marketing.html" class="text-white text-decoration-none small transition-all hover-white d-flex align-items-center"><i class="bi bi-chevron-right me-2 small text-white"></i> 360 Marketing</a></li>
                    </ul>
                </div>
                
            </div>

            <!-- Bottom Sub-Footer -->
            <div class="row align-items-center">
                <div class="col-md-6 text-center text-md-start mb-3 mb-md-0">
                    <p class="text-white-50 small mb-0">&copy; 2026 DigitalXPro. All rights reserved.</p>
                </div>
                <div class="col-md-6 text-center text-md-end">
                    <div class="d-flex gap-2 justify-content-center justify-content-md-end">
                        <a href="https://facebook.com" target="_blank" class="text-white-50 hover-white bg-white bg-opacity-10 rounded-circle d-flex align-items-center justify-content-center transition-all hover-bg-primary" style="width: 36px; height: 36px;"><i class="bi bi-facebook small"></i></a>
                        <a href="https://instagram.com" target="_blank" class="text-white-50 hover-white bg-white bg-opacity-10 rounded-circle d-flex align-items-center justify-content-center transition-all hover-bg-primary" style="width: 36px; height: 36px;"><i class="bi bi-instagram small"></i></a>
                        <a href="https://twitter.com" target="_blank" class="text-white-50 hover-white bg-white bg-opacity-10 rounded-circle d-flex align-items-center justify-content-center transition-all hover-bg-primary" style="width: 36px; height: 36px;"><i class="bi bi-twitter-x small"></i></a>
                        <a href="https://linkedin.com" target="_blank" class="text-white-50 hover-white bg-white bg-opacity-10 rounded-circle d-flex align-items-center justify-content-center transition-all hover-bg-primary" style="width: 36px; height: 36px;"><i class="bi bi-linkedin small"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </footer>
        `;
    }
}

customElements.define('app-header', AppHeader);
customElements.define('app-footer', AppFooter);
