document.addEventListener('DOMContentLoaded', solve);

function solve() {

   let contentElement = document.getElementById('content')
   let submitElement = document.querySelector('#task-input')

   submitElement.addEventListener('submit', (e) => {
      e.preventDefault()

      let sections = e.currentTarget.querySelector('input:nth-child(1)').value.split(',')
      
      for (let element of sections) {
         let divElement = document.createElement('div')
         let pElement = document.createElement('p')

         pElement.textContent = element
         pElement.style.display = 'none'

         divElement.append(pElement)
         divElement.addEventListener('click', (e) => {
            e.currentTarget.querySelector('p').style.display = 'initial'
         })

         contentElement.append(divElement)
      }
   })
}