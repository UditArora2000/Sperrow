let activeTabID = 0;
chrome.tabs.onActivated.addListener((tab) => {
  chrome.tabs.get(tab.tabId, (current_tab_info) => {
    activeTabID = tab.tabId;
    console.log(current_tab_info.url);
    const websiteURL = current_tab_info.url;
    if (websiteURL.includes("twitter")) {
      chrome.tabs.executeScript(null, { file: "./foreground.js" }, () => {
        console.log("I have injected");
      });
    }
  });
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.message === "tweet received") {
    chrome.storage.local.get("userTweet", (value) => {
      const userTweetText = value.userTweet;
      let req = new XMLHttpRequest();
      const baseUrl = "http://127.0.0.1:5000/getSummaryData";
      const urlParams = `userTweetText=${userTweetText}`;

      req.open("POST", baseUrl, true);
      req.setRequestHeader("Content-Type", "application/json");
      req.send(urlParams);
      req.onreadystatechange = function () {
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
          console.log(JSON.parse(this.response));
          chrome.tabs.sendMessage(activeTabID, this.response);
        }
      };
    });
  }
});
