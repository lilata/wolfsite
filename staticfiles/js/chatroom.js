function onJoinRoom(){
    const roomName = document.getElementById('room_name_input').value
    if (roomName === '') {
        return
    }
    window.location.href = `/chat/room/${roomName}/`
}
function onNewRoom() {
    window.location.href = '/chat/new_room'
}