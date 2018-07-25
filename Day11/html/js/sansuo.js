function f1() {
    var tag1 = document.getElementById('i1');
    var connent = tag1.innerText;

    var f = connent.charAt(0);
    var l = connent.substring(1, connent.length);

    var g;
    g = f + l;
    tag1.innerText= g;
}

setInterval('f1()',500);