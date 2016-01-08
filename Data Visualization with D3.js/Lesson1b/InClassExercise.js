/*select the dom object for footer*/
document.getElementById("footer");

/*select the dom object for navbar*/
document.querySelector("header.navbar-static-top");

/*select the class viewer-main using d3.select, what's returned will be a array of d3 object*/
d3.select('.viewer-main');

/*find the background color of the navbar using d3*/
d3.select("header.navbar-static-top").style("background-color");

/*change the background color of the navbar to green using d3*/
d3.select("header.navbar-static-top").style("background-color","green");

/*select all in d3*/
d3.selectAll("header.navbar-static-top");

/*store the query result into a variable called header*/
var header = d3.selectAll("header.navbar-static-top");

/*change the title of the course*/
d3.select("h1.left-hand-nav-title").text("This is fun");

/*sub selection and change tag attribute value*/
var parent_el = d3.select("a#header-logo");
parent_el.select("img").attr("alt", "Jon's logo");

/*change the logo image on the navbar*/
var zipf = "https://bit.ly/1MChLwj";
d3.select("a#header-logo").select("img").attr("src", zipf);

/*look at the html of the side bar*/
d3.select("div.col-xs-3").html();

/*remove the content of the side bar*/
d3.select("div.col-xs-3").html("");

/*remove the side bar entirly*/
d3.select("div.col-xs-3").remove();


/*add a svg element to a dom object*/
	var svg = d3.select('div.col-xs-3').append('svg');

/*creating scaling function using d3 domain() and range() it will be a linear mapping 
and notice that upper left point is 0,0 */
var y = d3.scale.linear().domain([15,90]).range([150,0]);
var x = d3.scale.log().domain([250,100000]).range([0,250]);

/*check if the scaling function works*/
console.log(y(75), x(8347));

/*append a red circle to the svg element*/
svg.append("circle").attr("r",10).attr("fill", "red").attr("cx",x(8347)).attr("cy",y(75));



