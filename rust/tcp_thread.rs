use std::net::{TcpListener, TcpStream};
use std::io::{Read, Write};
use std::thread;
use std::time::Duration;
use std::env;

fn upper(text: &str) -> String {
    thread::sleep(Duration::from_secs(1));
    text.to_uppercase()
}

fn handle(mut stream: TcpStream) {
    let peer_addr = stream.peer_addr().unwrap_or_else(|_| "Unknown".parse().unwrap());
    println!("Client connected: {}", peer_addr);
    let mut buffer = [0; 512];

    loop {
        match stream.read(&mut buffer) {
            Ok(0) => {
                println!("Client disconnected: {}", peer_addr);
                break;
            }
            Ok(size) => {
                let received = String::from_utf8_lossy(&buffer[..size]);
                let response = upper(&received);
                stream.write_all(response.as_bytes()).unwrap();
            }
            Err(e) => {
                eprintln!("Failed to read from client: {}", e);
                break;
            }
        }
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let port = args.get(1).expect("Usage: <program> <port>");
    let address = format!("0.0.0.0:{}", port);

    let listener = TcpListener::bind(&address).expect("Failed to bind port");
    println!("Server listening on {}...", address);

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                thread::spawn(|| handle(stream));
            }
            Err(e) => {
                eprintln!("Connection failed: {}", e);
            }
        }
    }
}
