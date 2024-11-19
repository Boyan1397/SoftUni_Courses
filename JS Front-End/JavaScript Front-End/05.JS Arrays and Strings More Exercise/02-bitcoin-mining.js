function totalBitcoins(goldAmountsArray) {
    const bitcoinPrice = 11949.16;
    const goldPerGram = 67.51;
    let bitcoinBbought = 0;
    let totalMoney = 0;
    let daysOfPurchase = [];

    for (let i = 0; i < goldAmountsArray.length; i++) {
        let currentDay = goldAmountsArray[i] * goldPerGram;
        
        
        if ((i + 1) % 3 === 0) {
            currentDay = currentDay * 0.70;
        }

        totalMoney += currentDay
        while (totalMoney >= bitcoinPrice) {
            bitcoinBbought += 1;
            daysOfPurchase.push(i + 1);
            totalMoney -= bitcoinPrice
        }
    }

    console.log(`Bought bitcoins: ${bitcoinBbought}`);
    if (bitcoinBbought > 0) {
        console.log(`Day of the first purchased bitcoin: ${daysOfPurchase[0]}`);
    }
    console.log(`Left money: ${totalMoney.toFixed(2)} lv.`);
}

totalBitcoins([100, 200, 300])
totalBitcoins([50, 100])
totalBitcoins([3124.15, 504.212, 2511.124])