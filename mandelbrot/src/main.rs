use bmp::{Image, consts::{BLACK, WHITE}};
use num::complex::Complex;

const ITERATIONS: usize = 100; // play with this to increase accuracy around borders
const BOUNDING_RADIUS: f64 = 2.0; // Mandelbrot set is inside closed disc of radius 2

fn main() {
    println!("Enter your file name: ");
    let mut file_name = String::new();
    std::io::stdin().read_line(&mut file_name).unwrap();

    println!("Enter pixel width of final image");
    let mut dimensions_string = String::new();
    std::io::stdin().read_line(&mut dimensions_string).unwrap();
    let pixel_width = dimensions_string.trim()
        .parse::<u32>().expect("Pixel width is not a non-negative integer");


    let mut image = Image::new(
        pixel_width,
        pixel_width,
    );

    for (x, y) in image.coordinates() {
        image.set_pixel(x, y,
            if inside_set(
                pixel_to_coord(x, pixel_width), 
                pixel_to_coord(y, pixel_width)
            ) {
                BLACK
            } else {
                WHITE
            }
        );
    }

    image.save(file_name.trim()).unwrap();
}

// get "actual" coordinate value from the pixel's coordinate value
//
// calculation is done by getting difference from center, then scaling to the
// radius 2 disc
fn pixel_to_coord(num: u32, pixel_width: u32) -> f64 {
    let p = pixel_width as f64;
    (num as f64 - p / 2.0) / p * BOUNDING_RADIUS * 2.0
}

// takes in coordinate version of complex number (i.e. takes (a, b) for a + bi)
fn inside_set(a: f64, b: f64) -> bool {
    let c = Complex::new(a, b);
    let mut z = Complex::new(0.0, 0.0);
    for _ in 0..ITERATIONS {
        z = z * z + c;
        if z.norm() > BOUNDING_RADIUS {
            return false;
        }
    }

    true
}
