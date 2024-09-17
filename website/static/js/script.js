// Get the nav links and menu icons
var navLinks = document.getElementById("navLinks");
var openMenuIcon = document.querySelector(".fa-bars");  // Mobile menu (hamburger) icon
var closeMenuIcon = document.querySelector(".fa-times");  // Close icon

// Show the mobile menu (when hamburger is clicked)
function showMenu() {
    navLinks.classList.add("show"); // Slide the nav into view
    navLinks.style.right = "0"; // Ensure it slides in from the right
    closeMenuIcon.style.display = "block"; // Show close icon
    openMenuIcon.style.display = "none"; // Hide hamburger icon
}

// Hide the mobile menu (when close icon is clicked)
function hideMenu() {
    navLinks.classList.remove("show"); // Hide the nav
    navLinks.style.right = "-250px";  // Slide it off the screen to the right
    closeMenuIcon.style.display = "none"; // Hide close icon
    openMenuIcon.style.display = "block"; // Show hamburger icon again
}

// Event listeners to handle clicks
openMenuIcon.addEventListener("click", showMenu);  // Handle hamburger menu click
closeMenuIcon.addEventListener("click", hideMenu);  // Handle close icon click

// Function to prevent dropdowns from overflowing off the screen
function preventOverflow() {
    const dropdowns = document.querySelectorAll('.dropdown-menu, .dropdown-menu-1');

    dropdowns.forEach(dropdown => {
        const rect = dropdown.getBoundingClientRect();
        const isOverflowing = rect.right > window.innerWidth;

        if (isOverflowing) {
            dropdown.classList.add('is-overflowing');
        } else {
            dropdown.classList.remove('is-overflowing');
        }
    });
}

// Add an event listener for window resizing to prevent overflow
window.addEventListener('resize', preventOverflow);

// Ensure the overflow is checked when the page loads
document.addEventListener('DOMContentLoaded', preventOverflow);

// Function to check if an element overflows outside the window bounds
function checkOverflow(element) {
    const rect = element.getBoundingClientRect();
    return rect.right > window.innerWidth || rect.left < 0;
}

// Apply the overflow check when hovering over dropdowns
document.querySelectorAll('.nav-links ul li .dropdown-menu').forEach(dropdown => {
    dropdown.addEventListener('mouseover', function () {
        this.classList.remove('is-overflowing');
        if (checkOverflow(this)) {
            this.classList.add('is-overflowing');
        }
    });

    dropdown.querySelectorAll('.dropdown-menu-1').forEach(subDropdown => {
        subDropdown.addEventListener('mouseover', function () {
            this.classList.remove('is-overflowing');
            if (checkOverflow(this)) {
                this.classList.add('is-overflowing');
            }
        });
    });
});

// Function to handle scroll-based actions for specific sections
document.addEventListener('scroll', function () {
    const aboutSection = document.querySelector('.about-section');
    const linkItems = document.querySelectorAll('.link-item');

    const triggerPoint = window.innerHeight * 0.7; // Adjust as necessary

    // Check if About Section is in view
    if (aboutSection && aboutSection.getBoundingClientRect().top < triggerPoint) {
        aboutSection.classList.add('scrolled');
    }

    // Check if individual link items are in view
    linkItems.forEach(item => {
        if (item.getBoundingClientRect().top < triggerPoint) {
            item.classList.add('scrolled');
        }
    });
});
