function subtract() {
    const firstNumberElement = document.getElementById('firstNumber');
    const secondNumberElement = document.getElementById('secondNumber');
    let result = document.getElementById('result')

    let firstNumber = Number(firstNumberElement.value);
    let secondNumber = Number(secondNumberElement.value);

    result.textContent = firstNumber - secondNumber
}