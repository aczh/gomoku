import React, {useEffect} from 'react'
import { connect } from 'react-redux'
import { TextField, Button, Grid, Paper } from '@material-ui/core'
import '../../styles/sidebar.css'

const Sidebar = ({setGameID, socket, game_id, history}) => {
    const construct_history = () => {
        let move_list = []
        for (let i = 0; i < history.length; i++){
            if (i % 2 === 0){
                move_list.push(<Grid item xs={4} key={`index${i}`}>{`${i / 2}.`}</Grid>)
            }
            move_list.push(<Grid item xs={4} key={i}>{`${String.fromCharCode('A'.charCodeAt()+history[i][1])}${history[i][0]+1}`}</Grid>)
        }
        return move_list
    }

    return (
        <div className='sidebar'>
            <div className='row'>
                <Button variant='contained' color='primary' disableElevation onClick={() => socket.emit('start_game')}>
                    New Game
                </Button>
            </div>
            <Grid container spacing={3} className='history'>
                {construct_history()}
            </Grid>
        </div>
    )
}

const mapStateToProps = state => ({
    game_id: state.game.game_id,
    history: state.game.history,
})
export default connect(
  mapStateToProps,
  null,
)(Sidebar)
