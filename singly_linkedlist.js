//Singly linked list data structure implementation in es6
class Node{
	constructor(data){
		this.data = data;
		this.link = null;
	}
	
}

class Linkedlist{
	constructor(){
		this.headnode = null
	}


	insertBegin(data){
		const new_node = new Node(data);
		new_node.link = this.headnode;
		this.headnode = new_node;
	}

	insertEnd(data){
	    const new_node = new Node(data);
	    if (this.headnode === null) {
	      this.headnode = new_node;
	    } else {
	      let current_node = this.headnode;
	      while (current_node.link !== null) {
	        current_node = current_node.link;
	      }
	      current_node.link = new_node;
	    }
	}

	display(){
	if(this.headnode === null){
		console.log("Linked list is empty!");
	}
	else{
		let current_node = this.headnode;

			while(current_node !== null){
				process.stdout.write(`${current_node.data}->`);
				current_node = current_node.link;
			}
			console.log("None");
		}

	}

}


const llist = new Linkedlist();

llist.insertBegin(5);
llist.insertBegin(4);
llist.insertBegin(3);
llist.insertBegin(2);

llist.insertEnd(6);
llist.insertEnd(7);
llist.insertEnd(8);
llist.insertEnd(9);
llist.insertEnd(10);

llist.display()



//Iterative singly linked list
class Node{
	constructor(data){
		this.data = data;
		this.link = null;
	}
}

class Linkedlist{
	constructor(){
		this.headnode = null;
	}

	displayer(){
		if(this.headnode == null){
			console.log("Linked list empty!");
		}
		else{
			let currentnode = this.headnode;

			while(currentnode != null){
				process.stdout.write(`${currentnode.data} -> `);//console.log(currentnode.data);
				currentnode = currentnode.link;
			}
			console.log("None");
		}
	}

	insertFront(data){
		const node = new Node(data);
		node.link = this.headnode;
		this.headnode = node;
	}

	insertBack(data){
		const newnode = new Node(data);
		let currentnode = this.headnode;
		while(currentnode.link != null){
			currentnode = currentnode.link;
		}
		currentnode.link = newnode;
	}
}

const llist = new Linkedlist();
llist.insertFront(2);
llist.insertFront(1);

llist.insertBack(3);
llist.insertBack(4);

llist.displayer();
