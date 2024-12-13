document.addEventListener('DOMContentLoaded', solve);

function solve() {
    let formsElements = document.querySelectorAll('form')

    let daysElement = document.getElementById('days-input')
    let hoursElement = document.getElementById('hours-input')
    let minutesElement = document.getElementById('minutes-input')
    let secondsElement = document.getElementById('seconds-input')

    let valuesToSeconds = {days: 86400, hours: 3600, minutes: 60, seconds: 1};

    formsElements.forEach(form => form.addEventListener('submit', updateData))

    function updateData(e) {
        e.preventDefault()

        let currentInput = e.target.querySelector('input[type="number"]')
        if (currentInput.value < 1) return

        let valueType = currentInput.id.split('-input')[0]
    
        let inputAsSeconds = valuesToSeconds[valueType] * Number(currentInput.value)

        asignFinalValues(inputAsSeconds)
    }

    function asignFinalValues(secondsInput) {
        daysElement.value = (secondsInput / valuesToSeconds.days).toFixed(2)
        hoursElement.value = (secondsInput / valuesToSeconds.hours).toFixed(2)
        minutesElement.value = (secondsInput / valuesToSeconds.minutes).toFixed(2)
        secondsElement.value = (secondsInput / valuesToSeconds.seconds).toFixed(2)
    }
}
