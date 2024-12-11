function validate() {
    let inputElement = document.getElementById('email')

    let pattern = /[a-z]+@[a-z]+\.[a-z]+/

    inputElement.addEventListener('change', (e) => {
        let value  = e.currentTarget.value;

        if (!(pattern.test(value))) {
            e.currentTarget.classList.add('error')
        } else {
            e.currentTarget.classList.remove('error')
        }
    })
}