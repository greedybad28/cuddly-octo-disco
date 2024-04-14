function doSomething(callback){
    console.log("Doing something.....");
    // calling bac kthe arrow function
    
    callback();
}
doSomething(() =>{
    console.log("Callback function called")
}

)



