// Dropdown functionality
const avatarBtn = document.getElementById('avatarBtn');
const userDropdown = document.getElementById('userDropdown');
const searchInput = document.getElementById('searchInput');
const clearBtn = document.getElementById('clearBtn');
const searchBtn = document.getElementById('searchBtn');

// Toggle dropdown
avatarBtn.addEventListener('click', function(e) {
    e.stopPropagation();
    userDropdown.classList.toggle('show');
});

// Close dropdown when clicking outside
document.addEventListener('click', function(e) {
    if (!userDropdown.contains(e.target) && !avatarBtn.contains(e.target)) {
        userDropdown.classList.remove('show');
    }
});

// Search functionality
searchInput.addEventListener('input', function() {
    if (this.value.length > 0) {
        clearBtn.classList.add('show');
    } else {
        clearBtn.classList.remove('show');
    }
});

clearBtn.addEventListener('click', function() {
    searchInput.value = '';
    clearBtn.classList.remove('show');
    searchInput.focus();
});

searchBtn.addEventListener('click', function() {
    if (searchInput.value.trim()) {
        console.log('Searching for:', searchInput.value);
        // Add your search logic here
    }
});

searchInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter' && this.value.trim()) {
        console.log('Searching for:', this.value);
        // Add your search logic here
    }
});