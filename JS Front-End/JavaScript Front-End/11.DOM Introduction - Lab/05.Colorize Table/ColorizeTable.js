function colorize() {
    const evenRows = document.querySelectorAll('table tr:nth-of-type(even)')
    evenRows.forEach(element => element.style.backgroundColor = 'Teal')
}