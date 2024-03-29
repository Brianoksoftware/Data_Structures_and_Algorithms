//Quicksort algorithm recursive implementation
	function quicksort(arr){
		if(arr.length <= 1){
			return arr;
		}
		else{
			const pivot = arr[Math.floor(arr.length/2)];
			const lesser = [];
			const greater = [];

			for(let m = 0; m < arr.length; m++){
				if(arr[m] < pivot){
					lesser.push(arr[m]);
				}
				else if(arr[m] > pivot){
					greater.push(arr[m]);
				}
			}
			return quicksort(lesser).concat(pivot, quicksort(greater));
		}
	}
	console.log("Quicksort results: " + quicksort([3,4,1,7,0,2,5]));

	
	//Quicksort algorithm in ES6 recursively...using Arrow functions
	const quicksrrt = array => { 
		if(array.length <= 1){
			return array;
		}
		else{
			const pivot = array[Math.floor(array.length/2)];
			const left =[];
			const right =[];

			for(i=0; i<array.length; i++){
				if(array[i] < pivot){
					left.push(array[i]);
				}
				else if(array[i]>pivot){
					right.push(array[i]);
				}
			}
			return quicksrrt(left).concat(pivot, quicksrrt(right));
		}
	}
	console.log("result:" + quicksrrt([3,1,2,4,0]));



//quicksort algorithm in ES6 using recursion...mastery 1
arr = [4,3,2,1];

const quicksort = (arr) => {
    if(arr.length <= 1){
        return arr;
    }
    //choosing middle index
    const pivot =arr[Math.floor(arr.length/2)];
    const lesser = [];
    const greater = [];
    
    for(let x=0;x<arr.length;x++){
        if(arr[x] < pivot){
            lesser.push(arr[x]);
        }
        else if(arr[x] > pivot){
            greater.push(arr[x]);
        }
    }
    return quicksort(lesser).concat([pivot], quicksort(greater));
}

console.log("Quicksorted array:", quicksort(arr))



//Another quicksort algorithm implemented recursively
const arr = [5,686,6,90,7,1];

const quicksorto = (arr) => {
	if (arr.length <= 1){
		return arr;
	}
	else{
		const pivot = arr[Math.floor(arr.length / 2)];
		const lesser = [];
		const greater = [];

		for(let i=0; i<arr.length; i++){
			if(arr[i] < pivot){
				lesser.push(arr[i]);
			}
			else if(arr[i] > pivot){
				greater.push(arr[i]);
			}
		}

		return quicksorto(lesser).concat([pivot], quicksorto(greater));

	}
}

console.log("Quickosorted array:", quicksorto(arr))




//Quicksort algorithm implemented recursively
let arry = [7,2,5,1,0,4,3];

const quick_sort = (arry) => {
	if(arry.length <= 1){
		return arry;
	}
	else{
		let pivot = arry[Math.floor(arry.length/2)];
		let lesser = [];
		let greater = [];

		for(let i=0; i<arry.length; i++){
			if(arry[i] < pivot){
				lesser.push(arry[i]);
			}
			else if(arry[i] > pivot){
				greater.push(arry[i]);
			}
		}
		return quick_sort(lesser).concat([pivot], quick_sort(greater));
	}
}

console.log("The quicksorted list is:", quick_sort(arry));



//Quicksort algorithm in es6 javascript
const arr_ = [4,98,574,0,2,7,1,5,3];

const quicksorrrt = (arr_) => {
	if(arr_.length <=1){
		return arr_;
	}
	else{
		let pivot = arr_[Math.floor(arr_.length/2)];
		let lessr = [];
		let greatr = [];

		for(let i=0; i<= arr_.length;i++){
			if(arr_[i] < pivot){
				lessr.push(arr_[i]);
			}
			else if(arr_[i] > pivot){
				greatr.push(arr_[i]);
			}
		}
		return quicksorrrt(lessr).concat([pivot], quicksorrrt(greatr));
	}
}
process.stdout.write(`Old unsorted array was: ${JSON.stringify(arr_)}`);
console.log();
console.log("The new Quicksorted array:", quicksorrrt(arr_));






