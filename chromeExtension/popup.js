document.addEventListener(
  "DOMContentLoaded",
  function () {
    var checkPageButton = document.getElementById("checkPage");
    checkPageButton.addEventListener(
      "click",
      function () {
        console.log("anything??");
        let newDiv = document.getElementsByClassName(
          "public-DraftStyleDefault-block public-DraftStyleDefault-ltr"
        );
        console.log(newDiv);
      },
      false
    );
  },
  false
);
