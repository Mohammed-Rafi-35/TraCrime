const SOS_btn = document.getElementById('SOS_btn');

let count = 0;

SOS_btn.addEventListener('click', () => {
    setTimeout(() => {
        alert('SOS Alerted! Be Safe');
    }, 1000)

    while(1) {
        count += 1;
        setTimeout(()=> {
            SOS_btn.style.transitionm = 'all 1s ease';
            SOS_btn.style.boxShadow = '0px 0px 0px red;';
        }, 10000)
        setTimeout(()=> {
            SOS_btn.style.transitionm = 'all 1s ease';
            SOS_btn.style.boxShadow = '0px 0px 200px red;';
        }, 10000)
        if(count >= 10){ 
            console.log('Hello');
            break;
           
        }
    }
});