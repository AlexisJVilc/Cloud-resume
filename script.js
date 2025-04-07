var counterContainer = document.querySelector(".website-counter");
var resetButton = document.querySelector("#reset");
var visitCount = localStorage.getItem("page_view");

if (visitCount) {
  visitCount = Number(visitCount) + 1;
  localStorage.setItem("page_view", visitCount);
} else {
  visitCount = 1;
  localStorage.setItem("page_view", 1);
}
counterContainer.innerHTML = visitCount;

resetButton.addEventListener("click", () => {
  visitCount = 1;
  localStorage.setItem("page_view", 1);
  counterContainer.innerHTML = visitCount;
});

const counter = document.querySelector(".counter-number");
async function updateCounter() {
  try {
    let response = await fetch("https://6hnsxdohyuc6uzrxg4bhvysjxq0qzphk.lambda-url.us-west-2.on.aws/");
    let data = await response.json();
    counter.innerHTML = ` This page has ${data} Views!`;
  } catch (error) {
    console.error("Error fetching counter data:", error);
    counter.innerHTML = "Counter unavailable.";
  }
}

updateCounter();