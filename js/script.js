// Fairy Tale Child Care - Custom Interactions
document.addEventListener('DOMContentLoaded', () => {
    console.log('Fairy Tale Child Care site loaded');

    // 1. Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // 2. Mobile Menu Toggle
    const mobileBtn = document.querySelector('.mobile-menu-btn, .menu-t');
    const navMenu = document.querySelector('.nav-menu, nav');
    const icon = mobileBtn ? mobileBtn.querySelector('i, svg') : null;

    if (mobileBtn && navMenu) {
        mobileBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            const isActive = navMenu.classList.contains('active') || navMenu.style.display === 'block';

            if (isActive) {
                navMenu.classList.remove('active');
                navMenu.style.display = '';
            } else {
                navMenu.classList.add('active');
                if (window.innerWidth <= 768) {
                    navMenu.style.display = 'block';
                    navMenu.style.position = 'absolute';
                    navMenu.style.top = '100%';
                    navMenu.style.left = '0';
                    navMenu.style.width = '100%';
                    navMenu.style.background = '#fff';
                    navMenu.style.padding = '20px';
                    navMenu.style.boxShadow = '0 10px 20px rgba(0,0,0,0.1)';
                    const ul = navMenu.querySelector('ul');
                    if (ul) {
                        ul.style.flexDirection = 'column';
                        ul.style.gap = '15px';
                    }
                }
            }

            if (icon && icon.classList && icon.classList.contains('fas')) {
                if (navMenu.classList.contains('active')) {
                    icon.classList.remove('fa-bars');
                    icon.classList.add('fa-times');
                } else {
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            }
        });

        // Close menu when clicking a link
        navMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                navMenu.style.display = '';
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if ((navMenu.classList.contains('active') || navMenu.style.display === 'block') && !navMenu.contains(e.target) && !mobileBtn.contains(e.target)) {
                navMenu.classList.remove('active');
                navMenu.style.display = '';
            }
        });
    }

    // 3. Dynamic Year in Footer (if element exists)
    const yearSpan = document.getElementById('year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }

    // 4. Custom Fairy Cursor (Desktop Only) - DISABLED to show native cursor
    /*
    if (window.innerWidth > 768) {
        const cursor = document.createElement('div');
        cursor.className = 'custom-cursor';
        document.body.appendChild(cursor);

        // Initial state: hide cursor until first move
        cursor.style.opacity = '0';

        const updateCursor = (e) => {
            cursor.style.opacity = '1';
            const x = e.clientX;
            const y = e.clientY;

            cursor.style.left = x + 'px';
            cursor.style.top = y + 'px';

            // Create pixie dust particle
            const particle = document.createElement('div');
            particle.className = 'pixie-dust';

            // Randomize initial position slightly around the cursor
            const offset = 10;
            const px = x + (Math.random() * offset - offset / 2);
            const py = y + (Math.random() * offset - offset / 2);

            particle.style.left = px + 'px';
            particle.style.top = py + 'px';

            document.body.appendChild(particle);

            // Remove particle after animation ends
            setTimeout(() => {
                particle.remove();
            }, 800);
        };

        document.addEventListener('mousemove', updateCursor);

        // Handle mouse leaving/entering the window
        document.addEventListener('mouseleave', () => {
            cursor.style.opacity = '0';
        });

        document.addEventListener('mouseenter', () => {
            cursor.style.opacity = '1';
        });

        // Hover effect for interactive elements
        const interactables = document.querySelectorAll('a, button, .btn');
        interactables.forEach(el => {
            el.addEventListener('mouseenter', () => {
                cursor.style.transform = 'translate(-50%, -50%) scale(1.2) rotate(15deg)';
            });
            el.addEventListener('mouseleave', () => {
                cursor.style.transform = 'translate(-50%, -50%) scale(1) rotate(0deg)';
            });
        });
    }
    */

    // 5. Sticky Video Logic REMOVED per user request

    // 6. Gallery Slider Logic
    const slider = document.getElementById('photo-slider');
    const prevBtn = document.querySelector('.prev-arrow');
    const nextBtn = document.querySelector('.next-arrow');

    if (slider && prevBtn && nextBtn) {
        // Calculate scroll amount based on first item width
        const getScrollAmount = () => {
            const firstItem = slider.querySelector('.gallery-item');
            if (firstItem) {
                // width + gap
                return firstItem.offsetWidth + 18;
            }
            return 338; // fallback
        };

        const scrollSlider = (direction) => {
            const scrollAmount = getScrollAmount();
            let newScrollPosition = slider.scrollLeft + (direction * scrollAmount);
            
            // If we hit the end, loop back to start
            if (direction === 1 && newScrollPosition >= slider.scrollWidth - slider.clientWidth) {
                slider.scrollTo({ left: 0, behavior: 'smooth' });
            } 
            // If we hit the start and go backwards, loop to end
            else if (direction === -1 && slider.scrollLeft <= 0) {
                slider.scrollTo({ left: slider.scrollWidth, behavior: 'smooth' });
            } 
            // Normal scroll
            else {
                slider.scrollBy({ left: direction * scrollAmount, behavior: 'smooth' });
            }
        };

        // Arrow clicks
        prevBtn.addEventListener('click', () => scrollSlider(-1));
        nextBtn.addEventListener('click', () => scrollSlider(1));

        // Auto-scroll every 3.5 seconds
        let autoScrollTimer = setInterval(() => scrollSlider(1), 3500);

        // Pause auto-scroll when user interacts
        const pauseScroll = () => {
            clearInterval(autoScrollTimer);
        };
        
        const resumeScroll = () => {
            clearInterval(autoScrollTimer);
            autoScrollTimer = setInterval(() => scrollSlider(1), 3500);
        };

        slider.addEventListener('mouseenter', pauseScroll);
        slider.addEventListener('mouseleave', resumeScroll);
        slider.addEventListener('touchstart', pauseScroll, {passive: true});
        slider.addEventListener('touchend', resumeScroll);
    }

});
