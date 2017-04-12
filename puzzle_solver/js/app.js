/* global Mustache:true, $:true, swal: true */

function kickoff() {

  // server address
  var address = window.location.origin;

  var puzzleValues = [0, 0, 0, 0, 0, 0, 0, 0, 0];

  // ----------------- GET/POST ---------------------

  function request(method, url, data, callback){
    var xhr = new XMLHttpRequest();
    url = address + url;
    xhr.open(method, url);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (xhr.status === 200) {
          // console.log("response:", xhr.responseText);
          if(callback) callback(JSON.parse(xhr.responseText));
        }
    };
    if(data) xhr.send(JSON.stringify(data));
    else xhr.send();
  }

  function randomGlow() {
    var glowEls = document.getElementsByClassName("glow");
    for (var i = 0; i < glowEls.length; i++) {
      var el = glowEls[i];
      el.style.webkitAnimationDuration = (Math.floor(Math.random() * 6) + 1) + "s";
    }
  }

  function hasDuplicates(data) {
    var result = [];
    data.forEach(function(element, index) {
      // Find if there is a duplicate or not
      if (data.indexOf(element, index + 1) > -1) {
        // Find if the element is already in the result array or not
        if (result.indexOf(element) === -1) {
          result.push(element);
        }
      }
    });
    return result.length > 0;
  }

  function getSolution() {
    document.getElementsByClassName("puzzle-steps")[0].innerHTML = '<div class="loader"></div>';
    var errorMsg = document.getElementById("puzzle-error-msg");
    puzzleValues = puzzleValues.map(function(val) {
      return !val ? 0 : val;
    });
    console.log("puzzleValues", puzzleValues);
    if(hasDuplicates(puzzleValues)){
      errorMsg.className = "error";
      errorMsg.innerHTML = "Invalid puzzle: has duplicated values.";
    } else {
      request('POST', '/puzzle', {"puzzle": puzzleValues}, function(resp) {
        if(resp.message) {
          var template = $('#template-steps').html();
          Mustache.parse(template);
          var steps = false, counter = -1;
          if(resp.solution) {
            steps = resp.solution.map(function(step){
              step = step.map(function(number) {
                return number == 0 ? false : number;
              });
              var styledStep = [];
              counter += 1;
              while(step.length) styledStep.push({"lines": step.splice(0,3)});
              return {"step": styledStep, "count": counter};
            });
          }
          console.log(resp, steps);
          var rendered = Mustache.render(template, {"steps": steps, "message": resp.message});
          $('.puzzle-steps').html(rendered);
        }
        errorMsg.className = "";
        errorMsg.innerHTML = "";
      });
    }
    return false;
  }

  function clearPuzzle() {
    puzzleValues = [0, 0, 0, 0, 0, 0, 0, 0, 0];
    var errorMsg = document.getElementById("puzzle-error-msg");
    errorMsg.className = "";
    errorMsg.innerHTML = "";
    var inputs = document.getElementsByTagName('input');
    for (var index = 0; index < inputs.length; ++index) {
      var elem = inputs[index];
      if(elem.type == "number") {
        elem.className = "";
        elem.value = "";
      }
    }
  }

  function randomPuzzle() {
    swal({
      title: "Are you sure?",
      text: "Getting a random puzzle, may generate a puzzle that has no solution. Taking a long time to get a response.",
      type: "warning",
      showCancelButton: true,
      confirmButtonColor: "#DD6B55",
      confirmButtonText: "Yes, generate it!"
    },
    function(){
      getPuzzle();
    });
  }

  function getPuzzle() {
    clearPuzzle();
    request('GET', '/puzzle', null, function(resp) {
      if(resp.puzzle) {
        puzzleValues = resp.puzzle;
        var inputs = document.getElementsByTagName('input');
        for (var index = 0; index < inputs.length; ++index) {
          var elem = inputs[index];
          if(elem.type == "number") {
            elem.className = "";
            var value = resp.puzzle[index]
            elem.value = value == 0 ? "" : value;
          }
        }
      }
    });
  }

  function isNumeric(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
  }

  function validatePuzzle(val, pos, el) {
    var errorMsg = document.getElementById("puzzle-error-msg");
    if(!isNumeric(val) && val != "") {
      el.className = "error";
      errorMsg.className = "error";
      errorMsg.innerHTML = "Invalid number.";
      return;
    }
    var number = parseInt(val);
    if(number < 1 || number > 8) {
      el.className = "error";
      errorMsg.className = "error";
      errorMsg.innerHTML = "Number must be in the range 1-8.";
      return;
    }
    var foundIndex = puzzleValues.indexOf(number);
    if(foundIndex != -1 && foundIndex != pos) {
      el.className = "error";
      errorMsg.className = "error";
      errorMsg.innerHTML = "That number is already set.";
      return;
    }
    if(!number) {
      number = 0;
    }
    el.className = "";
    errorMsg.className = "";
    errorMsg.innerHTML = "";
    puzzleValues[pos] = number;
  }

  this.randomGlow = randomGlow;
  this.getSolution = getSolution;
  this.clearPuzzle = clearPuzzle;
  this.randomPuzzle = randomPuzzle;
  this.validatePuzzle = validatePuzzle;
}

var app = new kickoff();

window.addEventListener('load', function() {
  app.randomGlow();
}, false);
