testArr = [2,4,6,8]

anotherArr = [1,2,3,4,5,6]

function allEvens(inputArr){
    return inputArr.every(num => num % 2 == 0)
}

console.log(allEvens(anotherArr))