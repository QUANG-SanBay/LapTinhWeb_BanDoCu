{
    const productImg = document.querySelectorAll('.product__img-item');
    productImg.forEach((item) => {
        item.addEventListener('click', () => {
            const imgSrc = item.querySelector('img').getAttribute('src');
            const mainImg = document.querySelector('.product__img-main img');
            if (imgSrc !== mainImg.getAttribute('src')) {
                mainImg.setAttribute('src', imgSrc);
                productImg.forEach((img) => img.classList.remove('active'));
                item.classList.add('active');
            }
        });
    });
}
document.addEventListener('DOMContentLoaded', function () {
    const minusBtn = document.querySelector('.product__infor-quantity-btn-minus');
    const plusBtn = document.querySelector('.product__infor-quantity-btn-plus');
    const numberSpan = document.querySelector('.product__infor-quantity-number');

    minusBtn.addEventListener('click', function () {
        let current = parseInt(numberSpan.textContent, 10);
        if (current > 1) {
            numberSpan.textContent = current - 1;
        }
    });

    plusBtn.addEventListener('click', function () {
        let current = parseInt(numberSpan.textContent, 10);
        numberSpan.textContent = current + 1;
    });
});