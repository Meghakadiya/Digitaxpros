/**
 * Main Javascript for DigitalXPro
 */
document.addEventListener('DOMContentLoaded', () => {

    // 1. Initialize AOS (Animate On Scroll)
    AOS.init({
        duration: 1000,
        easing: 'ease-out-cubic',
        once: true, // whether animation should happen only once - while scrolling down
        offset: 50, // offset (in px) from the original trigger point
    });

    // 2. Navbar Scroll Effect & Styling swap
    const navbar = document.querySelector('.custom-navbar');
    const togglerIcon = document.querySelector('.navbar-toggler i');
    
    const handleScroll = () => {
        if (window.scrollY > 80) {
            navbar.classList.add('scrolled');
            if(togglerIcon) togglerIcon.classList.replace('text-white', 'text-primary');
        } else {
            navbar.classList.remove('scrolled');
            if(togglerIcon) togglerIcon.classList.replace('text-primary', 'text-white');
        }
    };
    
    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Trigger on load in case not at top

    // 3. Number Counter Animation (GSAP optional, using Vanilla JS for simplicity)
    const counters = document.querySelectorAll('.counter');
    const speed = 200; // lower is slower

    const animateCounters = () => {
        counters.forEach(counter => {
            const updateCount = () => {
                const target = +counter.getAttribute('data-target');
                const count = +counter.innerText;
                const inc = target / speed;

                if (count < target) {
                    counter.innerText = Math.ceil(count + inc);
                    setTimeout(updateCount, 15);
                } else {
                    counter.innerText = target + "+";
                }
            };
            
            // Only trigger when scrolled into view
            const rect = counter.getBoundingClientRect();
            if(rect.top < window.innerHeight && counter.innerText === '0') {
               updateCount();
            }
        });
    }
    
    window.addEventListener('scroll', animateCounters);

    // 4. Form Submission Simulation (Get a Quote Modal)
    const quoteForm = document.getElementById('quoteForm');
    const successMessage = document.getElementById('successMessage');
    
    // Custom Dropdown Logic
    const dropdownItems = document.querySelectorAll('.custom-select-option, .custom-select-dropdown .dropdown-item');
    dropdownItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const val = e.target.getAttribute('data-val');
            // Find parent dropdown
            const parentDropdown = e.target.closest('.dropdown');
            const btnText = parentDropdown.querySelector('button span');
            const hiddenInput = parentDropdown.querySelector('input[type="hidden"]');
            
            // Update text and value
            btnText.innerText = val;
            btnText.classList.remove('text-muted');
            btnText.classList.add('text-dark-main', 'fw-medium');
            if(hiddenInput) hiddenInput.value = val;
        });
    });

    if (quoteForm && successMessage) {
        quoteForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const submitBtn = quoteForm.querySelector('button[type="submit"]');
            const originalBtnContent = submitBtn.innerHTML;
            
            submitBtn.innerHTML = '<span class="position-relative z-1 d-flex justify-content-center align-items-center"><span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span> Submitting...</span>';
            submitBtn.disabled = true;

            // Simulate API Call
            setTimeout(() => {
                // Hide form, show success message
                quoteForm.classList.add('d-none');
                successMessage.classList.remove('d-none');
                successMessage.classList.add('d-flex');
                
                setTimeout(() => {
                    // Reset Form and UI completely silently after success finishes
                    const modalEl = document.getElementById('quoteModal');
                    const modal = bootstrap.Modal.getInstance(modalEl);
                    if (modal) {
                        modal.hide();
                    }
                    
                    // Allow modal closing animation to finish before resetting state visually
                    setTimeout(() => {
                        quoteForm.reset();
                        submitBtn.innerHTML = originalBtnContent;
                        submitBtn.disabled = false;
                        quoteForm.classList.remove('d-none');
                        successMessage.classList.add('d-none');
                        successMessage.classList.remove('d-flex');
                        
                        // Reset custom dropdowns
                        document.getElementById('serviceBtnText').innerText = 'Select Core Focus...';
                        document.getElementById('serviceBtnText').classList.add('text-muted');
                        document.getElementById('budgetBtnText').innerText = 'Select Budget...';
                        document.getElementById('budgetBtnText').classList.add('text-muted');
                        if(document.getElementById('serviceReq')) document.getElementById('serviceReq').value = '';
                        if(document.getElementById('budgetRange')) document.getElementById('budgetRange').value = '';
                    }, 400);

                }, 2500); // 2.5 seconds showing success screen
            }, 1000); // 1 second loading simulation
        });
    }

    // 4.1 Contact Page Form Submission (Standalone Section)
    const contactForm = document.getElementById('contactPageForm');
    const contactSuccessMsg = document.getElementById('contactSuccessMsg');
    
    if (contactForm && contactSuccessMsg) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const submitBtn = contactForm.querySelector('button[type="submit"]');
            const originalBtnContent = submitBtn.innerHTML;
            
            submitBtn.innerHTML = '<span class="position-relative z-1 d-flex justify-content-center align-items-center"><span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span> Sending...</span>';
            submitBtn.disabled = true;

            setTimeout(() => {
                // Hide form, show success
                contactForm.classList.add('d-none');
                contactSuccessMsg.classList.remove('d-none');
                contactSuccessMsg.classList.add('d-flex');
                
                setTimeout(() => {
                    // Reset everything silently
                    contactForm.reset();
                    submitBtn.innerHTML = originalBtnContent;
                    submitBtn.disabled = false;
                    contactForm.classList.remove('d-none');
                    contactSuccessMsg.classList.add('d-none');
                    contactSuccessMsg.classList.remove('d-flex');
                }, 4000); // Show success for 4 seconds
            }, 1200);
        });
    }

    // 5. Why Choose Us Card Interaction
    const whyCards = document.querySelectorAll('.why-card');
    whyCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            whyCards.forEach(c => {
                c.classList.remove('active');
                c.classList.add('bg-white');
            });
            card.classList.add('active');
            card.classList.remove('bg-white');
        });
    });
    
    // 6. GSAP subtle floating elements
    if(typeof gsap !== 'undefined') {
        gsap.to(".card-1", {
            y: 15,
            duration: 3,
            repeat: -1,
            yoyo: true,
            ease: "sine.inOut"
        });
        
        gsap.to(".card-2", {
            y: -20,
            x: 10,
            duration: 4,
            repeat: -1,
            yoyo: true,
            ease: "sine.inOut",
            delay: 1
        });
    }
    
    // 7. Lead Generation Toast Simulation
    const toastEl = document.getElementById('liveLeadToast');
    if (toastEl) {
        toastEl.classList.remove('hide'); // remove initial hide class
        const toast = new bootstrap.Toast(toastEl, {
            autohide: true,
            delay: 5000 // display for 5 seconds
        });
        
        const toastName = document.getElementById('toastName');
        const toastAction = document.getElementById('toastAction');

        const leads = [
            { name: "Michael R. (Dentist)", action: "Just requested a Free Growth Audit." },
            { name: "Sarah L. (Real Estate)", action: "Just booked a Strategy Call." },
            { name: "David K. (Plumbing)", action: "Upgraded to our Local SEO package." },
            { name: "Amanda W. (Spa Owner)", action: "Started a Google Ads campaign." },
            { name: "James T. (Lawyer)", action: "Requested a quote for Review Management." }
        ];

        const showNextLead = () => {
            // Pick a random lead
            const lead = leads[Math.floor(Math.random() * leads.length)];
            
            // Update toast HTML
            if (toastName) toastName.innerText = lead.name;
            if (toastAction) toastAction.innerText = lead.action;
            
            toast.show();
        };

        // Show first lead after 3 seconds
        setTimeout(() => {
            showNextLead();
            
            // Continue showing random leads every 10 seconds
            setInterval(() => {
                showNextLead();
            }, 10000);
        }, 3000);
    }

    // 8. Scroll To Top Button Logic
    const scrollTopBtn = document.getElementById('scrollToTopBtn');
    if (scrollTopBtn) {
        // Toggle visibility on scroll
        window.addEventListener('scroll', () => {
            if (window.scrollY > 400) {
                scrollTopBtn.style.opacity = '1';
                scrollTopBtn.style.visibility = 'visible';
                scrollTopBtn.style.transform = 'translateY(0)';
            } else {
                scrollTopBtn.style.opacity = '0';
                scrollTopBtn.style.visibility = 'hidden';
                scrollTopBtn.style.transform = 'translateY(20px)';
            }
        });

        // Scroll smoothly to top on click
        scrollTopBtn.addEventListener('click', (e) => {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

});
