//stack data structure implemented in ES6
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
