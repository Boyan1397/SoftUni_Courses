function attachEvents() {
    let inputElement = document.getElementById('location')
    let buttonElement = document.getElementById('submit')
    let forecastElement = document.getElementById('forecast')
    let currentElement = document.getElementById('current')

    buttonElement.addEventListener('click', getWeather)

    const weatherSymbols = {
        'Sunny': '☀',  // ☀
        'Partly sunny': '⛅',  // 
        'Overcast': '☁',  // ☁
        'Rain': '☂',  // ☂
        'Degrees': '°'  // °
    };    

    let baseUrl = 'http://localhost:3030/jsonstore/forecaster'
    function getWeather() {
        fetch(baseUrl + '/locations')
            .then(response => response.json())
            .then(data => {
                let location = data.find(city => city.name === inputElement.value)
                let locCode = location.code  
                
                return Promise.all([
                    fetch(baseUrl + '/today/' + locCode).then(response => response.json()),
                    fetch(baseUrl + '/upcoming/' + locCode).then(response => response.json())
                ])
            })
            .then(([todaysWeather, upcomingWeather]) => {
                // tpdays weather
                // create all elements
                forecastElement.style.display = 'block'
                let createForecastsElement = document.createElement('div')
                createForecastsElement.classList.add('forecasts')
                
                let createCondition = document.createElement('span')
                createCondition.classList.add('condition')

                let createConditionSymbolEl = document.createElement('span')
                createConditionSymbolEl.classList.add('condition', 'symbol')
                createConditionSymbolEl.textContent = weatherSymbols[todaysWeather.forecast['condition']];

                let createCitySpan = document.createElement('span')
                createCitySpan.classList.add('forecast-data')
                createCitySpan.textContent = todaysWeather.name
                
                let createHighSpan = document.createElement('span')
                createHighSpan.classList.add('forecast-data')
                createHighSpan.textContent = `${todaysWeather.forecast['low']}${weatherSymbols['Degrees']}/${todaysWeather.forecast['high']}${weatherSymbols['Degrees']}`

                let createLastConditionSpan = document.createElement('span')
                createLastConditionSpan.classList.add('forecast-data')
                createLastConditionSpan.textContent = todaysWeather.forecast['condition']

                // add all elements
                currentElement.appendChild(createForecastsElement)
                createForecastsElement.appendChild(createConditionSymbolEl)
                createForecastsElement.appendChild(createCondition)
                createCondition.appendChild(createCitySpan)
                createCondition.appendChild(createHighSpan)
                createCondition.appendChild(createLastConditionSpan)

                // upcoming weather
                let upcomingWeatherConditions = document.getElementById('upcoming')
                let divElement = document.createElement('div')
                divElement.className = 'forecast-info'
                for (let dayForecast of upcomingWeather.forecast) {
                    let newSpan = document.createElement('span')
                    newSpan.className = 'upcoming'
                    newSpan.innerHTML = `
                    <span class="symbol">${weatherSymbols[dayForecast.condition]}</span>
                    <span class="forecast-data">${dayForecast.low}${weatherSymbols['Degrees']}/${dayForecast.high}${weatherSymbols['Degrees']}</span>
                    <span class="forecast-data">${dayForecast.condition}</span>
                    `
                    divElement.appendChild(newSpan)
                }

                upcomingWeatherConditions.appendChild(divElement)

            })


    }
}

attachEvents();


