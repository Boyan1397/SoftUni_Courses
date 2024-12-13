document.addEventListener('DOMContentLoaded', solve);

// delegation !
function solve() {
    document.querySelector('main').addEventListener('click', (e) => {
        if (e.target.tagName !== 'BUTTON') return
        
        let parentEl = e.target.closest('.profile')
        let state = parentEl.querySelector('.radio-group input:checked').getAttribute('id')
        if (state.includes('Lock')) return
        
        let hiddenElements = parentEl.querySelector('.hidden-fields')
        
        if (e.target.textContent === 'Show more') {
            hiddenElements.classList.remove('active')
            e.target.textContent = 'Show less'
        } else {
            hiddenElements.classList.add('active')
            e.target.textContent = 'Show more'
        }
    })
}




// basic one
// function solve() {
//     let lockButtonElements = document.querySelectorAll('.radio-group label:first-of-type')
//     let unlockButtonElements = document.querySelectorAll('.radio-group label:nth-of-type(2)')
    
//     let showMoreButtonElements = document.querySelectorAll('button')
    
//     showMoreButtonElements.forEach(button => button.disabled = true);
    
//     // show more ||| show less
//     showMoreButtonElements.forEach(button => button.addEventListener('click', showMoreData))
//     function showMoreData(e) {
//         let profileElement = e.target.parentElement;

//         let hiddenElements = profileElement.querySelector('div:last-of-type');
        
//         if (!(hiddenElements.style.display === 'block')) {
//             hiddenElements.style.display = 'block';
//             e.target.textContent = 'Show less'
//         } else {
//             hiddenElements.style.display = 'none';
//             e.target.textContent = 'Show more'
//         }
//     }

//     // lock show button
//     lockButtonElements.forEach(lock => lock.addEventListener('click', lockShowButton))
//     function lockShowButton(e) {
//         let profileElement = e.target.parentElement.parentElement;
//         let showMoreButtonElement = profileElement.querySelector('button')
//         showMoreButtonElement.disabled = true
//     }

//     // unclock show button
//     unlockButtonElements.forEach(unlock => unlock.addEventListener('click', unlockShowButton))

//     function unlockShowButton(e) {
//         let profileElement = e.target.parentElement.parentElement;
//         let showMoreButtonElement = profileElement.querySelector('button')
//         showMoreButtonElement.disabled = false
//     }
// }