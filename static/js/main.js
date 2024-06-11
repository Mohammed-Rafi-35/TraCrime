const navbar = document.getElementById('navbar');
const navbar_btn = document.getElementById('navbar_btn');

let navbar_expanded = false;

navbar_btn.addEventListener('click', () => {
    if( navbar_expanded == false) {
        navbar.style.height = '10vh';
        navbar_expanded = true;
    }
    else {
        navbar.style.height = '4.5vh';
        navbar_expanded = false;
    }
});