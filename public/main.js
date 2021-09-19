'use strict';

function play() {
    const audio = new Audio('siren.mp3');
    audio.play();
}

async function handler() {
    const but = document.getElementById('button');
    but.style.marginBottom = "-20px";
    play();
    await new Promise((resolve) => setTimeout(resolve, 500));
    document.getElementById('white').style.display = 'none';
    document.body.classList.add('pizdec');
}

document.getElementById('one').addEventListener('click', handler, {once: true});
document.getElementById('two').addEventListener('click', handler, {once: true});