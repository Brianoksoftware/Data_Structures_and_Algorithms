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
