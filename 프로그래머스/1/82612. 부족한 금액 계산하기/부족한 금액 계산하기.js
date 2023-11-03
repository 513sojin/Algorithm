function solution(price, money, count) {
    var sum = 0;
    var original = price;
    
    for(var i=2;i<=count+1;i++){
        sum += price;
        price = original * i;
    }
    return sum-money > 0 ? sum-money : 0;
}