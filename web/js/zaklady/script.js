for (let i = 0; i <8; i++) {
    console.log(2 ** i);
}


for (let i = 1; i <= 128; i*=2) {
    console.log(i);
}


const header = document.getElementById("header");
const btn = document.getElementById("btn");

btn.onclick = () => {
    header.style.backgroundColor = "#3a3";
    header.innerHTML = "Pyco";
}