document.addEventListener('DOMContentLoaded', () => {
    var socket = io.connect(location.protocol + '//' + window.location.hostname + ':' + location.port)
    socket.on('connect', () => {
        document.querySelectorAll('button').forEach(button => {
            button.onlick = () => {
                const selection = button.dataset.vote;
                socket.emit('submit vote',{'selection': selection}) //这个函数给服务器传递并将信息广播给所有客户端
            }
        })
    })

    socket.on('announce vote', data => {
        const li = document.createElement('li');
        li.innerHTML = `Vote recorded: ${data.selection}`;
        document.querySelector('#votes').append(li);
    })
}) 