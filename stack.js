//Stack data structure implementation using arrays...LIFO
const stack = [];

//populate stack
stack.push(7);
stack.push(8);
stack.push(9);

console.log("Stack:", stack);
//process.stdout.write(`${stack}\n`);

//pop operation, first check if stack is empty
if(stack.length == 0){
	console.log("ERROR!stack empty.");
}
else{
	stack.pop();
}
console.log("New stack after pop operation:", stack);

//peep operation
if(stack.length == 0){
	console.log("ERROR!stack empty.");
}
else{
	let peeked = stack[stack.length - 1];
	console.log("Peeked/last item:", peeked);
}



//Stack data structure implemented in ES6 using OOP
class Stack {
  constructor() {
    this.stack = [];
  }

  push(element) {
    this.stack.push(element);
  }

  pop() {
    if (this.isEmpty()) {
      console.log("Stack empty!");
    } else {
      return this.stack.pop();
    }
  }

  peek() {
    if (!this.isEmpty()) {
      return this.stack[this.stack.length - 1];
    } else {
      console.log("Stack empty!");
    }
  }

  isEmpty() {
    return this.stack.length === 0;
  }

  toString() {
    return this.stack.toString();
  }
}

const stack = new Stack();
stack.push(1);
stack.push(2);
stack.push(35);

console.log("New stack:", stack.toString());
console.log("Last element:", stack.peek());

stack.pop();
console.log("New stack:", stack.toString());
console.log("Last element:", stack.peek());
