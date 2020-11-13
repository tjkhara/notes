let john = {
  name: "John",
  driveCar: function driveCar(){
    console.log(this.name + " is driving a car.")
  }
}

john.driveCar()