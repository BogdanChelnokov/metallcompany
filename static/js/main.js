// static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    // Плавная прокрутка к секции при клике на категорию
    const categoryBtns = document.querySelectorAll('.category-btn');
    const productsSection = document.querySelector('.products-section');
    
    categoryBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Плавно скроллим к секции (только на мобильных)
            if (window.innerWidth <= 768) {
                setTimeout(() => {
                    productsSection.scrollIntoView({ 
                        behavior: 'smooth', 
                        block: 'start' 
                    });
                }, 100);
            }
        });
    });
    
    // Инициализация: загружаем первую категорию
    const firstActive = document.querySelector('.category-btn.active');
    if (firstActive) {
        // Триггерим клик для загрузки контента
        setTimeout(() => {
            firstActive.click();
        }, 200);
    }
});