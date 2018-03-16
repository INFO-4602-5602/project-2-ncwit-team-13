tabs = ["all","ue","ef","es","other"];
// Sets the initial tabPosition to 0 (all)
tabPosition = 0;

$(document).ready(function() {  // do when document is loaded
    switchTabs(tabPosition)
});


// When you click a button, use the switchTabs() function
$("#all").click(function() {
  switchTabs(0)
});

$("#ue").click(function() {
  switchTabs(1)
});

$("#ef").click(function() {
  switchTabs(2)
});

$("#es").click(function() {
  switchTabs(3)
});

$("#other").click(function() {
  switchTabs(4)
});


// This function switches highlight and content based on tabPosition.
// tabPosition 0 = all; 1 = upon enrollment; 2 = end of first year; 3 = end of second year; 4 = other

function switchTabs(tabPosition) {
  if (tabPosition == 0){
    // Show all majors image and hide others
      $("#all-content").show();
      $("#ue-content").hide();
      $("#ef-content").hide();
      $("#es-content").hide();
      $("#other-content").hide();

  // Make all majors button active and all others inactive
      $("#all").addClass("active");
      $("#ue").removeClass("active");
      $("#ef").removeClass("active");
      $("#es").removeClass("active");
      $("#other").removeClass("active");

    // reset tabPosition (just in case)
      tabPosition = 0;
  }

  if (tabPosition == 1){
    // Show upon enrollment image and hide others
      $("#all-content").hide();
      $("#ue-content").show();
      $("#ef-content").hide();
      $("#es-content").hide();
      $("#other-content").hide();

      // Make upon enrollment button active and all others inactive
          $("#all").removeClass("active");
          $("#ue").addClass("active");
          $("#ef").removeClass("active");
          $("#es").removeClass("active");
          $("#other").removeClass("active");

      tabPosition = 1;
  }
  if (tabPosition == 2){

    // Show end of first year  image and hide others
      $("#all-content").hide();
      $("#ue-content").hide();
      $("#ef-content").show();
      $("#es-content").hide();
      $("#other-content").hide();

      // Make end of first year  button active and all others inactive
          $("#all").removeClass("active");
          $("#ue").removeClass("active");
          $("#ef").addClass("active");
          $("#es").removeClass("active");
          $("#other").removeClass("active");

      tabPosition = 2;

  }
  if (tabPosition == 3){

    // Show end of second year image and hide others
      $("#all-content").hide();
      $("#ue-content").hide();
      $("#ef-content").hide();
      $("#es-content").show();
      $("#other-content").hide();

      // Make end of second year button active and all others inactive
          $("#all").removeClass("active");
          $("#ue").removeClass("active");
          $("#ef").removeClass("active");
          $("#es").addClass("active");
          $("#other").removeClass("active");

      tabPosition = 3;
  }

  if (tabPosition == 4){

    // Show other image and hide others
      $("#all-content").hide();
      $("#ue-content").hide();
      $("#ef-content").hide();
      $("#es-content").hide();
      $("#other-content").show();

      // Make other button active and all others inactive
          $("#all").removeClass("active");
          $("#ue").removeClass("active");
          $("#ef").removeClass("active");
          $("#es").removeClass("active");
          $("#other").addClass("active");

      tabPosition = 4;
  }


}

// This listens for key strokes and updates tab position based on the direction
// It then calls the tabPosition() function to update the content
document.addEventListener('keypress', (event) => {
const keyName = event.key;
if (keyName == "ArrowLeft"){
  tabPosition = tabPosition-1;
  if (tabPosition == -1){
    tabPosition = 3
  }
  switchTabs(tabPosition)
}
if (keyName == "ArrowRight"){
  tabPosition = tabPosition+1;
  if (tabPosition == 4){
    tabPosition = 0
  }
  switchTabs(tabPosition)
}
});

// Switching tabs with the gesture nav
$("#gesture-box-2").mousedown(function(event) {

  downX = event.pageX;
  downY = event.pageY;

}
);

$("#gesture-box-2").mouseup(function(event) {
  upX = event.pageX;
  upY = event.pageY;

    // Navigate to the left on a right swipe
  if ((upX - downX) > 20) {
    tabPosition = tabPosition-1;
    if (tabPosition == -1){
      tabPosition = 3
    }
    switchTabs(tabPosition)
  }
  // Navigate to the right on a left swipe
  else if ((upX - downX) < -20) {
    tabPosition = tabPosition+1;
    if (tabPosition == 4){
      tabPosition = 0
    }
    switchTabs(tabPosition)
  }

}
);
