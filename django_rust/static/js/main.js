$(document).ready(function() {
    const socket = new ReconnectingWebSocket(
        'ws://' + window.location.host + '/ws/'
    )

    let tagsToReplace = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '\\': '&#92'
    }

    function replaceTag(tag) {
        return tagsToReplace[tag] || tag
    }

    function safeTagsReplace(str) {
        return str.replace(/[&<>\\]/g, replaceTag)
    }

    socket.onmessage = function(e) {
        const data = JSON.parse(e.data)
        console.log(data)
        switch (data.command) {
            case 'server':
                if (data.online === true) {
                    $('#main_div').removeClass()
                    $('#main_div').text('SERVER ONLINE!')
                    $('#main_div').addClass('row bg-success w-100 justify-content-center align-items-center h1 g-0')
                } else {
                    $('#main_div').removeClass()
                    $('#main_div').text('SERVER OFFLINE')
                    $('#main_div').addClass('row bg-danger w-100 justify-content-center align-items-center h1 g-0')
                }
                break
            case 'player':
                break
            case 'chat':
                let message = safeTagsReplace(data.text)
                let date = new Date(data.create_date)
                dateString = date.getHours() + ":" + String(date.getMinutes()).padStart(2, "0")
                    $('#chat').append(`
            <div class="col-12 p-0">
                <div class="border" style="min-height: 60px; border-radius: 0.25rem; background-color: var(--bs-gray-100);">
                    <div class="row justify-content-between">
                        <font class="w-auto mx-1 text-decoration-none 'text-success'" data-username="${data.nickname}"><i>${data.nickname}</i></font>
                        <div class="w-auto mx-1" style="color: var(--bs-gray-600)">${dateString}</div>
                    </div>
                    <div class="mx-1 text-break" style="white-space: pre-wrap;">${message}</div>
                </div>
            </div>`)
                let objDiv = document.getElementById("scrollarea")
                objDiv.scrollTop = objDiv.scrollHeight
                break
        }
    }
})