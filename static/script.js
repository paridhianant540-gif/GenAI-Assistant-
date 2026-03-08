console.log("JS Loaded")

let sessionId = Math.random().toString(36).substring(7)

async function sendMessage(){

    const input = document.getElementById("input")

    const message = input.value

    if(message.trim() === ""){
        return
    }

    const messages = document.getElementById("messages")

    const userDiv = document.createElement("div")
    userDiv.innerHTML = "<b>You:</b> " + message
    messages.appendChild(userDiv)

    input.value = ""

    const loading = document.createElement("div")
    loading.innerHTML = "Assistant is thinking..."
    messages.appendChild(loading)

    const res = await fetch("/api/chat",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body: JSON.stringify({
            sessionId: sessionId,
            message: message
        })

    })

    const data = await res.json()

    messages.removeChild(loading)

    const div = document.createElement("div")

    div.innerHTML = "<b>Assistant:</b> " + data.reply

    messages.appendChild(div)

    messages.scrollTop = messages.scrollHeight
}
