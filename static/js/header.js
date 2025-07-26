// script.js

document.addEventListener('DOMContentLoaded', () => {
    const hamburgerButton = document.getElementById('hamburgerButton');
    const mainNavigation = document.getElementById('mainNavigation');

    if (hamburgerButton && mainNavigation) {
        hamburgerButton.addEventListener('click', () => {
            // mainNavigationに'is-open'クラスを追加したり削除したりする
            mainNavigation.classList.toggle('is-open');

            // アクセシビリティのためにaria-expanded属性を切り替える
            const isExpanded = hamburgerButton.getAttribute('aria-expanded') === 'true';
            hamburgerButton.setAttribute('aria-expanded', !isExpanded);
        });
    }
});