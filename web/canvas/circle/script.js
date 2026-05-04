// Získáme odkaz na element canvas a jeho 2D kontext pro kreslení
const platno = document.getElementById("platno");
const ctx = platno.getContext("2d");

// Funkce pro vykreslení kruhu
// Parametry: ctx = kontext kreslení, x, y = střed kruhu, radius = poloměr, color = barva
function nakresliKruh(ctx, x, y, radius, color) {
    ctx.beginPath();                    // Zahájí novou cestu (path)
    ctx.arc(x, y, radius, 0, Math.PI * 2); // Celá kružnice: od 0 do 2π (360°)
    ctx.fillStyle = color;              // Nastavení barvy výplně
    ctx.fill();                         // Vyplnění tvaru
    ctx.closePath();                    // Uzavření cesty
}

// Výchozí hodnoty kruhu
const x = 200;   // vodorovná souřadnice středu
const y = 400;   // svislá souřadnice středu
const radius = 100;    // poloměr v pixelech
const color = "yellow"; // barva výplně

// Zavolání funkce – kruh se zobrazí na plátně
nakresliKruh(ctx, x, y, radius, color);