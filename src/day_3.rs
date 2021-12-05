use crate::common;

pub fn problem1() {
    let filename: &str = "input/day3/problem1.in";
    let input: Vec<String> = common::read_input_as_vector_of_strings(filename);

    let value_count: usize = input.len();
    let value_size: usize = input[0].len();
    let mut counts = vec![0; value_size];
    for value in input {
        for (i, c) in value.chars().enumerate() {
            if c == '1' {
                counts[i] += 1;
            }
        }
    }

    let mut gamma_rate: u32 = 0b0;
    let mut epsilon_rate: u32 = 0b0;
    for (i, value) in counts.iter().enumerate() {
        if value > &(value_count / 2) {
            gamma_rate = gamma_rate | (1<<(value_size-i-1));
        } else {
            epsilon_rate = epsilon_rate | (1<<(value_size-i-1));
        }
    }
}

pub fn problem2() {
    let filename: &str = "input/day3/problem1.in";
    let input: Vec<String> = common::read_input_as_vector_of_strings(filename);

    // for each number
    // consider 1st bit
    // if more 1s than 0s, keep only numbers with 1 as first bit
    let oxygen_generator_rating = find_rating(&input, true);
    let co2_scrubber_rating = find_rating(&input, false);

    let oxygen_generator_rating 
        = convert_binary_string_to_decimal(&oxygen_generator_rating);
    let co2_scrubber_rating 
        = convert_binary_string_to_decimal(&co2_scrubber_rating);

    // println!("rating1: {} and rating2: {}", oxygen_generator_rating, co2_scrubber_rating);
    println!("final answer: {}", oxygen_generator_rating * co2_scrubber_rating);
}

fn find_rating(input: &Vec<String>, favor_ones: bool) -> String {
    let mut index = 0;
    let mut current_values: Vec<String> = input.to_vec();
    loop {
        let mut ones: Vec<String> = Vec::new();
        let mut zeroes: Vec<String> = Vec::new();

        if current_values.len() == 1 {
            return current_values.remove(0);
        }

        loop {
            let value: String = match current_values.pop() {
                Some(p) => p,
                None => break
            };

            if value.chars().nth(index) == Some('1') {
                ones.push(value);
            } else {
                zeroes.push(value);
            }
        }

        if favor_ones {
            current_values = if ones.len() >= zeroes.len() { ones } else { zeroes }
        } else {
            current_values = if zeroes.len() <= ones.len() { zeroes } else { ones }
        }

        index += 1;
    }
}

fn convert_binary_string_to_decimal(binary_string: &str) -> u32 {
    let mut decimal_value: u32 = 0;
    for (i, value) in binary_string.chars().enumerate() {
        let value = value.to_digit(2).unwrap();
        decimal_value = decimal_value | (value << (binary_string.len() - i - 1));
    }

    return decimal_value;
}