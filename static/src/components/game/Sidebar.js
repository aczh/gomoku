import React, {useState, useEffect} from 'react'
import { connect } from 'react-redux'
import { setGameID } from '../../actions/Actions'
import { TextField, Button } from '@material-ui/core'
import '../../styles/sidebar.css'

const Sidebar = ({setGameID, socket, game_id}) => {
    const new_game = () => {
        let game_id = new Date().getTime()
        setGameID(game_id)
        socket.emit('start_game', {game_id: game_id})
    }

    useEffect(() => {
        if (game_id !== null){
            console.log(game_id)
            socket.emit('start_game', {game_id: game_id})
        }
    })

    socket.on('game_won', () => {
        console.log("GAME WON")
    })

    return (
        <div className='sidebar'>
            <div className='row'>
                <Button variant='contained' color='primary' disableElevation onClick={() => new_game()}>
                    New Game
                </Button>
            </div>
        </div>
    )
}

const mapStateToProps = state => ({
    game_id: state.game.game_id
})
const mapDispatchToProps = dispatch =>({
    setGameID: (game_id) => dispatch(setGameID(game_id))
})
export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(Sidebar)
