use std::fs;

pub fn read_string_input(filename: &str) -> String {
    println!("Reading from file: {}", filename);

    return fs::read_to_string(filename)
        .expect("Something went wrong reading the file");
}

pub fn read_input_as_vector_of_strings(filename: &str) -> Vec<String> {
    return read_string_input(filename)
        .lines()
        .map(String::from)
        .collect();
}