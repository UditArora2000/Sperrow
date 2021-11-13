chrome.tabs.onActivated.addListener((tab) => {
  // fetch("http://localhost:3000/get_companies", {
  //   var1: "yesss",
  // })
  //   .then((r) => r.text())
  //   .then((result) => {
  //     console.log(result, "pleaseee");
  //   });
  let text = "my text";
  let req = new XMLHttpRequest();
  const baseUrl = "http://127.0.0.1:5000/getSummaryData";
  const urlParams = `text=${text}`;

  req.open("POST", baseUrl, true);
  // req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  req.setRequestHeader("Content-Type", "application/json");
  req.send(urlParams);
  req.onreadystatechange = function () {
    // Call a function when the state changes.
    if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
      console.log(JSON.parse(this.response));
    }
  };
  console.log(tab);
});

// request: tweet  -> python helper -> generates response
// response: render summary
