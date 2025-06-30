
const avatarBtn = document.getElementById('avatarBtn');
const userDropdown = document.getElementById('userDropdown');

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
