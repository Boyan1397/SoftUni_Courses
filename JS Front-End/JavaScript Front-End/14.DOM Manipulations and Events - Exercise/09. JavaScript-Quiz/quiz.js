document.addEventListener('DOMContentLoaded', solve);

function solve() {
  let questionElements = document.querySelectorAll('.question')
  let posssibleAnswers = ['onclick', 'JSON.stringify()', 'A programming API for HTML and XML documents']
  let answered = []
  let counter = 0
  let correct = 0
  questionElements.forEach(question => {
    let answersElements = question.querySelectorAll('.quiz-answer')

    let firstAnswer = Array.from(answersElements)[0]
    let secondAnswer = Array.from(answersElements)[1]

    firstAnswer.addEventListener('click', (e) => {
      answered.push(e.currentTarget.textContent)
      counter += 1
      if (counter < 3) {
        questionElements[counter].classList.remove('hidden')
        question.classList.add('hidden')
      } else {
        question.classList.add('hidden')
        showResult(answered)
      }
    });

    secondAnswer.addEventListener('click', (e) => {
      answered.push(e.currentTarget.textContent)
      counter += 1
      if (counter < 3) {
        questionElements[counter].classList.remove('hidden')
        question.classList.add('hidden')
      } else {
        question.classList.add('hidden')
        showResult(answered)
      }
    });

    function showResult(answers) {
      let resultElement = document.querySelector('#results')
      for (let answer of answers) {
        if (posssibleAnswers.includes(answer)) {
          correct += 1
        }
      }
      if (correct === 3) {
        resultElement.textContent = "You are recognized as top JavaScript fan!"
      } else if (correct === 2) {
        resultElement.textContent = `You have ${correct} right answers`
      } else {
        resultElement.textContent = `You have ${correct} right answer`
      }
    }
  })
}