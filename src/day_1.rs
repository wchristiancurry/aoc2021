use crate::common;

pub fn problem1() {
    let filename: &str = "input/day1/problem1.in";
    let input: Vec<String> = common::read_input_as_vector_of_strings(filename);
    
    let mut increases: u32 = 0;
    let mut previous: u32 = u32::MAX;
    for depth in input {
        println!("depth: {}", depth);
        
        let depth = match depth.parse::<u32>() {
            Ok(num) => num,
            Err(_) => break,
        };

        if depth > previous {
            increases += 1;
        }

        previous = depth;
    }

    println!("{}", increases);
}

pub fn problem2() {
    let filename: &str = "input/day1/problem1.in";
    let input: Vec<String> = common::read_input_as_vector_of_strings(filename);
    
    let mut converted_input: Vec<u32> = Vec::<u32>::new();
    for depth in input {
        let depth = match depth.parse::<u32>() {
            Ok(num) => num,
            Err(_) => break,
        };

        converted_input.push(depth)
    }

    let mut previous_window = u32::MAX;
    let mut increases: u32 = 0;
    for (i, depth) in converted_input.iter().enumerate() {
        if converted_input.len() <= i+2 {
            break
        }

        let current_window: u32 
            = depth + converted_input[i+1] + converted_input[i+2];
        
        if current_window > previous_window {
            increases += 1;
        }

        previous_window = current_window;
    }

    println!("{}", increases);
}