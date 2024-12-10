// function solve() {
//   const textElement = document.getElementById('text')
//   const namingElement = document.getElementById('naming-convention')
//   let resultContainer = document.getElementById('result');

//   let text = textElement.value.split(' ')
//   let error = 'Error!'
  
//   let naming = namingElement.value    

//   let textResult = []

//   if (naming === 'Camel Case') {
//     textResult.push(text[0].toLowerCase())
//     for (let i = 1; i < text.length; i++) { 
//       let word = text[i]
//       word = word[0].toUpperCase() + word.slice(1,).toLowerCase()
//       textResult.push(word)
//     }
//   } else if (naming === 'Pascal Case') {
//     for (let i = 0; i < text.length; i++) {
//       let word = text[i]
//       word = word[0].toUpperCase() + word.slice(1,).toLowerCase()
//       textResult.push(word)
//     }
//   }  else {
//     resultContainer.textContent = 'Error!'
//     return
//   }

//   textResult = textResult.join('')
//   resultContainer.textContent = textResult

// }


function solve() {
  const textElement = document.getElementById('text');
  const namingElement = document.getElementById('naming-convention');
  let resultContainer = document.getElementById('result');
  
  let text = textElement.value
  let naming = namingElement.value

  let convertToPascalCase = (text) => 
      text
        .split(' ')
        .map(word => word[0].toUpperCase() + word.slice(1,).toLowerCase())
        .join('')

  let convertor = {
    'Pascal Case': convertToPascalCase,
    'Camel Case': (text) => convertToPascalCase(text)[0].toLowerCase() + convertToPascalCase(text).slice(1,)
  }

  if (naming !== 'Pascal Case' && naming !== 'Camel Case') {
    resultContainer.textContent = 'Error!'
    return
  }
  
  resultContainer.textContent = convertor[naming](text)
}