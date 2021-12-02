use crate::common;

pub fn problem1() {
    let filename: &str = "input/day2/problem1.in";
    let input: Vec<String> = common::read_input_as_vector_of_strings(filename);

    let mut horizontal = 0;
    let mut depth = 0;
    for (i, instruction) in input.iter().enumerate() {
        let instruction: Vec<&str> = instruction.split(' ').collect();
        
        let direction = instruction[0];
        let units = instruction[1];
        let units = match units.parse::<u32>() {
            Ok(num) => num,
            Err(_) => break,
        };


        if direction == "forward" {
            horizontal += units;
        } else if direction == "down" {
            depth += units;
        } else if direction == "up" {
            depth -= units;
        }
    }

    println!("Answer is: {}", horizontal * depth);
}

pub fn problem2() {
    let filename: &str = "input/day2/problem1.in";
    let input: Vec<String> = common::read_input_as_vector_of_strings(filename);

    let mut horizontal = 0;
    let mut depth = 0;
    let mut aim = 0;
    for (i, instruction) in input.iter().enumerate() {
        let instruction: Vec<&str> = instruction.split(' ').collect();
        
        let direction = instruction[0];
        let units = instruction[1];
        let units = match units.parse::<u32>() {
            Ok(num) => num,
            Err(_) => break,
        };


        if direction == "forward" {
            horizontal += units;
            depth += (aim * units);
        } else if direction == "down" {
            aim += units;
        } else if direction == "up" {
            aim -= units;
        }
    }

    println!("Answer is: {}", horizontal * depth);
}