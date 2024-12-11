function attachGradientEvents() {
    let gradientElement = document.getElementById('gradient');
    let resultElement = document.getElementById('result');

    gradientElement.addEventListener('mousemove', (e) => {
        let currentPosition = e.offsetX;        
        let maxWidth = e.currentTarget.clientWidth;
        let percentage = Math.trunc((currentPosition / maxWidth) * 100)
        resultElement.textContent = `${percentage}%`
    })
}


// function attachGradientEvents() {
//     let gradientElement = document.getElementById('gradient')
//     gradientElement.addEventListener('mousemove', mouseMoveEvent)
//     gradientElement.addEventListener('mouseout', mouseOutEvent)

//     function mouseMoveEvent(e) {
//         let power = e.offsetX / (e.target.clientWidth - 1)
//         power = Math.trunc(power * 100)
//         document.getElementById('result').textContent = `${power}%`
//     }

//     function mouseOutEvent(e) {
//         document.getElementById('result') = ''
//     }
// }

// function attachGradientEvents() {
//     let gradientElement = document.getElementById('gradient');
//     let resultElement = document.getElementById('result');

//     gradientElement.addEventListener('mousemove', (e) => {
//         let currentPosition = e.offsetX;
//         let maxWidth = e.currentTarget.clientWidth;
//         let percentage = Math.min(Math.round((currentPosition / maxWidth) * 100), 100);
//         resultElement.textContent = `${percentage}%`;
//     });
// }