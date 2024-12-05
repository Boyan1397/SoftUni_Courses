function calc() {
    let firstNumber = document.getElementById('num1')
    let secondNumber = document.getElementById('num2')
    let finalSum = document.getElementById('sum')

    finalSum.value = Number(firstNumber.value) + Number(secondNumber.value)
    
}
