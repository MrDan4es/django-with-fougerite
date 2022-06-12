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
        console.log(data['online'])
        if (data['online'] === true) {
            $('#main_div').removeClass()
            $('#main_div').text('SERVER ONLINE!')
            $('#main_div').addClass('row bg-success h-100 w-100 justify-content-center align-items-center h1 g-0')
        } else {
            $('#main_div').removeClass()
            $('#main_div').text('SERVER OFFLINE')
            $('#main_div').addClass('row bg-danger h-100 w-100 justify-content-center align-items-center h1 g-0')
        }
    }
})