// Filter button active state
document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
    });
});

// Product actions
// Edit
document.querySelectorAll('.edit-btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
        e.preventDefault();
        alert('Chức năng chỉnh sửa sản phẩm');
    });
});
// Delete

// Animation for fadeOut
const style = document.createElement('style');
style.innerHTML = `
@keyframes fadeOut { from { opacity: 1; } to { opacity: 0; transform: scale(0.95); } }
@keyframes fadeInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: none; } }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
`;
document.head.appendChild(style);

document.querySelectorAll('.delete-btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
        e.preventDefault();
        if(confirm('Bạn có chắc chắn muốn xóa sản phẩm này?')) {
            this.closest('.seller-product-card').style.animation = 'fadeOut 0.3s ease forwards';
            setTimeout(() => {
                this.closest('.seller-product-card').remove();
            }, 300);
        }
    });
});

// Search functionality
const searchInput = document.querySelector('.seller-header__search input');
if (searchInput) {
    searchInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase();
        document.querySelectorAll('.seller-product-card').forEach(card => {
            const productName = card.querySelector('.seller-product-name').textContent.toLowerCase();
            if (productName.includes(searchTerm)) {
                card.style.display = 'block';
                card.style.animation = 'fadeInUp 0.3s ease forwards';
            } else {
                card.style.display = 'none';
            }
        });
    });
}

// Add smooth scrolling
Array.from(document.querySelectorAll('a[href^="#"]')).forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Add loading animation
window.addEventListener('load', function() {
    document.body.style.opacity = '0';
    document.body.style.animation = 'fadeIn 0.5s ease forwards';
});

// Sidebar mobile menu
const sidebar = document.getElementById('sellerSidebar');
const sidebarOverlay = document.getElementById('sidebarOverlay');
const sidebarOpenBtn = document.querySelector('.header-menu');
const sidebarCloseBtn = document.getElementById('sidebarCloseBtn');

function openSidebar() {
    sidebar.classList.add('open');
    sidebarOverlay.classList.add('open');
    document.body.style.overflow = 'hidden';
}
function closeSidebar() {
    sidebar.classList.remove('open');
    sidebarOverlay.classList.remove('open');
    document.body.style.overflow = '';
}
if (sidebarOpenBtn && sidebar && sidebarOverlay && sidebarCloseBtn) {
    sidebarOpenBtn.addEventListener('click', openSidebar);
    sidebarCloseBtn.addEventListener('click', closeSidebar);
    sidebarOverlay.addEventListener('click', closeSidebar);
}