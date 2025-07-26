// script.js

// ハンバーガーメニューの切り替え
document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.querySelector('.menu-toggle');
    const mainNav = document.querySelector('.main-nav');

    if (menuToggle && mainNav) {
        menuToggle.addEventListener('click', () => {
            mainNav.classList.toggle('is-active');
            // 必要であれば、ハンバーガーアイコン自体をX印に変えるアニメーションなどもここに追加
        });

        // 画面サイズが変更されたときにメニューの状態をリセット (PC表示になったらhiddenに戻す)
        window.addEventListener('resize', () => {
            if (window.innerWidth >= 768) { // Tailwindのmdブレークポイント
                mainNav.classList.remove('is-active');
            }
        });
    }

    // セクションのフェードインアニメーション (Intersection Observer APIを使用)
    const fadeElements = document.querySelectorAll('.fade-in-section');

    const observerOptions = {
        root: null, // ビューポートをルートとする
        rootMargin: '0px',
        threshold: 0.1 // 要素の10%が見えたらコールバックを実行
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target); // 一度アニメーションしたら監視を停止
            }
        });
    }, observerOptions);

    fadeElements.forEach(element => {
        observer.observe(element);
    });
});