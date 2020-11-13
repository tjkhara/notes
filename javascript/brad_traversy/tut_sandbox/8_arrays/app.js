function under50(num){
  if(num < 50){
    return num
  }
}

numbers = [100,23,45,55];

val = numbers.find(under50);

console.log(val);