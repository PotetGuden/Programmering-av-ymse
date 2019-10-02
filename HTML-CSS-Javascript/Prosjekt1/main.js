
function myFunction() {
    document.getElementById("frm1").submit();
  }


console.log("hello world");
var x = 5;
var y = 1;

var z = x+y;

console.log(z);


function velkommenMelding(navn){
    var result = "Hei og velkommen til denne siden " + navn + " hyggelig at du kom.";

    return result;

}
console.log(velkommenMelding("jostein"));



/*

function go(name, age){
    if (age > 20){
        return name + "!";
    } else {
        return name;
    }
}

alert(go("Jostein", 23))

function add (first, second){
    return first+second
}

alert(add(1,7))

function add1(først,sist){
    if (først > sist) {
        return først*først;
    } else {
        return først*sist;
    }
}

alert(add1(2,3));

add1(1,2)*/