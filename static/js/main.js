// GRUPO COINP - Main JS

document.addEventListener('DOMContentLoaded', () => {

    // ===== NAVBAR: scroll effect =====
    const header = document.querySelector('header');
    if (header) {
        const onScroll = () => {
            header.classList.toggle('scrolled', window.scrollY > 20);
        };
        window.addEventListener('scroll', onScroll, { passive: true });
    }

    // ===== NAVBAR: hamburger menu =====
    const toggle = document.querySelector('.nav-toggle');
    const navLinks = document.querySelector('.nav-links');
    if (toggle && navLinks) {
        toggle.addEventListener('click', () => {
            const open = navLinks.classList.toggle('open');
            toggle.classList.toggle('open', open);
            toggle.setAttribute('aria-expanded', open);
        });

        // Close on outside click
        document.addEventListener('click', (e) => {
            if (!toggle.contains(e.target) && !navLinks.contains(e.target)) {
                navLinks.classList.remove('open');
                toggle.classList.remove('open');
            }
        });

        // Close on nav link click (mobile)
        navLinks.querySelectorAll('a').forEach(a => {
            a.addEventListener('click', () => {
                navLinks.classList.remove('open');
                toggle.classList.remove('open');
            });
        });
    }

    // ===== SCROLL REVEAL with IntersectionObserver =====
    const revealEls = document.querySelectorAll('.reveal, .reveal-stagger');
    if (revealEls.length > 0 && 'IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

        revealEls.forEach(el => observer.observe(el));
    } else {
        // Fallback: show all immediately
        revealEls.forEach(el => el.classList.add('visible'));
    }

    // ===== SMOOTH ANCHOR SCROLL =====
    document.querySelectorAll('a[href^="#"]').forEach(a => {
        a.addEventListener('click', e => {
            const target = document.querySelector(a.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // ===== CATEGORY FILTER CHIPS =====
    const chips = document.querySelectorAll('.chip[data-category]');
    const productCards = document.querySelectorAll('.product-card-item[data-category]');

    if (chips.length > 0 && productCards.length > 0) {
        chips.forEach(chip => {
            chip.addEventListener('click', () => {
                chips.forEach(c => c.classList.remove('active'));
                chip.classList.add('active');
                const cat = chip.dataset.category;

                productCards.forEach(card => {
                    const show = cat === 'all' || card.dataset.category === cat;
                    card.style.transition = 'opacity 0.3s, transform 0.3s';
                    if (show) {
                        card.style.display = '';
                        requestAnimationFrame(() => {
                            card.style.opacity = '1';
                            card.style.transform = 'translateY(0)';
                        });
                    } else {
                        card.style.opacity = '0';
                        card.style.transform = 'translateY(10px)';
                        setTimeout(() => { if (card.style.opacity === '0') card.style.display = 'none'; }, 310);
                    }
                });
            });
        });
    }

    // ===== COUNTER ANIMATION for stats =====
    const statNumbers = document.querySelectorAll('.stat-number[data-target]');
    if (statNumbers.length > 0 && 'IntersectionObserver' in window) {
        const countObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounter(entry.target);
                    countObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        statNumbers.forEach(el => countObserver.observe(el));
    }

    function animateCounter(el) {
        const target = parseInt(el.dataset.target, 10);
        const suffix = el.dataset.suffix || '';
        const duration = 1600;
        const step = 16;
        const increment = target / (duration / step);
        let current = 0;
        const timer = setInterval(() => {
            current = Math.min(current + increment, target);
            el.textContent = Math.floor(current) + suffix;
            if (current >= target) clearInterval(timer);
        }, step);
    }

    // ===== QUANTITY INPUT: +/- buttons =====
    document.querySelectorAll('.qty-wrapper').forEach(wrap => {
        const input = wrap.querySelector('input[type="number"]');
        const btnMinus = wrap.querySelector('.qty-minus');
        const btnPlus = wrap.querySelector('.qty-plus');
        if (!input) return;

        if (btnMinus) btnMinus.addEventListener('click', () => {
            const min = parseInt(input.min || '1', 10);
            if (parseInt(input.value) > min) input.value = parseInt(input.value) - 1;
        });

        if (btnPlus) btnPlus.addEventListener('click', () => {
            const max = parseInt(input.max || '9999', 10);
            if (parseInt(input.value) < max) input.value = parseInt(input.value) + 1;
        });
    });

    // ===== ACTIVE NAV LINK =====
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-links a').forEach(a => {
        const href = a.getAttribute('href');
        if (href && href !== '/' && currentPath.startsWith(href)) {
            a.classList.add('active');
        } else if (href === '/' && currentPath === '/') {
            a.classList.add('active');
        }
    });

});
