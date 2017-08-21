// Problem 1
// LOOP WAY
// function threeAndFive(num){
//     var runTot = 0;
//     for(i=0;i<num;i++){
//         if((i%3===0)||(i%5===0)) runTot += i;
//     }
//     return runTot;
//
// }

// RECURSION WAY
function threeAndFive(num){
    num--
    if(num===0) return 0;
    if((num%3===0)||(num%5===0)) return num + threeAndFive(num);
    else return threeAndFive(num);

}
console.log(threeAndFive(1000));
