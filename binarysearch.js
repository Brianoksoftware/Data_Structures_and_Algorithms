//Binary search algorithm using recursion in ES6
const arr = [1,2,3,4,5];

const target_value = 2;
let lowerbound = 0;
let upperbound = arr.length - 1;
let midpoint_index;

const binarysearch = (arr, target_value, lowerbound, upperbound) => {
	if(lowerbound <= upperbound){
		midpoint_index = Math.floor((lowerbound + upperbound) / 2);

		if (target_value == arr[midpoint_index]){
			return midpoint_index;
		}
		else if (target_value < arr[midpoint_index]){
			return binarysearch(arr, target_value, lowerbound, midpoint_index - 1);
		}
		else{
			return  binarysearch(arr, target_value, midpoint_index + 1, upperbound);
		}
	}
}

console.log("The target value " + target_value + " is at index: " + binarysearch(arr, target_value, lowerbound, upperbound) + " of the SORTED array: " + JSON.stringify(arr));




//Quicksort algorithm that sorts an array and feeds it to a Binary search algorithm for search operation using recursion in ES6
const unsorted_array = [3,1,5,2,4];

const brian_quicksort = (unsorted_array) => {
	if(unsorted_array.length <= 1){
		return unsorted_array;
	}
	else{
		let pivot = unsorted_array[Math.floor(unsorted_array.length/2)];
		let lesser = [];
		let greater = [];


		for(let i=0; i<unsorted_array.length; i++){
			if(unsorted_array[i] < pivot){
				lesser.push(unsorted_array[i]);
			}
			else if(unsorted_array[i] > pivot){
				greater.push(unsorted_array[i]);
			}
		}
		return brian_quicksort(lesser).concat([pivot], brian_quicksort(greater));
	}
}

const arry = brian_quicksort(unsorted_array); //[1,2,3,4,5]
//console.log("UNSORTED ARRAY:", unsorted_array);
//console.log("SORTED ARRAY:", arry);

const target_valueo = 3;
let lowerboundo = 0;
let upperboundo = arry.length - 1;
let midpoint_indexo;

const binarysearcho = (arry, target_valueo, lowerboundo, upperboundo) => {
	if(lowerboundo <= upperboundo){
		midpoint_indexo = Math.floor((lowerboundo + upperboundo) / 2);

		if (target_valueo == arry[midpoint_indexo]){
			return midpoint_indexo;
		}
		else if (target_valueo < arry[midpoint_indexo]){
			return binarysearcho(arry, target_valueo, lowerboundo, midpoint_indexo - 1);
		}
		else{
			return  binarysearcho(arry, target_valueo, midpoint_indexo + 1, upperboundo);
		}
	}
}
console.log("The target value " + target_valueo + " is at index: " + binarysearcho(arry, target_valueo, lowerboundo, upperboundo) + " of the SORTED array: " + JSON.stringify(arry));






