function solve() {
  const textareaElement = document.getElementById('input')
  let output = document.getElementById('output')
  let sentences = (textareaElement.value).split('. ')

  let result = sentences
      .map(sent => sent.trim())
      .reduce((finalArr, sentence, i) => {
        let currentIdx = Math.floor(i / 3)

        if (!(finalArr[currentIdx])) {
          finalArr[currentIdx] = []
        }

        finalArr[currentIdx].push(sentence)
        return finalArr
      }
      , [])
      .map(sentArr => `<p>${sentArr.join('. ')}</p>`)
      .join('\n');
  
  output.innerHTML = result

}


// function solve() {
//   const textareaElement = document.getElementById('input')
//   let outputElement = document.getElementById('output')

//   let sentences =  textareaElement.value.split('. ')
//     .filter(sent => sent.trim() !== '')
//     .map(sent => sent.trim());
  
//   let parsCount = Math.ceil(sentences.length / 3)
//   let output = ''
  
//   for (let i = 0; i < parsCount; i++) {
//     const p = i * parsCount

//     output += '<p>';
//     output += sentences.slice(p, (p + 3)).join('. ')
//     output += '</p>';
//   }
  
//   outputElement.innerHTML = output
// }