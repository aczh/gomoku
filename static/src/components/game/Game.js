import React from 'react'
import { connect } from 'react-redux'
import { TextField, Button } from '@material-ui/core'
import Board from './Board'
import Sidebar from './Sidebar'
import GameOver from './GameOver'
import '../../styles/game.css'
import { updateGame, setDialogVisibility } from '../../actions/Actions'

import io from 'socket.io-client'
const socket = io(process.env.API_URL)


const Game = ({updateGame, setDialogVisibility}) => {
    React.useEffect(() => {
        socket.on('request_move', (data) => {
            updateGame(data.p1, data.p2, data.turns, data.history)
        })
        socket.on('game_won', (data) => {
            updateGame(data.p1, data.p2, data.turns, data.history)
            setDialogVisibility(true)
            // set turns to turns + 1 so it isn't our move
            // this prevents users from making additional moves (hacky, but works)
            updateGame(data.p1, data.p2, data.turns + 1, data.history)
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
