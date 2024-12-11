function solve() {
   let addButtonsElements = document.querySelectorAll('.add-product')
   let textareaElement = document.querySelector('textarea')
   let checkoutButton = document.querySelector('.checkout')
   let total = 0
   let productsObj = {}

   for (let button of addButtonsElements) {
      button.addEventListener('click', (e) => {
         let product = button.parentElement.parentElement
         let name = product.querySelector('.product-title').textContent
         let price = Number(product.querySelector('.product-line-price').textContent)

         total += price
         productsObj[name] = true
         
         
         textareaElement.textContent += `Added ${name} for ${price.toFixed(2)} to the cart.\n`
      })
   }

   checkoutButton.addEventListener('click', (e) =>  {
      checkoutButton.setAttribute('disabled', true)
      addButtonsElements.forEach(button => button.setAttribute('disabled', true))

      list = Object.keys(productsObj)
      textareaElement.textContent += `You bought ${list.join(', ')} for ${total.toFixed(2)}.`      
   })
}

   // let productNamesElements = document.querySelectorAll('.product-title')
   // let productPricesElements = document.querySelectorAll('.product-line-price')
   // let addButtonsElement = document.querySelectorAll('.add-product')