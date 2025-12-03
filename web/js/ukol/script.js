document.addEventListener('DOMContentLoaded', () => {
    const sachovnice = document.getElementById('sachovnice');
    const btn = document.getElementById('btn');
    const num = document.getElementById('num');

    btn.onclick = (event) => {
        event.preventDefault();
        let n = parseInt(num.value);
        if (isNaN(n) || n <= 0) return;

        sachovnice.style.setProperty('--size', n);
        sachovnice.innerHTML = ''; 
        
        sachovnice.innerHTML = '';
        for (let r = 0; r < n; r++) {
            for (let c = 0; c < n; c++) {
                let pole = document.createElement('div');
                pole.className = ((r + c) % 2 === 0) ? 'black' : 'white';
                sachovnice.appendChild(pole);
            }
        }
    };
});
