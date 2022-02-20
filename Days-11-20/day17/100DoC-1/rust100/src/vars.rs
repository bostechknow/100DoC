// Variables hold primitive data or references to data
// Variables are immutable by default
// Rust is a block-scoped language

pub fn run() {
    let name = "Tom";
    let job = "engineer";
    let mut age = 25;
    println!("My name is {}, and I am a {} year old {}.", name, age, job);
    age = 27;
    println!("My name is {}.  I just had a birthday, and now I am {} years old.", name, age);

    // Define constant
    const ID: i32 = 001;
    println!("ID: {}", ID);

    // Assign multiple variables
    let (newname, newage) = ("Angie", 23);
    println!("My co-worker is {}, and she is {}.", newname, newage)
}