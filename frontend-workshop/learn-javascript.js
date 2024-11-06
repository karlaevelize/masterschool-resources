// Variables

const name = "Karla";
const age = 29;
const hasPets = true;

let score = 20;

// Conditionals

if (age > 19) {
  console.log("adult"); // print("adult")
}

age > 19 ? console.log("adult") : console.log("not adult"); // ternary operator

// Functions

function greet(name) {
  return `Hello, ${name}`; // f"Hello, {name}"
}

greet("Karla");

// Arrow function

const sayHello = (name) => {
  return `Hello, ${name}`;
};

sayHello("Elis");

// Objects -> Dictionaries

const person = {
  name: "Karla",
  age: 29,
  hasPets: true,
};

console.log(person.name, person.age, person.hasPets);

// Arrays -> Lists

const students = ["Elis", "Polina", "Aroosha", "Welat"];
