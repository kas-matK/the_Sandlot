function fibEven(fibArr = [1,2]){
    if(fibArr[fibArr.length-1] > 4000000) return 0;
    fibArr.push(fibArr[fibArr.length-1]+fibArr[fibArr.length-2]);
    if(fibArr[fibArr.length-2]%2===0) return fibArr[fibArr.length-2] + fibEven(fibArr);
    else return 0 + fibEven(fibArr);
}

console.log(fibEven());
