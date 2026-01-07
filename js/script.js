// Language Switching Functionality
let currentLanguage = 'en';

function switchLanguage(lang) {
    currentLanguage = lang;

    // Update active button
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    document.getElementById(`lang-${lang}`).classList.add('active');

    // Update all elements with language attributes
    const elements = document.querySelectorAll('[data-en]');
    elements.forEach(element => {
        const content = element.getAttribute(`data-${lang}`);
        if (content) {
            // Check if it's a button or link
            if (element.tagName === 'A' || element.tagName === 'BUTTON') {
                element.textContent = content;
            } else {
                element.textContent = content;
            }
        }
    });

    // Save language preference
    localStorage.setItem('preferredLanguage', lang);
}

// Load saved language preference
document.addEventListener('DOMContentLoaded', () => {
    const savedLanguage = localStorage.getItem('preferredLanguage') || 'en';
    switchLanguage(savedLanguage);

    // Add smooth scroll behavior
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });

                // Close mobile menu if open
                navMenu.classList.remove('active');
            }
        });
    });
});

// Mobile Menu Toggle
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

hamburger.addEventListener('click', () => {
    navMenu.classList.toggle('active');

    // Animate hamburger
    hamburger.classList.toggle('active');
});

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-menu a').forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        hamburger.classList.remove('active');
    });
});

// Navbar scroll effect
let lastScroll = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll <= 0) {
        navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
    } else {
        navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.15)';
    }

    lastScroll = currentScroll;
});

// Intersection Observer for fade-in animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe all sections and cards
document.addEventListener('DOMContentLoaded', () => {
    const animatedElements = document.querySelectorAll(
        '.project-card, .skill-category, .timeline-item, .stat-card, .contact-card'
    );

    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});

// Active navigation link on scroll
const sections = document.querySelectorAll('section[id]');

function highlightNavigation() {
    const scrollY = window.pageYOffset;

    sections.forEach(section => {
        const sectionHeight = section.offsetHeight;
        const sectionTop = section.offsetTop - 100;
        const sectionId = section.getAttribute('id');
        const navLink = document.querySelector(`.nav-menu a[href="#${sectionId}"]`);

        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            navLink?.classList.add('active');
        } else {
            navLink?.classList.remove('active');
        }
    });
}

window.addEventListener('scroll', highlightNavigation);

// Typing effect for hero subtitle (optional enhancement)
function typeWriter(element, text, speed = 100) {
    let i = 0;
    element.textContent = '';

    function type() {
        if (i < text.length) {
            element.textContent += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }

    type();
}

// Performance optimization: Debounce scroll events
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Apply debounce to scroll handlers
window.addEventListener('scroll', debounce(highlightNavigation, 100));

// Add loading animation
window.addEventListener('load', () => {
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s ease';
        document.body.style.opacity = '1';
    }, 100);
});

// Keyboard navigation support
document.addEventListener('keydown', (e) => {
    // Press 'L' to toggle language
    if (e.key === 'l' || e.key === 'L') {
        const newLang = currentLanguage === 'en' ? 'de' : 'en';
        switchLanguage(newLang);
    }
});

// Copy email to clipboard functionality
document.querySelectorAll('.contact-card a[href^="mailto:"]').forEach(emailLink => {
    emailLink.addEventListener('click', (e) => {
        e.preventDefault();
        const email = emailLink.textContent;

        // Create temporary input
        const tempInput = document.createElement('input');
        tempInput.value = email;
        document.body.appendChild(tempInput);
        tempInput.select();
        document.execCommand('copy');
        document.body.removeChild(tempInput);

        // Show feedback
        const originalText = emailLink.textContent;
        emailLink.textContent = currentLanguage === 'en' ? 'Copied!' : 'Kopiert!';
        emailLink.style.color = '#10b981';

        setTimeout(() => {
            emailLink.textContent = originalText;
            emailLink.style.color = '';
        }, 2000);
    });
});

// Print resume functionality (for future implementation)
function printResume() {
    window.print();
}

// Dark mode toggle (optional feature for future)
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
}

// Analytics event tracking (placeholder for future integration)
function trackEvent(category, action, label) {
    // Placeholder for Google Analytics or other tracking
    console.log(`Event: ${category} - ${action} - ${label}`);
}

// Track project card clicks
document.querySelectorAll('.project-card').forEach(card => {
    card.addEventListener('click', () => {
        const projectName = card.querySelector('h3').textContent;
        trackEvent('Projects', 'View', projectName);
    });
});

// Track contact link clicks
document.querySelectorAll('.contact-card a').forEach(link => {
    link.addEventListener('click', () => {
        const contactType = link.closest('.contact-card').querySelector('h3').textContent;
        trackEvent('Contact', 'Click', contactType);
    });
});

// Add skill tag interaction
document.querySelectorAll('.skill-tag').forEach(tag => {
    tag.addEventListener('click', () => {
        tag.style.transform = 'scale(1.1)';
        setTimeout(() => {
            tag.style.transform = '';
        }, 200);
    });
});

// Parallax effect for hero section (subtle)
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const hero = document.querySelector('.hero');
    if (hero) {
        hero.style.transform = `translateY(${scrolled * 0.5}px)`;
    }
});

// Console message for developers
console.log('%c👋 Hello, Developer!', 'color: #2563eb; font-size: 20px; font-weight: bold;');
console.log('%cInterested in how this portfolio was built?', 'color: #6b7280; font-size: 14px;');
console.log('%cFeel free to reach out at abjha1998@gmail.com', 'color: #6b7280; font-size: 14px;');
