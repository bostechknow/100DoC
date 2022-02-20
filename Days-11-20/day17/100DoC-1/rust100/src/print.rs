pub fn run() {
    // Print to console
    println!("Hello from the print.rs file.");

    // Basic formatting examples
    println!("Number: {}", 1);
    println!("{} is a {}.", "Sword", "weapon");

    // Positional Arguments
    println!("{0} is a {1}, but the {0} can be {2}.", "Cheshire Cat", "friend", "scary");

    // Named Arguments
    println!("{name} is a {job}.", name = "Tom", job="engineer");

    // Placeholder traits
    println!("Binary: {:b} Hex: {:x} Octal: {:o}", 31, 31, 31);

    // Placeholder for debug trait (tuple)
    println!("{:?}", (42, false, "Austin"));

    // Basic math
    println!("25 x 7 = {}", 25 * 7);
}