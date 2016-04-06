weatherOfInput = function(area) {
  console.log(area)
}

weatherByLocation = function(){
  var obj, aVar, splitter, splitter2, region, city
  obj = new XMLHttpRequest()
  obj.onreadystatechange = function(){

    if(obj.readyState == 4 && obj.status == 200){
      aVar = obj.responseXML
      console.log(aVar)
      splitter = aVar.getElementsByTagName("regionName")
      region = splitter[0].childNodes[0].data
      splitter2 = aVar.getElementsByTagName("city")
      city = splitter2[0].childNodes[0].data
      console.log(region)
      console.log(city)
    }

  };
  obj.open("GET", "http://ip-api.com/xml/?fields=regionName,city", true);
  obj.send();
  
}



/*weatherByLocation = function() {
  var obj = new XMLHttpRequest()
  obj.open("GET", "http://ip-api.com/xml", true);
  obj.setRequestHeader('Content-Type', 'test/xml');
  obj.send();

  xmlDocument = obj.responseXML;
  console.log(xmlDocument.childNodes['0'].textContent);
}
*/
