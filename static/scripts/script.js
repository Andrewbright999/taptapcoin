let input_id = document.getElementById("id-input");
input_id.value = 1
let balance_element = document.getElementById("balance-count");
var ws = new WebSocket('ws://localhost:8000/ws');
let TapBtn  = document.getElementById("tap-button");
let UpgradeBtn  = document.getElementById("upgrade-button");

ws.onmessage = function(event) {
    let user_data = JSON.parse(event.data)
    let balance = user_data["balance"]
    console.log(user_data)
    console.log(user_data[0])
    balance_element.innerText = '';
    balance_element.innerText = balance;
};

TapBtn.addEventListener("click", async function(event){
    id = input_id.value
    data = {
        "id": id,
        "event":"click"
    }
    ws.send(JSON.stringify(data))
    event.preventDefault()
});

UpgradeBtn.addEventListener("click", async function(event){
    id = input_id.value
    data = {
        "id": id,
        "event":"buy_upgrade"
    }
    ws.send(JSON.stringify(data))
    event.preventDefault()
});

// function sendMessage(event) {
//     var input = document.getElementById("messageText")
//     ws.send(input.value)
//     input.value = ''



