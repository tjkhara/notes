const todo = {
  add: function(){
    console.log("Add todo ...")
  },
  edit: function(id){
    console.log(`Edit ${id}`)
  }
}

todo.delete = function(){
  console.log("Delete todo")
}

todo.add();

todo.edit(10);

todo.delete()