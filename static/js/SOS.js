const SOS_btn = document.getElementById('SOS_btn');

let count = 0;

SOS_btn.addEventListener('click', () => {
    setTimeout(() => {
        alert('SOS Alerted! Be Safe');
    }, 1000)
});