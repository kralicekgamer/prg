const one = document.getElementById("1");
const two = document.getElementById("2");
const three = document.getElementById("3");
const btn = document.getElementById("btn");
const status = document.getElementById("status");

btn.addEventListener("click", function () {
    status.innerHTML = "Spining.";

    const interval = setInterval(() => {
        one.innerText = Math.floor(Math.random() * 10);
        two.innerText = Math.floor(Math.random() * 10);
        three.innerText = Math.floor(Math.random() * 10);
    }, 50);

    setTimeout(() => {
        clearInterval(interval); 
        if (one.innerText === two.innerText && one.innerText === three.innerText) {
            status.innerHTML = "Win"
        } else {
            status.innerHTML = "Lost";
        }
    }, 5000); 
});