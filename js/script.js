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

    // 4. Custom Fairy Cursor
    const cursor = document.createElement('div');
    cursor.className = 'custom-cursor';
    document.body.appendChild(cursor);

    document.addEventListener('mousemove', (e) => {
        cursor.style.left = e.clientX + 'px';
        cursor.style.top = e.clientY + 'px';

        // Create pixie dust particle
        const particle = document.createElement('div');
        particle.className = 'pixie-dust';

        // Randomize initial position slightly around the cursor
        const offset = 10;
        const x = e.clientX + (Math.random() * offset - offset / 2);
        const y = e.clientY + (Math.random() * offset - offset / 2);

        particle.style.left = x + 'px';
        particle.style.top = y + 'px';

        document.body.appendChild(particle);

        // Remove particle after animation ends
        setTimeout(() => {
            particle.remove();
        }, 800);
    });

    // Handle mouse leaving the window
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
});
