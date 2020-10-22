import React from 'react'
import { connect } from 'react-redux'
import { TextField, Button } from '@material-ui/core'
import Board from './Board'
import Sidebar from './Sidebar'
import GameOver from './GameOver'
import '../../styles/game.css'
import { updateGame, setDialogVisibility, socket } from '../../actions/Actions'


const Game = ({updateGame, setDialogVisibility}) => {
    React.useEffect(() => {
        socket.on('request_move', (data) => {
            updateGame(data.p1, data.p2, data.turns, data.history)
        })
        socket.on('game_won', (data) => {
            updateGame(data.p1, data.p2, data.turns, data.history)
            setDialogVisibility(true)
        })

        return function cleanup() {
            socket.off('request_move')
            socket.off('game_won')
        }
    }, [])

    return (
        <div className='flex-container'>
            <GameOver socket={socket}/>
            <Board socket={socket}/>
            <Sidebar socket={socket}/>
        </div>
    )
}

const mapDispatchToProps = dispatch =>({
    updateGame: (p1, p2, turns, history) => dispatch(updateGame(p1, p2, turns, history)),
    setDialogVisibility: (visibility) => dispatch(setDialogVisibility(visibility)),
})
export default connect(null, mapDispatchToProps)(Game)
