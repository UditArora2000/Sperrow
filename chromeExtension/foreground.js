console.log("Here!");
// let newDiv = document.getElementsByClassName(
//   "public-DraftStyleDefault-block public-DraftStyleDefault-ltr"
// )[0];

let sperrowIcon = document.createElement("img");
sperrowIcon.src = "https://i.ibb.co/cLfVSR6/icon.png";

let sperrowIconContainer = document.createElement("div");
sperrowIconContainer.id = "sperrowIcon";
sperrowIconContainer.style = "cursor:pointer";

sperrowIconContainer.appendChild(sperrowIcon);

let fetchButton = document.createElement("button");
fetchButton.src =
  "https://i.ibb.co/1mD9WDB/Mountain-Landscape-Twitter-Header.png";
// fetchButton.innerText = "Close";
fetchButton.id = "closeExtensionBox";
// fetchButton.style.fontFamily = "Impact,Charcoal,sans-serif";
// fetchButton.style.Color = "White";
fetchButton.style.bottom = "10px";
fetchButton.style.position = "absolute";
fetchButton.style.alignContent = "center";
fetchButton.style.alignItems = "center";
fetchButton.style.alignSelf = "center";
// fetchButton.style.background = "#1DA1F2";

let fetchButton1 = document.createElement("button");
fetchButton1.innerText = "Dashboard";
fetchButton1.id = "gotodashboard";
fetchButton1.style.fontFamily = "Impact,Charcoal,sans-serif";
fetchButton1.style.color = "White";
fetchButton1.style.bottom = "10px";
fetchButton1.style.position = "absolute";
fetchButton1.style.alignContent = "right";
fetchButton1.style.alignItems = "right";
fetchButton1.style.alignSelf = "right";
fetchButton1.style.width = "120px";
fetchButton1.style.height = "30px";
fetchButton1.style.background = "#1DA1F2";

document
  .getElementsByClassName("css-1dbjc4n r-1awozwy r-18u37iz r-a1ub67")[0]
  .appendChild(sperrowIconContainer);

console.log("isSuccess??");

document.getElementById("sperrowIcon").onclick = function () {
  console.log("wut?");
  let newDiv = document.getElementsByClassName(
    "public-DraftStyleDefault-block public-DraftStyleDefault-ltr"
  )[0];
  let spanElement = newDiv.childNodes[0];
  const userText = spanElement.textContent;
  //   console.log(spanElement.textContent);
  let twitterDiv = document.getElementsByClassName(
    "css-1dbjc4n r-1ihkh82 r-j7yic r-rull8r r-qklmqi r-mxfbl1 r-1efd50x r-5kkj8d r-vz2u4x"
  )[0];
  twitterDiv.appendChild(fetchButton);
  twitterDiv.style.height = "150px";
  document.getElementById("closeExtensionBox").onclick = function () {
    // document.getElementById("extensionContent").remove();
    let twitterDiv = document.getElementsByClassName(
      "css-1dbjc4n r-1ihkh82 r-j7yic r-rull8r r-qklmqi r-mxfbl1 r-1efd50x r-5kkj8d r-vz2u4x"
    )[0];
    twitterDiv.style.height = "0px";
  };
  twitterDiv.appendChild(fetchButton1);
  document.getElementById("gotodashboard").onclick = function () {
    // document.getElementById("extensionContent").remove();
    location.href = "http://127.0.0.1:8000/Desktop/Sperrow/web%20app/";
  };
  chrome.storage.local.set({ userTweet: userText });
  chrome.runtime.sendMessage({ message: "tweet received" });
};

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  console.log(request, "received");
  // let extensionContentDiv = document.createElement("div");
  // extensionContentDiv.id = "extensionContent";
  // extensionContentDiv.style.overflow = "auto";
  // let twitterDiv = document.getElementsByClassName(
  //   "css-1dbjc4n r-1ihkh82 r-j7yic r-rull8r r-qklmqi r-mxfbl1 r-1efd50x r-5kkj8d r-vz2u4x"
  // )[0];
  // twitterDiv.appendChild(extensionContentDiv);
  request = JSON.parse(request)
  setTimeout(() => {
      let extensionContentDiv = document.createElement("div");
      extensionContentDiv.id = "extensionContent";
      extensionContentDiv.style.overflow = "auto";
      let twitterDiv = document.getElementsByClassName(
        "css-1dbjc4n r-1ihkh82 r-j7yic r-rull8r r-qklmqi r-mxfbl1 r-1efd50x r-5kkj8d r-vz2u4x"
      )[0];
      twitterDiv.appendChild(extensionContentDiv);
      let pTag = document.createElement("p");
      pTag.innerHTML = request["abcd"];
      pTag.id = "summaryContentText";
      extensionContentDiv.append(pTag);
    }, 30000);
  // add request to this div
});
