function solve() {
    let input = document.querySelector('#inputs > textarea').value    
    let outputBestRestaurants = document.querySelector('#bestRestaurant p')
    let outputWorkers = document.querySelector('#workers p')

    let restaurantsObj = {}
    let restaurantsArr = JSON.parse(input)
    
    if (!input) return

    for (let rest of restaurantsArr) {
        let [restName, workersData] = rest.split(' - ')

        if (!Object.keys(restaurantsObj).includes(restName)){
            restaurantsObj[restName] = {
               totalSalary: 0,
               bestSalary: 0,
               workers: {}
            }
        };
        
        workersData = workersData.split(', ')
        
        for (let worker of workersData) {
            let [wName, salary] = worker.split(' ')
            restaurantsObj[restName]['workers'][wName] = Number(salary)
            restaurantsObj[restName]['totalSalary'] += Number(salary)

            if (Number(salary) > restaurantsObj[restName]['bestSalary']) {
                restaurantsObj[restName]['bestSalary'] = Number(salary)
            }
        };
        console.log(restaurantsObj);
         
    }
    
    let bestRestaurant = {
        'name': '',
        'avrgeSalary': 0,
        'bestSalary': 0,
        'workers': {}
    }

    for (let restName of Object.keys(restaurantsObj)) {
        let sum = restaurantsObj[restName]['totalSalary']
        let countWorkers = Object.keys(restaurantsObj[restName]['workers']).length
        let averageSalary = sum / countWorkers

        if (averageSalary >= bestRestaurant['avrgeSalary']) {

            bestRestaurant['name'] = restName;
            bestRestaurant['avrgeSalary'] = averageSalary;
            bestRestaurant['bestSalary'] = restaurantsObj[restName]['bestSalary'];
            bestRestaurant['workers'] = restaurantsObj[restName]['workers']
        }
    }
    
    let sortedBestWorkers = Object.entries(bestRestaurant['workers']).sort((a, b) => b[1] - a[1])
    sortedBestWorkers = Object.fromEntries(sortedBestWorkers)
    console.log(bestRestaurant['workers']);
    
    let bestRestInfo = `Name: ${bestRestaurant['name']} Average Salary: ${bestRestaurant['avrgeSalary'].toFixed(2)} Best Salary: ${bestRestaurant['bestSalary'].toFixed(2)}`
    let bestWorkersInfo = []

    for (let [workerName, workerSalary] of Object.entries(bestRestaurant['workers'])) {
        bestWorkersInfo.push(`Name: ${workerName} With Salary: ${workerSalary}`)
    }

    bestWorkersInfo = bestWorkersInfo.join(' ')
    

    outputBestRestaurants.textContent = bestRestInfo
    outputWorkers.textContent = bestWorkersInfo
    
    
}

// ["PizzaHut - Peter 500, George 300, Mark 800","TheLake - Bob 1300, Joe 780, Jane 660"]