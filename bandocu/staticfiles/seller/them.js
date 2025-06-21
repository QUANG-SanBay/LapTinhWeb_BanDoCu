document.querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Sản phẩm đã được thêm thành công!');
});

// Handle image upload
document.getElementById('image-upload').addEventListener('change', function(e) {
    const files = e.target.files;
    if (files.length > 0) {
        const uploadArea = document.querySelector('.upload-area');
        uploadArea.innerHTML = `
            <div class="upload-icon">
                <i class="fas fa-check-circle" style="color: #28a745;"></i>
            </div>
            <p class="upload-text">Đã chọn ${files.length} hình ảnh</p>
        `;
    }
});

// Handle video upload
document.getElementById('video-upload').addEventListener('change', function(e) {
    const file = e.target.files[0];
    if (file) {
        const uploadArea = document.querySelector('.video-upload-area');
        uploadArea.innerHTML = `
            <div class="upload-icon">
                <i class="fas fa-check-circle" style="color: #28a745;"></i>
            </div>
            <p class="upload-text">Đã chọn video: ${file.name}</p>
        `;
    }
});

// Function to show sua san pham page
function showSuaSanPham() {
    // This will be implemented when creating the sua-san-pham page
    alert('Chuyển đến trang sửa sản phẩm...');
}